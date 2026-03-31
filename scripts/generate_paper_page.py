#!/usr/bin/env python3
"""
CHRI-Lab Paper Page Generator
Called by .github/workflows/paper-page.yml

Reads inputs from environment variables, extracts paper information,
calls the Claude API to draft content, and writes:
  - _papers/<slug>.md
  - Updated _bibliography/papers.bib (appended)
  - $GITHUB_ENV values for the PR step (PAPER_SLUG, PAPER_TITLE, PR_BODY)
"""

import os
import re
import sys
import json
import textwrap
from pathlib import Path

import anthropic
import requests
import yaml
from bs4 import BeautifulSoup

# ── Optional imports with fallbacks ──────────────────────────────────────────

try:
    from pypdf import PdfReader
    HAS_PYPDF = True
except ImportError:
    HAS_PYPDF = False


try:
    import bibtexparser
    from bibtexparser.bparser import BibTexParser
    HAS_BIBTEX = True
except ImportError:
    HAS_BIBTEX = False

# ── Venue logo lookup ─────────────────────────────────────────────────────────
# Maps keywords found in venue names to a stable logo URL.
# The PI can extend this list or override via the venue_logo front matter field.
VENUE_LOGOS = {
    "chi":     "https://sigchi.org/wp-content/uploads/2024/01/cropped-sigchi-icon-192x192.png",
    "cscw":    "https://sigchi.org/wp-content/uploads/2024/01/cropped-sigchi-icon-192x192.png",
    "uist":    "https://sigchi.org/wp-content/uploads/2024/01/cropped-sigchi-icon-192x192.png",
    "idc":     "https://sigchi.org/wp-content/uploads/2024/01/cropped-sigchi-icon-192x192.png",
    "assets":  "https://sigchi.org/wp-content/uploads/2024/01/cropped-sigchi-icon-192x192.png",
    "iui":     "https://sigchi.org/wp-content/uploads/2024/01/cropped-sigchi-icon-192x192.png",
    "hri":     "https://humanrobotinteraction.org/wp-content/uploads/2022/09/cropped-hri-logo-192x192.png",
    "ro-man":  "https://www.ieee-ras.org/images/logos/ieee-ras-logo.png",
    "roman":   "https://www.ieee-ras.org/images/logos/ieee-ras-logo.png",
    "iros":    "https://www.ieee-ras.org/images/logos/ieee-ras-logo.png",
    "icra":    "https://www.ieee-ras.org/images/logos/ieee-ras-logo.png",
    "ieee":    "https://www.ieee-ras.org/images/logos/ieee-ras-logo.png",
    "acm":     "https://www.acm.org/binaries/content/gallery/acm/publications/acm-logo.png",
}

def lookup_venue_logo(venue_str):
    """Return a logo URL for a known venue, or empty string."""
    if not venue_str:
        return ""
    lower = venue_str.lower()
    for keyword, url in VENUE_LOGOS.items():
        if keyword in lower:
            return url
    return ""


# ─────────────────────────────────────────────────────────────────────────────
# Input collection
# ─────────────────────────────────────────────────────────────────────────────

def get_inputs():
    return {
        "paper_source": os.environ.get("INPUT_PAPER_SOURCE", "").strip(),
        "pdf_path":     os.environ.get("INPUT_PDF_PATH", "").strip(),
        "bibtex":       os.environ.get("INPUT_BIBTEX", "").strip(),
        "code_url":     os.environ.get("INPUT_CODE_URL", "").strip(),
        "demo_url":     os.environ.get("INPUT_DEMO_URL", "").strip(),
        "dataset_url":  os.environ.get("INPUT_DATASET_URL", "").strip(),
        "slides_url":   os.environ.get("INPUT_SLIDES_URL", "").strip(),
        "video_url":    os.environ.get("INPUT_VIDEO_URL", "").strip(),
        "teaser_path":  os.environ.get("INPUT_TEASER_PATH", "").strip(),
        "notes":        os.environ.get("INPUT_NOTES", "").strip(),
    }


# ─────────────────────────────────────────────────────────────────────────────
# Paper info extraction
# ─────────────────────────────────────────────────────────────────────────────

def extract_arxiv_id(source):
    """Pull an arXiv ID from a bare ID or full URL."""
    source = source.strip()
    m = re.search(r"(\d{4}\.\d{4,5})", source)
    return m.group(1) if m else None


def fetch_arxiv(arxiv_id):
    """Fetch title, authors, abstract from arXiv."""
    print(f"Fetching arXiv metadata for {arxiv_id} …")
    url = f"https://export.arxiv.org/abs/{arxiv_id}"
    try:
        resp = requests.get(url, timeout=20, headers={"User-Agent": "CHRI-Lab-PaperPage/1.0"})
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        title_tag = soup.find("h1", class_="title")
        title = title_tag.get_text(strip=True).replace("Title:", "").strip() if title_tag else ""

        authors_tag = soup.find("div", class_="authors")
        authors_raw = authors_tag.get_text(separator=", ", strip=True).replace("Authors:", "").strip() if authors_tag else ""
        authors = [a.strip() for a in authors_raw.split(",") if a.strip()]

        abstract_tag = soup.find("blockquote", class_="abstract")
        abstract = abstract_tag.get_text(strip=True).replace("Abstract:", "").strip() if abstract_tag else ""

        # Venue / comments
        comments_tag = soup.find("td", class_="tablecell comments")
        venue = comments_tag.get_text(strip=True) if comments_tag else ""

        # Year
        dateline = soup.find("div", class_="dateline")
        year = ""
        if dateline:
            m = re.search(r"\b(20\d{2})\b", dateline.get_text())
            year = m.group(1) if m else ""

        return {"title": title, "authors": authors, "abstract": abstract,
                "venue": venue, "year": year, "arxiv_id": arxiv_id,
                "paper_url": f"https://arxiv.org/pdf/{arxiv_id}"}
    except Exception as e:
        print(f"Warning: could not fetch arXiv page — {e}")
        return {}


def fetch_paper_url(url):
    """Scrape title, authors, abstract from ACM / IEEE / CHRI-Lab / generic URL."""
    print(f"Fetching paper metadata from {url} …")
    try:
        resp = requests.get(url, timeout=20, headers={"User-Agent": "CHRI-Lab-PaperPage/1.0"})
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        # Try common meta tags first (works for most publishers)
        def meta(name=None, prop=None):
            tag = (soup.find("meta", {"name": name}) if name
                   else soup.find("meta", {"property": prop}))
            return tag["content"].strip() if tag and tag.get("content") else ""

        title = (meta(name="citation_title") or meta(prop="og:title")
                 or (soup.find("h1").get_text(strip=True) if soup.find("h1") else ""))

        # Authors from citation_author meta tags
        author_tags = soup.find_all("meta", {"name": "citation_author"})
        authors = [t["content"].strip() for t in author_tags if t.get("content")]
        if not authors:
            authors_raw = meta(prop="og:description") or ""
            # fallback: empty list, Claude will note it's missing
            authors = []

        abstract = (meta(name="citation_abstract") or meta(prop="og:description") or "")
        venue = meta(name="citation_conference_title") or meta(name="citation_journal_title") or ""
        year = meta(name="citation_publication_date") or meta(name="citation_year") or ""
        if year:
            m = re.search(r"\b(20\d{2})\b", year)
            year = m.group(1) if m else year[:4]

        doi = meta(name="citation_doi") or ""
        pdf_url = meta(name="citation_pdf_url") or ""

        return {"title": title, "authors": authors, "abstract": abstract,
                "venue": venue, "year": year, "doi": doi,
                "paper_url": url, "pdf_url": pdf_url}
    except Exception as e:
        print(f"Warning: could not fetch paper URL — {e}")
        return {"paper_url": url}


def extract_pdf_text(pdf_path):
    """Extract text from a PDF, limited to first 12 pages (intro + method + conclusion)."""
    if not HAS_PYPDF:
        print("Warning: pypdf not available, skipping PDF extraction.")
        return ""
    path = Path(pdf_path)
    if not path.exists():
        print(f"Warning: PDF not found at {pdf_path}")
        return ""
    print(f"Extracting text from {pdf_path} …")
    try:
        reader = PdfReader(str(path))
        pages = reader.pages[:12]
        text = "\n\n".join(p.extract_text() or "" for p in pages)
        # Trim to ~12,000 chars to stay within context limits
        return text[:12000]
    except Exception as e:
        print(f"Warning: PDF extraction failed — {e}")
        return ""



def parse_bibtex(bibtex_str):
    """Parse a BibTeX string into a dict."""
    if not bibtex_str:
        return {}
    if not HAS_BIBTEX:
        # Minimal hand-rolled parser as fallback
        fields = {}
        for m in re.finditer(r'(\w+)\s*=\s*\{([^}]*)\}', bibtex_str):
            fields[m.group(1).lower()] = m.group(2).strip()
        return fields
    try:
        parser = BibTexParser(common_strings=True)
        parser.ignore_nonstandard_types = False
        db = bibtexparser.loads(bibtex_str, parser)
        if db.entries:
            return db.entries[0]
    except Exception as e:
        print(f"Warning: BibTeX parsing failed — {e}")
    return {}


def read_existing_authors():
    """Load _data/authors.yml if it exists."""
    path = Path("_data/authors.yml")
    if not path.exists():
        return []
    try:
        with open(path) as f:
            data = yaml.safe_load(f) or []
        return data if isinstance(data, list) else []
    except Exception:
        return []


# ─────────────────────────────────────────────────────────────────────────────
# Claude API — generate page content
# ─────────────────────────────────────────────────────────────────────────────

SYSTEM_PROMPT = """\
You are a research assistant helping the CHRI Lab (Human-Robot Interaction lab at the
University of Sydney) create paper project pages for their Jekyll website.

Your output must be a single JSON object — no prose, no markdown fences, just raw JSON.
The reference aesthetic is cleo.kixlab.org: clean, confident, academic but approachable.
"""

def build_user_prompt(info, inputs, existing_author_names):
    sections = []

    if info.get("title"):
        sections.append(f"TITLE: {info['title']}")
    if info.get("authors"):
        sections.append(f"AUTHORS: {', '.join(info['authors'])}")
    if info.get("abstract"):
        sections.append(f"ABSTRACT:\n{info['abstract']}")
    if info.get("venue"):
        sections.append(f"VENUE: {info['venue']}")
    if info.get("year"):
        sections.append(f"YEAR: {info['year']}")
    if info.get("doi"):
        sections.append(f"DOI: {info['doi']}")
    if info.get("pdf_text"):
        sections.append(f"PDF TEXT (first pages):\n{info['pdf_text']}")
    if info.get("raw_bibtex"):
        sections.append(f"BIBTEX:\n{info['raw_bibtex']}")
    if inputs.get("notes"):
        sections.append(f"EXTRA NOTES FROM SUBMITTER:\n{inputs['notes']}")
    if existing_author_names:
        sections.append(f"AUTHORS ALREADY IN _data/authors.yml: {', '.join(existing_author_names)}")

    paper_info_block = "\n\n".join(sections)

    return f"""\
Here is everything I know about this paper:

{paper_info_block}

Please generate the paper page content as a JSON object with these exact keys:

{{
  "title": "Full paper title",
  "subtitle": "One evocative sentence (max 20 words) capturing the paper's core contribution. Not a repeat of the abstract.",
  "slug": "year-short-title-slug (lowercase, hyphenated, year-prefixed, e.g. 2024-robot-gesture-learning)",
  "authors": [
    {{
      "name": "Full Name",
      "affiliation": "Institution name",
      "url": "personal website URL or empty string"
    }}
  ],
  "venue": "Conference or journal name",
  "year": "YYYY",
  "abstract": "The paper abstract, lightly reformatted for web readability. No column-break artefacts. Preserve the authors' voice. Single string.",
  "keywords": ["Keyword One", "Keyword Two", "Keyword Three"],
  "key_findings": [
    "**Bold claim.** One sentence of supporting context.",
    "**Bold claim.** One sentence of supporting context."
  ],
  "method": "2–3 paragraphs describing the approach in plain language. Use \\n\\n to separate paragraphs.",
  "results": "Plain-language summary of main findings. Include specific numbers where available.",
  "acknowledgements": "Verbatim acknowledgements from the paper, or empty string if not found.",
  "bibtex": "Clean, properly formatted BibTeX entry as a single string",
  "new_authors": ["Full Name of any author NOT already in _data/authors.yml"]
}}

Rules:
- Only include what you know. Do not invent paper content.
- If a field is unknown, use an empty string or empty list.
- key_findings: 3–5 items.
- keywords: 4–8 short phrases, title case.
- The bibtex entry should include all standard fields. Add a website field pointing to the full URL: website = {{https://chri-lab.github.io/papers/<slug>/}}
- For authors already in _data/authors.yml, still include them in the authors array (their photo/URL will be looked up later).
"""


def call_claude(client, info, inputs, existing_author_names):
    print("Calling Claude API to generate page content …")
    prompt = build_user_prompt(info, inputs, existing_author_names)

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = message.content[0].text.strip()

    # Strip any accidental markdown fences
    raw = re.sub(r"^```(?:json)?\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)

    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"Error: Claude returned invalid JSON — {e}")
        print("Raw response:", raw[:500])
        sys.exit(1)


# ─────────────────────────────────────────────────────────────────────────────
# File generation
# ─────────────────────────────────────────────────────────────────────────────

def make_slug(title, year):
    """Convert title + year to a URL slug."""
    slug = re.sub(r"[^\w\s-]", "", title.lower())
    slug = re.sub(r"[\s_]+", "-", slug).strip("-")
    # Trim to reasonable length
    parts = slug.split("-")[:6]
    slug = "-".join(parts)
    return f"{year}-{slug}" if year else slug


def build_frontmatter(page, inputs, existing_authors_map):
    """Build the YAML front matter dict."""

    # Resolve author photos from existing authors map
    authors_out = []
    for a in page.get("authors", []):
        name = a.get("name", "")
        existing = existing_authors_map.get(name.lower())
        photo = ""
        if existing:
            photo = existing.get("photo", "")
            url = a.get("url") or existing.get("url", "")
            affiliation = a.get("affiliation") or existing.get("affiliation", "")
        else:
            url = a.get("url", "")
            affiliation = a.get("affiliation", "")
            photo = f"/assets/authors/{re.sub(r'[^a-z]', '', name.lower())}.jpg"

        entry = {"name": name}
        if affiliation:
            entry["affiliation"] = affiliation
        if url:
            entry["url"] = url
        if photo:
            entry["photo"] = photo
        authors_out.append(entry)

    fm = {
        "layout": "paper",
        "title": page.get("title", ""),
        "subtitle": page.get("subtitle", ""),
        "slug": page.get("slug", ""),
        "authors": authors_out,
        "venue": page.get("venue", ""),
        "year": page.get("year", ""),
        "abstract": page.get("abstract", ""),
        "keywords": page.get("keywords", []),
    }

    # Optional links
    for key in ("arxiv", "paper_url", "code_url", "demo_url", "dataset_url", "slides_url", "video_url"):
        input_key = key  # matches input names directly
        val = (inputs.get(input_key) or "").strip()
        if key == "arxiv":
            val = (page.get("arxiv_id") or "").strip()
        if val:
            fm[key] = val

    # Teaser
    if inputs.get("teaser_path"):
        fm["teaser_image"] = f"/{inputs['teaser_path'].lstrip('/')}"

    # Venue logo
    venue_logo = lookup_venue_logo(page.get("venue", ""))
    if venue_logo:
        fm["venue_logo"] = venue_logo

    # Acknowledgements
    ack = page.get("acknowledgements", "").strip()
    if ack:
        fm["acknowledgements"] = ack

    # BibTeX — replace relative /papers/<slug>/ with full URL
    bibtex = page.get("bibtex", "").strip()
    if bibtex:
        bibtex = re.sub(
            r"website\s*=\s*\{/papers/([^}]+)/\}",
            r"website     = {https://chri-lab.github.io/papers/\1/}",
            bibtex
        )
        fm["bibtex"] = bibtex

    return fm


def fm_to_yaml(fm):
    """Serialise front matter to YAML string, keeping multiline strings readable."""
    return yaml.dump(fm, allow_unicode=True, default_flow_style=False,
                     sort_keys=False, width=100)


def build_body(page):
    """Build the Markdown body (everything below front matter)."""
    lines = []

    # Key findings
    findings = page.get("key_findings", [])
    if findings:
        lines.append("## Key Findings\n")
        lines.append('<ul class="findings-list">')
        for f in findings:
            lines.append(f"  <li>{f}</li>")
        lines.append("</ul>\n")

    # Method
    method = page.get("method", "").strip()
    if method:
        lines.append("## Method\n")
        lines.append(method + "\n")

    # Results
    results = page.get("results", "").strip()
    if results:
        lines.append("## Results\n")
        lines.append(results + "\n")

    return "\n".join(lines)


def write_paper_md(page, inputs, existing_authors_map, slug):
    """Write _papers/<slug>.md"""
    out_path = Path("_papers") / f"{slug}.md"
    out_path.parent.mkdir(exist_ok=True)

    if out_path.exists():
        print(f"Warning: {out_path} already exists — skipping to avoid overwrite. Rename manually if needed.")
        return

    fm = build_frontmatter(page, inputs, existing_authors_map)
    body = build_body(page)

    content = f"---\n{fm_to_yaml(fm)}---\n\n{body}\n"
    out_path.write_text(content, encoding="utf-8")
    print(f"Written: {out_path}")


def update_bib_file(bibtex_entry, slug, paper_url=None):
    """Append BibTeX entry to _bibliography/papers.bib if not already present."""
    bib_path = Path("_bibliography/papers.bib")
    if not bib_path.exists():
        print(f"Warning: {bib_path} not found — skipping BibTeX update.")
        return

    existing = bib_path.read_text(encoding="utf-8")

    # Inject website field if not present
    if "website" not in bibtex_entry and slug:
        bibtex_entry = bibtex_entry.rstrip().rstrip("}")
        bibtex_entry += f',\n  website     = {{/papers/{slug}/}}'\
                        f'\n}}'

    # Check for duplicate by comparing the entry key
    key_match = re.match(r"@\w+\{([^,]+),", bibtex_entry)
    if key_match:
        entry_key = key_match.group(1).strip()
        if entry_key in existing:
            print(f"BibTeX key '{entry_key}' already in papers.bib — skipping append.")
            return

    with open(bib_path, "a", encoding="utf-8") as f:
        f.write(f"\n{bibtex_entry}\n")
    print(f"Appended BibTeX entry to {bib_path}")


# ─────────────────────────────────────────────────────────────────────────────
# GitHub Actions environment outputs
# ─────────────────────────────────────────────────────────────────────────────

def set_github_env(key, value):
    """Write a key=value pair to $GITHUB_ENV for subsequent workflow steps."""
    env_file = os.environ.get("GITHUB_ENV")
    if env_file:
        with open(env_file, "a") as f:
            # Use heredoc delimiter to handle multiline values safely
            delimiter = "EOF_GHENV"
            f.write(f"{key}<<{delimiter}\n{value}\n{delimiter}\n")


def build_pr_body(page, new_authors, slug, inputs):
    author_list = ", ".join(a.get("name", "") for a in page.get("authors", []))
    lines = [
        f"**Paper:** {page.get('title', '')}  ",
        f"**Authors:** {author_list}  ",
        f"**Venue:** {page.get('venue', '')} {page.get('year', '')}  ",
        f"**Page URL:** https://chri-lab.github.io/papers/{slug}/  ",
        "",
        "### Review checklist",
        "",
        "- [ ] Abstract is accurate and reads well",
        "- [ ] Key findings reflect the paper's contributions",
        "- [ ] Method description is correct",
        "- [ ] Author names and affiliations are correct",
        "- [ ] All provided URLs are correct",
    ]

    if inputs.get("teaser_path"):
        lines.append(f"- [x] Teaser image set to `{inputs['teaser_path']}`")
    else:
        lines += [
            "- [ ] Add a teaser image:",
            f"  - Drop it into `assets/papers/{slug}/teaser.jpg`",
            f"  - Then add `teaser_image: /assets/papers/{slug}/teaser.jpg` to the front matter",
        ]

    if new_authors:
        lines += [
            "",
            "### ⚠️ New authors — update `_data/authors.yml`",
            "",
            "These authors were not found in `_data/authors.yml`. Add them manually:",
            "",
        ]
        for name in new_authors:
            safe = re.sub(r"[^a-z]", "", name.lower())
            lines += [
                f"```yaml",
                f"- name: {name}",
                f"  affiliation: Their Institution",
                f"  url: https://their-website.com",
                f"  photo: /assets/authors/{safe}.jpg",
                f"```",
                "",
            ]
        lines += [
            f"Upload their photos to `assets/authors/`.",
        ]

    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY is not set.")
        sys.exit(1)

    inputs = get_inputs()

    if not any([inputs["paper_source"], inputs["pdf_path"], inputs["bibtex"]]):
        print("Error: provide at least one of: paper_source, pdf_path, or bibtex.")
        sys.exit(1)

    # ── 1. Collect raw paper info ─────────────────────────────────────────────
    info = {}

    # arXiv
    if inputs["paper_source"]:
        arxiv_id = extract_arxiv_id(inputs["paper_source"])
        if arxiv_id:
            info.update(fetch_arxiv(arxiv_id))
            info["arxiv_id"] = arxiv_id
        else:
            # Generic URL
            info.update(fetch_paper_url(inputs["paper_source"]))
            info["paper_url"] = inputs["paper_source"]

    # PDF
    if inputs["pdf_path"]:
        pdf_text = extract_pdf_text(inputs["pdf_path"])
        if pdf_text:
            info["pdf_text"] = pdf_text
        # Use the PDF path as the paper URL if nothing else provided
        if not info.get("paper_url"):
            info["paper_url"] = f"/{inputs['pdf_path'].lstrip('/')}"

    # BibTeX overrides / supplements
    if inputs["bibtex"]:
        info["raw_bibtex"] = inputs["bibtex"]
        bib = parse_bibtex(inputs["bibtex"])
        if not info.get("title") and bib.get("title"):
            info["title"] = bib["title"]
        if not info.get("year") and bib.get("year"):
            info["year"] = bib["year"]
        if not info.get("venue"):
            info["venue"] = bib.get("booktitle") or bib.get("journal") or ""

    # Extra URLs
    for key in ("code_url", "demo_url", "dataset_url", "slides_url", "video_url"):
        if inputs.get(key):
            info[key] = inputs[key]

    # ── 2. Existing authors ───────────────────────────────────────────────────
    existing_authors = read_existing_authors()
    existing_authors_map = {a.get("name", "").lower(): a for a in existing_authors}
    existing_author_names = list(existing_authors_map.keys())

    # ── 4. Call Claude ────────────────────────────────────────────────────────
    client = anthropic.Anthropic(api_key=api_key)
    page = call_claude(client, info, inputs, existing_author_names)

    # ── 5. Determine slug ─────────────────────────────────────────────────────
    slug = page.get("slug") or make_slug(page.get("title", "paper"), page.get("year", ""))
    slug = re.sub(r"[^\w-]", "", slug).lower().strip("-")
    page["slug"] = slug

    # ── 6. Write files ────────────────────────────────────────────────────────
    write_paper_md(page, inputs, existing_authors_map, slug)
    bibtex_entry = page.get("bibtex", "").strip()
    if bibtex_entry:
        update_bib_file(bibtex_entry, slug)

    # ── 6. Set GitHub Actions outputs ─────────────────────────────────────────
    new_authors = page.get("new_authors", [])
    pr_body = build_pr_body(page, new_authors, slug, inputs)

    set_github_env("PAPER_SLUG", slug)
    set_github_env("PAPER_TITLE", page.get("title", slug))
    set_github_env("PR_BODY", pr_body)

    print(f"\n✓ Done. Slug: {slug}")
    print(f"  Page:  _papers/{slug}.md")
    if bibtex_entry:
        print(f"  BibTeX: appended to _bibliography/papers.bib")
    if new_authors:
        print(f"  New authors to add to _data/authors.yml: {', '.join(new_authors)}")


if __name__ == "__main__":
    main()

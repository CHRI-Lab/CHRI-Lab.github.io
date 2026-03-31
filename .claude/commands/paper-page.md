# /paper-page — CHRI-Lab Paper Page Generator

You are helping a CHRI-Lab researcher create a rich, standalone paper project page for the lab website at https://chri-lab.github.io.

The reference aesthetic is **cleo.kixlab.org** — clean whitespace, confident typography, author cards with photos, and clear visual hierarchy.

---

## STEP 1 — Gather inputs

Ask the user for the following. Tell them to provide **at least one paper source**; the rest are optional but improve the output.

**Paper source (at least one required):**
- PDF file path — e.g. `files/papers/mypaper.pdf`
- arXiv link — e.g. `https://arxiv.org/abs/2603.02050`
- Paper URL — CHRI-Lab site, ACM DL, IEEE Xplore, etc.
- BibTeX entry — paste directly

**Optional extras:**
- Teaser image or video (file path or URL) — `.jpg`, `.png`, `.gif`, `.mp4`, `.webm`
- Author photos (file path or URL, per author)
- Extra links: code repo, demo, dataset, slides, supplemental PDF
- Acknowledgements text (if not in the PDF)

Once gathered, confirm all inputs before proceeding.

---

## STEP 2 — Extract paper information

Use all provided sources. Cross-check and merge; manual inputs always take precedence.

**If a PDF path was given:**
Use the Read tool to read the PDF. Extract:
- Title, authors, affiliations
- Abstract (verbatim)
- Key contributions (from intro / contributions list)
- Method/system description (from method section)
- Main results (quantitative or qualitative)
- Acknowledgements (verbatim if present)
- Figure references (figure numbers and captions)

**If an arXiv link was given:**
Use WebFetch to fetch the abstract page (`https://arxiv.org/abs/<id>`). Extract title, authors, abstract, venue, date. Also note the arXiv ID for the front matter.

**If an ACM / IEEE / CHRI-Lab URL was given:**
Use WebFetch to fetch the page. Extract whatever metadata is available: title, authors, abstract, venue, year, DOI.

**If BibTeX was given:**
Parse: title, authors, year, venue/booktitle, DOI, any URLs already present.

Summarise everything you extracted so the user can verify before you draft anything.

---

## STEP 3 — Check existing authors

Read `_data/authors.yml` (if it exists).

For each author in the paper:
- **Known author** (name matches an entry): use their existing photo, affiliation, and URL.
- **New author**:
  1. If they have a personal website URL (from the paper PDF, arXiv, or provided by the user), use WebFetch to visit the page and look for a profile photo URL.
  2. Create a draft `_data/authors.yml` entry:
     ```yaml
     - name: First Last
       affiliation: University Name
       url: https://their-website.com
       photo: /assets/authors/firstlast.jpg  # or URL if found
     ```
  3. Show the user the new entries and ask: **accept, edit, or skip**.

Do not modify `_data/authors.yml` yet — just build the confirmed list of author records for use in Step 6.

---

## STEP 4 — Draft page content

Using the extracted information, draft each section below. Present them **one at a time**. After each section, ask:

> **[a] accept  [e] edit  [r] regenerate**

For **regenerate**, ask what to change first, then produce a revised draft.

Sections to draft:

1. **Hero subtitle** — one evocative sentence below the title capturing the paper's core contribution. Not a repeat of the abstract. Max 20 words.

2. **Abstract** — the paper's abstract, lightly reformatted for web readability (no column-break artefacts, no hyphenation splits). Do not rewrite; preserve the authors' voice. This goes into the `abstract:` front matter field — output it as a single quoted string.

3. **Keywords** — 4–8 short keyword phrases drawn from the paper's own keyword list (if present) or synthesised from the abstract and contributions. Each keyword: 1–3 words, title case. Output as a YAML list. Example:
   ```yaml
   keywords:
     - Human-Robot Interaction
     - Gesture Recognition
     - Accessibility
   ```

4. **Key findings / contributions** — 3–5 bullet points synthesised from the intro, contributions list, and conclusions. Each bullet: one bold claim + one sentence of context.

5. **Method / system overview** — 2–3 paragraphs in plain language describing the approach. Draw from the method section. Avoid jargon where possible.

6. **Results summary** — plain-language summary of the main quantitative or qualitative findings. Include specific numbers if available.

7. **Figure captions** — cleaned-up captions for any figures the user will include (de-column-break, fix hyphenation, make standalone).

8. **Acknowledgements** — extracted verbatim from the paper (if present). Goes into the `acknowledgements:` front matter field. If not found, ask the user or skip.

Compile all confirmed drafts before moving to Step 5.

---

## STEP 5 — Choose figures

If figures were extracted from the PDF (or the user mentions specific figures), list them:

```
Fig 1 — [caption preview]
Fig 2 — [caption preview]
...
```

Ask: **Which figures do you want on the paper page?** (enter numbers, e.g. `1 3 5`, or `none`)

---

## STEP 6 — Determine the page slug

Suggest a slug: lowercase, hyphenated, year-prefixed, derived from the title.
Example: `2024-adaptive-robot-learning`

Ask the user to confirm or provide their own. The slug is used for:
- The page URL: `https://chri-lab.github.io/papers/<slug>/`
- The output file: `_papers/<slug>.md`
- The asset folder: `assets/papers/<slug>/`

---

## STEP 7 — Generate all files

### 7a. `_papers/<slug>.md`

```markdown
---
layout: paper
title: "Full Paper Title"
subtitle: "AI-drafted hero subtitle"
slug: paper-slug

authors:
  - name: First Author
    affiliation: University of Sydney
    url: https://author1.com
    photo: /assets/authors/firstauthor.jpg
  - name: Second Author
    affiliation: University Name
    url: https://author2.com
    photo: /assets/papers/<slug>/authors/secondauthor.jpg

venue: "Conference or Journal Name"
year: 2024
month: "October"          # optional

abstract: "The paper abstract goes here as a single quoted string. Keep line
  breaks out — YAML multiline strings can cause Jekyll rendering issues."

keywords:
  - Human-Robot Interaction
  - Gesture Recognition
  - Accessibility

# Links — omit any that were not provided
arxiv: "2603.02050"
paper_url: https://...
code_url: https://...
demo_url: https://...
dataset_url: https://...
slides_url: https://...
video_url: https://...

# Teaser — omit if not provided
teaser_image: /assets/papers/<slug>/teaser.jpg
teaser_video: /assets/papers/<slug>/teaser.mp4
teaser_caption: "Optional caption for the teaser."

# Acknowledgements — omit if none
acknowledgements: "This work was supported by ..."

bibtex: |
  @inproceedings{key2024,
    author    = {Author One and Author Two},
    title     = {Paper Title},
    booktitle = {Conference Name},
    year      = {2024},
    doi       = {10.xxxx/xxxxx}
  }
---

## Key Findings

- **Finding one.** Supporting detail in one sentence.
- **Finding two.** Supporting detail in one sentence.
- **Finding three.** Supporting detail in one sentence.

## Method

[2–3 paragraph narrative]

## Results

[Results summary]

## Figures

<div class="paper-figures">
  <figure class="paper-figure">
    <img src="{{ '/assets/papers/<slug>/fig1.png' | relative_url }}" alt="Figure 1">
    <figcaption>Figure 1: Caption text.</figcaption>
  </figure>
</div>

{% if page.video_url %}
## Video

<div class="video-embed">
  <iframe src="{{ page.video_url }}" allowfullscreen></iframe>
</div>
{% endif %}
```

**Rules for the front matter:**
- The `abstract:` field is rendered by the layout automatically — do **not** add an `## Abstract` section in the body.
- `keywords:` is rendered by the layout automatically — do **not** add a keywords section in the body.
- `acknowledgements:` is rendered by the layout automatically — do **not** add an `## Acknowledgements` section in the body.
- Only include front matter fields for links that were actually provided. Omit empty fields.

### 7b. `_bibliography/papers.bib` update

Check if the paper already exists in the bib file (search by title or arXiv ID).

- **New paper**: append the BibTeX entry. Add a `website` field: `website = {/papers/<slug>/}`
- **Existing entry**: show a diff of what will change and ask for confirmation before editing.

### 7c. `assets/papers/<slug>/` directory

List every asset file that belongs here:
- `teaser.jpg` / `teaser.mp4` (if provided)
- `authors/firstauthor.jpg`, etc. (for any new author photos)
- `fig1.png`, `fig2.png`, ... (chosen figures)

For files the user provided as local paths, note that they will be copied.
For files from URLs, provide the exact `curl` or `wget` command to download each one.

### 7d. `_data/authors.yml` update (if new authors confirmed in Step 3)

Show the exact lines to be appended. Ask for final confirmation before writing.

---

## STEP 8 — Review

Show a complete summary:

```
Files to be created:
  ✦ _papers/<slug>.md
  ✦ assets/papers/<slug>/          (directory)

Files to be modified:
  ✦ _bibliography/papers.bib       (BibTeX entry added)
  ✦ _data/authors.yml              (N new authors added)   ← only if applicable

Assets needed in assets/papers/<slug>/:
  • teaser.jpg         ← copy from <source>
  • authors/jo.jpg     ← download from <url>
  • fig1.png           ← copy from <source>
```

Ask: **"Ready to write? Type `yes` to create all files, or tell me what to change."**

---

## STEP 9 — Write files

Use the Write tool to create `_papers/<slug>.md`.
Use the Edit tool to update `_bibliography/papers.bib` and `_data/authors.yml`.

**Never silently overwrite an existing file.** If a file already exists, show a diff and require explicit confirmation.

After all files are written, print:

```
Done! Files written:
  _papers/<slug>.md
  _bibliography/papers.bib  (updated)
  _data/authors.yml         (updated — N new authors)

Next: add your asset files to assets/papers/<slug>/
then commit and push (see instructions below).
```

---

## STEP 10 — Commit and push

Print these instructions verbatim after writing the files:

---

### How to publish your paper page

#### In GitHub Codespaces (recommended)

1. In the left sidebar, click the **Source Control** icon (the branch icon, or press `Ctrl+Shift+G`)
2. You'll see all changed/new files listed under **Changes**
3. Hover over each file and click **+** to stage it (or click **+** next to "Changes" to stage all)
4. In the commit message box, type something like:
   `Add paper page: <Paper Title>`
5. Click **✓ Commit**
6. Click **Sync Changes** (the cloud icon with arrows) to push to GitHub

Your page will be live at:
**`https://chri-lab.github.io/papers/<slug>/`**
within a few minutes once GitHub Actions finishes building the site.

#### Working locally

```bash
git add _papers/<slug>.md assets/papers/<slug>/ _bibliography/papers.bib
# if new authors were added:
git add _data/authors.yml
git commit -m "Add paper page: <Paper Title>"
git push
```

---

> **Tip:** You can check build status at `https://github.com/CHRI-Lab/CHRI-Lab.github.io/actions`

---

## Notes

- Only include front matter fields for URLs that were actually provided — never leave placeholder `https://...` values.
- If `_layouts/paper.html` does not exist in the repo, warn the user and offer to create it.
- The page URL is `/papers/<slug>/` — this requires `_papers/` to be configured as a Jekyll collection in `_config.yml`. If it isn't, show the user what to add:
  ```yaml
  # In _config.yml, under collections:
  papers:
    output: true
    permalink: /papers/:slug/
  ```
- Keep the `.md` file clean — all styling is handled by `_layouts/paper.html`.

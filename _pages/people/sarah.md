---
title: "Sarah Schombs"
layout: personal
permalink: /people/sarah-schombs/
sitemap: false
excerpt: "Personal website of Sarah"
---
{%- assign data = site.data.people -%}
{%- assign member = data.sarah -%}

<div class="row">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="22%" style="float: left" />
  <h1>{{ member.name }}</h1>
  <i style="font-size:20px">{{ member.info }}</i><br>

  {% if member.website %}<a href="{{ member.website }}" target="_blank"><i class="fa fa-home fa-3x"></i></a> {% endif %}
  {% if member.email %}<a href="mailto:{{ member.email }}" target="_blank"><i class="fa fa-envelope-square fa-3x"></i></a> {% endif %}
  {% if member.scholar %} <a href="{{ member.scholar }}" target="_blank"><i class="ai ai-google-scholar-square ai-3x"></i></a> {% endif %}
  {% if member.cv %} <a href="{{ site.url }}{{ site.baseurl }}/files/{{ member.cv }}" target="_blank"><i class="ai ai-cv-square ai-3x"></i></a> {% endif %}
  {% if member.github %} <a href="{{ member.github }}" target="_blank"><i class="fa fa-github-square fa-3x"></i></a> {% endif %}
  {% if member.linkedin %} <a href="{{ member.linkedin }}" target="_blank"><i class="fa fa-linkedin-square fa-3x"></i></a> {% endif %}
  {% if member.twitter %} <a href="{{ member.twitter }}" target="_blank"><i class="fa fa-twitter-square fa-3x"></i></a> {% endif %}
  <!-- {% if member.researchgate %} <a href="{{ member.researchgate }}" target="_blank"><i class="ai ai-researchgate-square ai-3x"></i></a> {% endif %} -->
  <ul style="overflow: hidden">

  {% for education in member.education %}
	<li> {{ education }} </li>
  {% endfor %}

  </ul>
</div>

## Sketch

<p>
I am a second year Ph.D. student in ..... 
I am working with Wafa and Jorge. 
I am broadly interested in ..... 
Before joining XXXX, I received my B.S. and M.S. degree in XXXX.
</p>

## Work Experience

<p>
<em><strong>Research Assistant (Aug 2019 - Present)</strong></em><br>
XXXXX
</p>

<p>
<em><strong>Research Intern (May 2021 - Aug 2021)</strong></em><br>
XXXXX.<br>
Mentor: XXXXX<br>
</p>

## Publications

<div class="publications">

{% bibliography -f people/sarah%}

</div>

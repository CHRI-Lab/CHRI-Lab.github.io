---
title: "Chri Lab - Ulan"
layout: personal
permalink: /people/ulan/
sitemap: false
excerpt: "Personal webpage of Ulan"
---
{%- assign data = site.data.people -%}
{%- assign member = data.ulan -%}

<div class="row">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="22%" style="float: left" />
  <h1>{{ member.name }}</h1>
  <i style="font-size:20px">{{ member.info }}</i><br>

  {% if member.website %}<a href="{{ member.website }}" target="_blank"><i class="fa fa-home fa-3x"></i></a> {% endif %}
  {% if member.email %}<a href="mailto:{{ member.email }}" target="_blank"><i class="fa fa-envelope-square fa-3x"></i></a> {% endif %}
  {% if member.scholar %} <a href="{{ member.scholar }}" target="_blank"><i class="ai ai-google-scholar-square ai-3x"></i></a> {% endif %}
  <!-- {% if member.cv %} <a href="{{ site.url }}{{ site.baseurl }}/files/{{ member.cv }}" target="_blank"><i class="ai ai-cv-square ai-3x"></i></a> {% endif %}
  {% if member.github %} <a href="{{ member.github }}" target="_blank"><i class="fa fa-github-square fa-3x"></i></a> {% endif %} -->
  {% if member.linkedin %} <a href="{{ member.linkedin }}" target="_blank"><i class="fa fa-linkedin-square fa-3x"></i></a> {% endif %}
  {% if member.twitter %} <a href="{{ member.twitter }}" target="_blank"><i class="fa fa-twitter-square fa-3x"></i></a> {% endif %}
  <!-- {% if member.researchgate %} <a href="{{ member.researchgate }}" target="_blank"><i class="ai ai-researchgate-square ai-3x"></i></a> {% endif %} -->
  <ul style="overflow: hidden">

  {% for education in member.education %}
	<li> {{ education }} </li>
  {% endfor %}

  </ul>
</div>

## Biography

<p>
I received my MS XXXXX

My current research interest is XXXXX

If you have any questions, please contact me at [at]unimelb[dot]edu[dot]au
</p>


## Teaching Experience

<p>
<em>Teaching Assistant at Unimelb</em><br>
<b>Course:</b> XXXX, Fall 2022
</p>

## Work Experience

<p>
<em> Research Assistant (XXXX - XXXX)</em><br>
Department of XXXX, University of XXXXX.<br>
</p>

<p>
<em>Software Engineer Intern, XXXXX<br>
</p>

<p></p>
{% if member.awards %}
## Awards
{% endif %}

{% for award in member.awards %}
<ul style="overflow: hidden">
<li> {{ award }} </li>
</ul>
{% endfor %}

## Publications

<div class="publications">

{% bibliography -f people/ulan%}

</div>

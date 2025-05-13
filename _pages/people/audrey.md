---
title: "Chri Lab - Audrey"
layout: personal
permalink: /people/audrey/
sitemap: false
excerpt: "Personal webpage of Audrey"
---
{%- assign data = site.data.people -%}
{%- assign member = data.audrey -%}

<div class="row">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="22%" style="float: left" />
  <h1>{{ member.name }}</h1>
  <i style="font-size:20px">{{ member.info }}</i><br>

  {% if member.website %}<a href="{{ member.website }}" target="_blank"><i class="fa fa-home fa-3x"></i></a> {% endif %}
  {% if member.email %}<a href="mailto:{{ member.email }}" target="_blank"><i class="fa fa-envelope-square fa-3x"></i></a> {% endif %}
  {% if member.scholar %} <a href="{{ member.scholar }}" target="_blank"><i class="ai ai-google-scholar-square ai-3x"></i></a> {% endif %}
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

## Biography

<p>
I'm a Postdoctoral Research Fellow in the School of Computing and Information Systems, University of Melbourne, working under the supervision of Dr. Wafa Johal.  My research areas include assistive technology design, human-robot interaction, agent-based modeling, and control theory. Before joining the CHRI team, I received my joint-Ph.D. in Mechanical Engineering and Human-Robot Interaction from Tufts University, successfully defending my dissertation - "Human-Robot Interactions in Supervision of Robots by People With Blindness and Low Vision" - in May 2024.  Before that, I received my Bachelors in Mechanical Engineering from the University of New Hampshire in 2019, where I first discovered my love for control theory and advanced assistive technology design.  

I am espcially interested in the collaborations that occur in the interdisciplinary field of Human-Robot Interaction - in particular, observing how someone's "home discipline" or personal background influences their approach to research and design in this space.  When specifically talking about assistive design of complex technological systems, I am interested in optimizing the inclusion of people with disabilities in the design process in a way that increases the adoption and acceptance of new technologies and educates new designers on inclusivity without contributing to disability advocacy fatigue.  

<br/>

Contact me: audrey[dot]balaska[at]unimelb[dot]edu[dot]au
<br/>
[Google Scholar](https://scholar.google.com/citations?user=DyoiyokAAAAJ&hl=en)
<br/>
[LinkedIn](https://www.linkedin.com/in/audrey-balaska-75a095135/)
<br/>
[Personal Webpage](https://sites.google.com/view/audrey-balaska-engineering/home?authuser=0)

## Publications

<div class="publications">

{% bibliography -f people/audrey%}

</div>

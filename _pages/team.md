---
title: "CHRI Lab - Team"
layout: team
excerpt: "CHRI Lab: Team members"
sitemap: false
permalink: /people/
---

<!-- # Group Members -->
<!-- **We are  looking for new PhD students, Postdocs, and Master students to join the team** [(see openings)]({{ site.url }}{{ site.baseurl }}/vacancies) **!** -->

Jump to [Faculty](#faculty), [Current Students](#current-students), [Visitor](#postdoc), [Alumni](#alumni).

<!----------------------------------------------------------------------------------------------------------------------------------------->
## Faculty
{% assign number_printed = 0 %}
{% assign fac_array = site.data.team.faculty | sort: "lastname" %}
{% for member in fac_array %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">

  {% if member.social.website %}

  {% if member.photo %}
  <a target="blank" href="{{ member.social.website }}"><img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" /></a>
  {% endif %}
  <h4><a target="blank" href="{{ member.social.website }}">{{ member.name }}</a></h4>
  {% else %}

  {% if member.photo %}
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  {% endif %}
  <h4>{{ member.name }}</h4>

  {% endif %}

  {%- include socialmedia.html -%}
  <i>{{ member.info }}</i> <!--<br>email: <{{ member.email }}></i> -->
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

<!----------------------------------------------------------------------------------------------------------------------------------------->
## Current Students
{% assign number_printed = 0 %}
{% assign stud_array = site.data.team.current-students | sort: "lastname" %}
<!-- Inspect a variable in liquid -->
<!-- {{ stud_array[0] | inspect }} -->

{% for member in stud_array%}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">

  {% if member.social.website %}

  {% if member.photo %}
  <a target="blank" href="{{ member.social.website }}"><img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" /></a>
  {% endif %}
  <h4><a target="blank" href="{{ member.social.website }}">{{ member.name }}</a></h4>
  {% else %}

  {% if member.photo %}
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  {% endif %}
  <h4>{{ member.name }}</h4>
  
  {% endif %}
  
  {%- include socialmedia.html -%}
  <i>{{ member.info }}</i><!--<br>email: <{{ member.email }}></i> -->
  {% if member.advisor.size == 1 %}
  Advisor: <i>{{ member.advisor }}</i>
  {% endif %}

  {% if member.advisor.size == 2 %} <!-- Generally a student is advised by max of 2 professors -->
  Advisor: <i>{{ member.advisor[0] }}</i>, <i>{{ member.advisor[1] }}</i>
  {% endif %}

  {% if member.advisor.size == 3 %} <!-- Generally a student is advised by max of 2 professors -->
  Advisor: <i>{{ member.advisor[0] }}</i>, <i>{{ member.advisor[1] }}</i>, <i>{{ member.advisor[2] }}</i>
  {% endif %}

</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

<!----------------------------------------------------------------------------------------------------------------------------------------->
{% if site.data.team.other-students.size > 0 %}
## Master and Bachelor Students
{% endif %}
{% assign number_printed = 0 %}
{% for member in site.data.team.other-students %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <h4>{{ member.name }}</h4>
  <i>{{ member.info }} <!-- <br>email: <{{ member.email }}></i> -->
  <ul style="overflow: hidden">

  <!-- {% for education in member.education %}
    <li>{{ education }}</li>
  {% endfor %} -->

  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

<!----------------------------------------------------------------------------------------------------------------------------------------->
{% if site.data.team.postdoc.size > 0 %}
## Postdoc
{% endif %}

{% assign number_printed = 0 %}
{% for member in site.data.team.postdoc%}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">

  {% if member.social.website %}

  {% if member.photo %}
  <a target="blank" href="{{ member.social.website }}"><img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" /></a>
  {% endif %}
  <h4><a target="blank" href="{{ member.social.website }}">{{ member.name }}</a></h4>
  {% else %}

  {% if member.photo %}
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  {% endif %}
  <h4>{{ member.name }}</h4>

  {% endif %}

  {%- include socialmedia.html -%}
  <i>{{ member.info }}</i> <!--<br>email: <{{ member.email }}></i> -->

  {% if member.from %}
  <i>{{ member.from }}</i>
  {% endif %}
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

<!----------------------------------------------------------------------------------------------------------------------------------------->
## Alumni
<div class="row">
{% for member in site.data.alumni %}
<div class="col-sm-6 clearfix">
  <h4>{{ member.name }}</h4>
  <i> {{ member.role }}</i>
</div>
{% endfor %}
</div>

<!----------------------------------------------------------------------------------------------------------------------------------------->
<!-- ## Former visitors, BSc/ MSc students

<div class="row">
<div class="col-sm-4 clearfix">
<h4>Visitors</h4>
{% for member in site.data.alumni_visitors %}
{{ member.name }}
{% endfor %}
</div>

<div class="col-sm-4 clearfix">
<h4>Master students</h4>
{% for member in site.data.alumni_msc %}
{{ member.name }}
{% endfor %}
</div>

<div class="col-sm-4 clearfix">
<h4>Bachelor Students</h4>
{% for member in site.data.alumni_bsc %}
{{ member.name }}
{% endfor %}
</div>

</div> -->

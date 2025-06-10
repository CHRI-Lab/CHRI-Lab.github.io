---
title: "News"
layout: textlay
excerpt: "News: CHRI Lab at Unimelb."
sitemap: false
permalink: /allnews.html
---

# News

<div class="well">
{% for article in site.data.news %}
  <div class="news-item">
    {%- if article.img %}
      <img src="{{ site.url }}{{ site.baseurl }}/images/news/{{ article.img }}" class="img-responsive" width="22%" style="float: left; margin-right: 10px;" /> 
    {%- endif %}
    <p>{{ article.date }}<br/>
    {{ article.headline }}<br/>
    </p>
    <hr> <!-- Adds a line break between entries -->
  </div>
{% endfor %}
</div>

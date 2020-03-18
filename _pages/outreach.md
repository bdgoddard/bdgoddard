---
title: "Ben Goddard - Outreach"
layout: gridlay
excerpt: "Ben Goddard -- Outreach"
permalink: /outreach/
---

# Outreach and Public Engagement

I believe that communicating the excitement and beauty of mathematics to a wide audience is an important aspect of my work as researcher. This page highlights some of the things that I (along with many talented and enthusiastic collaborators) do in these areas.

**Current opportunity:**  Along with Francesca Iezzi and Zoe Wyatt, I have a small University of Edinburgh Principal's Teaching Award Scheme grant for <a href="https://www.ed.ac.uk/institute-academic-development/learning-teaching/funding/funding/previous-projects/year/march-2019/widening-participation-maths-circles">Widening participation in Maths Circles</a>.  In particular, this includes money to help people run Maths Circles in their schools or local communities.  Please get in touch if you're interested in this!

## Highlights
{% assign number_printed = 0 %}
{% for publi in site.data.outreach %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if publi.highlight == 1 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
 <div class="well">
  <pubtit>{{ publi.title }}</pubtit>
<img src="{{ site.url }}{{ site.baseurl }}/images/outreach/{{ publi.image }}" class="img-responsive" width="33%" style="float: left" />
  <p>{{ publi.description }}</p>
  <p><em>Jointly organised with {{ publi.collaborators }}</em></p>
  <p>Find out more about <a href="{{ publi.link.url }}">{{ publi.title }}</a></p>
 </div>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endif %}
{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}
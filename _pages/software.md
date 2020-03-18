---
title: "Ben Goddard - Software"
layout: softwarelay
excerpt: "Ben Goddard -- Software"
permalink: /software/
---

# Software

Below you can find some information on, and links to, scientific software that I have been involved in developing. They are primarily written in Matlab.

{% assign number_printed = 0 %}

{% for publi in site.data.software %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">

<h2>{{ publi.title }}</h2>

<img src="{{ site.url }}{{ site.baseurl }}/images/software/{{ publi.image }}" class="img-responsive" width="33%" style="float: right" />

  <p>{{ publi.description }}</p>

  {% if publi.collaborators.is_collab == 1%}

  <p>{{ publi.title }} is developed with {{ publi.collaborators.collabs }} and is available open source from  <a href="{{ publi.link.url }}">{{ publi.link.display }}</a>.</p>

  {% else %}

  <p>{{ publi.title }} is available open source from  <a href="{{ publi.link.url }}">{{ publi.link.display }}</a>.</p>
 
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
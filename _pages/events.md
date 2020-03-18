---
title: "Ben Goddard - Events"
layout: gridlay
excerpt: "Ben Goddard -- Events."
sitemap: false
permalink: /events/
---


# Events

## Recent and Upcoming

(For a full list see [below](#full-list)).

{% assign number_printed = 0 %}
{% for event in site.data.events %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if event.highlight == 1 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">

  <div class="well">
  <pubtit>{{ event.title }}</pubtit>

  {{ event.location }}, {{ event.dates }}
  
  {% if event.number_coorg == 1 %}
  Co-organised with 
  <a href="{{ event.coorg1_url }}">{{ event.coorg1 }}</a> ({{ event.coorg1_inst }}).
  {% endif %}
  {% if event.number_coorg == 2 %}
  Co-organised with 
  <a href="{{ event.coorg1_url }}">{{ event.coorg1 }}</a> ({{ event.coorg1_inst }})
  and 
  <a href="{{ event.coorg2_url }}">{{ event.coorg2 }}</a> ({{ event.coorg2_inst }}).
  {% endif %}
  {% if event.number_coorg == 3 %}
  Co-organised with 
  <a href="{{ event.coorg1_url }}">{{ event.coorg1 }}</a> ({{ event.coorg1_inst }}),
  <a href="{{ event.coorg2_url }}">{{ event.coorg2 }}</a> ({{ event.coorg2_inst }}),
  and 
  <a href="{{ event.coorg3_url }}">{{ event.coorg3 }}</a> ({{ event.coorg3_inst }}).  
  {% endif %}
  {% if event.number_coorg == 4 %}
  Co-organised with 
  <a href="{{ event.coorg1_url }}">{{ event.coorg1 }}</a> ({{ event.coorg1_inst }}),
  <a href="{{ event.coorg2_url }}">{{ event.coorg2 }}</a> ({{ event.coorg2_inst }}),
  <a href="{{ event.coorg3_url }}">{{ event.coorg3 }}</a> ({{ event.coorg3_inst }}),
  and 
  <a href="{{ event.coorg4_url }}">{{ event.coorg4 }}</a> ({{ event.coorg4_inst }}).    
  {% endif %}

  {% if event.link.is_link == 1 %}
  Please see the <a href="{{ event.link.url }}">event website</a> for more 
information.
  {% else %}
  More details will be available in due course.
  {% endif %}

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


## Full List

{% for event in site.data.events %}

{% if event.link.is_link == 1 %} 
<a href="{{ event.link.url }}"><pubtit>{{ event.title }}</pubtit></a>
<br/>
{{ event.location }}, {{ event.dates }}
  {% else %}
<pubtit>{{ event.title }}</pubtit>
{{ event.location }}, {{ event.dates }}
  {% endif %}
  

  {% if event.number_coorg == 1 %}
  Co-organised with 
  <a href="{{ event.coorg1_url }}">{{ event.coorg1 }}</a> ({{ event.coorg1_inst }}).
  {% endif %}
  {% if event.number_coorg == 2 %}
  Co-organised with 
  <a href="{{ event.coorg1_url }}">{{ event.coorg1 }}</a> ({{ event.coorg1_inst }})
  and 
  <a href="{{ event.coorg2_url }}">{{ event.coorg2 }}</a> ({{ event.coorg2_inst }}).
  {% endif %}
  {% if event.number_coorg == 3 %}
  Co-organised with 
  <a href="{{ event.coorg1_url }}">{{ event.coorg1 }}</a> ({{ event.coorg1_inst }}),
  <a href="{{ event.coorg2_url }}">{{ event.coorg2 }}</a> ({{ event.coorg2_inst }}),
  and 
  <a href="{{ event.coorg3_url }}">{{ event.coorg3 }}</a> ({{ event.coorg3_inst }}).{% endif %}
  {% if event.number_coorg == 4 %}
  Co-organised with 
  <a href="{{ event.coorg1_url }}">{{ event.coorg1 }}</a> ({{ event.coorg1_inst }}),
  <a href="{{ event.coorg2_url }}">{{ event.coorg2 }}</a> ({{ event.coorg2_inst }}),
  <a href="{{ event.coorg3_url }}">{{ event.coorg3 }}</a> ({{ event.coorg3_inst }}),
  and 
  <a href="{{ event.coorg4_url }}">{{ event.coorg4 }}</a> ({{ event.coorg4_inst }}).{% endif %}

<p> &nbsp; </p>

{% endfor %}


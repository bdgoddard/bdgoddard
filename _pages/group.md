---
title: "Ben Goddard - Group"
layout: grouplay
excerpt: "Ben Goddard: Group members"
sitemap: false
permalink: /group/
---

# Group Members

## PhD Students
{% assign number_printed = 0 %}
{% for member in site.data.team_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/group/{{ member.photo }}" class="img-responsive" width="25%" style="float: left"/>
  <h4>{{ member.name }}</h4>
  <i>{{ member.info.position }} since {{ member.info.date }} 
  <br>email: <{{ member.email }}></i>
  <ul style="overflow: hidden">
  {% if member.cdt.in_cdt == 1 %}
    <li> Member of <a href="{{ member.cdt.url }}">{{ member.cdt.abbr }}</a>, the {{ member.cdt.name }}  </li>
  {% endif %}

  {% if member.cosup.has_cosup == 1 %}
    <li> Co-supervised with <a href="{{ member.cosup.url }}">{{ member.cosup.name }}</a>,
         {{ member.cosup.affiliation }}
    </li>
  {% endif %}
  </ul>
  <p>
  {{ member.project }}
  </p></div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}



## Alumni

{% assign number_printed = 0 %}
{% for member in site.data.alumni_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/group/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4>{{ member.name }}</h4>
  <i>{{ member.info.position }}, {{ member.info.date }} 
  <p>{{ member.project }}</p>
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

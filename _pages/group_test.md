---
title: "Ben Goddard - Group"
layout: grouplay
excerpt: "Ben Goddard: Group members"
sitemap: false
permalink: /group_test/
---

# Group Members

{% for member in site.data.team_members %}
  <div>
  <img src="{{ site.url }}{{ site.baseurl }}/images/{{ member.photo }}" class="img-responsive" width="25%" style="float: left"/>
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
  </p>
  </div>

  <div class="row">
  </div>


{% endfor %}


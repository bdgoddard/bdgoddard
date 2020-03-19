---
title: "Ben Goddard - Beers"
layout: textlay
excerpt: "Ben Goddard -- Beers."
sitemap: false
permalink: /beers/
---

# Beers

{% assign total_beers = 0 %}

{% for beer in site.data.beers %}
  {% assign total_beers = total_beers | plus: 1 %}
{% endfor %}

I've finally become fed up with not being able to remember whether I've drunk a particular beer or not, and perhaps more so with remembering I've tried it, but not remembering if it was brilliant or  awful.  Hence I've decided to make a list. Below are the {{ total_beers }} beers currently in my database.

The rating is out of five, corresponding to:
* <span class="beers_rating1"> &#9733; </span> Pretty much undrinkable, I didn't (want) to finish it.
* <span class="beers_rating2"> &#9733;&#9733; </span> Poor, I drank that one, but wouldn't order another.
* <span class="beers_rating3"> &#9733;&#9733;&#9733; </span> A perfectly decent beer, not outstanding, but would happily drink again.
* <span class="beers_rating4"> &#9733;&#9733;&#9733;&#9733; </span> Very good, would order in preference to most other beers.
* <span class="beers_rating5"> &#9733;&#9733;&#9733;&#9733;&#9733; </span> A truly outstanding beer, get hold of wherever possible. Don't expect too many of these!

If you'd like to see the highlights, take a look at my [wishlist](#wishlist).

The format is:
  
  <span class="beers_brewery">Brewery</span>

  <span>
  Beer 1 &#9733;'s/&#9733;&#9733;&#9733;&#9733;&#9733;
  </span>
  <span class="beers_country">(Country)</span>
  <span class="beers_abv">ABV%</span>
  <span class="beers_style">Style</span>
  <span class="beers_bcx">(bottle/can/cask)</span>
  <br />
  <span class="beers_review">Review</span>

  <span>
  Beer 2 &#9733;'s/&#9733;&#9733;&#9733;&#9733;&#9733;
  </span>
  <span class="beers_country">(Country)</span>
  <span class="beers_abv">ABV%</span>
  <span class="beers_style">Style</span>
  <span class="beers_bcx">(bottle/can/cask)</span>
  <br />
  <span class="beers_review">Review</span>

  &vellip;


## Full List

{% for beer in site.data.beers %}

{% assign this_brewery = beer.Brewery %}

{% if this_brewery != old_brewery %}
  <span class="beers_brewery">{{ beer.Brewery }}</span>
  <span class="beers_country">({{ beer.Country }})</span>
{% endif %}

{% if beer.BCX == "B" %}
  {% assign BCX = "bottle" %}
{% endif %}
{% if beer.BCX == "C" %}
  {% assign BCX = "cask" %}
{% endif %}
{% if beer.BCX == "X" %}
  {% assign BCX = "can" %}
{% endif %}

{% if beer.Rating == '1' %}
  <span class="beers_rating1">
  {{ beer.Beer }} &#9733;
  </span>
  <span class="beers_abv">{{ beer.ABV }}%</span>
  <span class="beers_style">{{ beer.Style }}</span>
  <span class="beers_bcx">({{ BCX }})</span>
  <br />
  <span class="beers_review">{{ beer.Review }}</span>
{% endif %}
{% if beer.Rating == '2' %}
  <span class="beers_rating2">
  {{ beer.Beer }} &#9733;&#9733;
  </span>
  <span class="beers_abv">{{ beer.ABV }}%</span>
  <span class="beers_style">{{ beer.Style }}</span>
  <span class="beers_bcx">({{ BCX }})</span>
  <br />
  <span class="beers_review">{{ beer.Review }}</span>
{% endif %}
{% if beer.Rating == '3' %}
  <span class="beers_rating3">
  {{ beer.Beer }} &#9733;&#9733;&#9733;
  </span>
  <span class="beers_abv">{{ beer.ABV }}%</span>
  <span class="beers_style">{{ beer.Style }}</span>
  <span class="beers_bcx">({{ BCX }})</span>
  <br />
  <span class="beers_review">{{ beer.Review }}</span>
{% endif %}
{% if beer.Rating == '4' %}
  <span class="beers_rating4">
  {{ beer.Beer }} &#9733;&#9733;&#9733;&#9733;
  </span>
  <span class="beers_abv">{{ beer.ABV }}%</span>
  <span class="beers_style">{{ beer.Style }}</span>
  <span class="beers_bcx">({{ BCX }})</span>
  <br />
  <span class="beers_review">{{ beer.Review }}</span>
{% endif %}

{% if beer.Rating == '5' %}
  <span class="beers_rating5">
  {{ beer.Beer }} &#9733;&#9733;&#9733;&#9733;&#9733;
  </span>
  <span class="beers_abv">{{ beer.ABV }}%</span>
  <span class="beers_style">{{ beer.Style }}</span>
  <span class="beers_bcx">({{ BCX }})</span>
  <br />
  <span class="beers_review">{{ beer.Review }}</span>
{% endif %}

{% assign old_brewery = beer.Brewery %}

{% endfor %}


## Wishlist

If you're thinking about buying me some beer then: (a) you're amazing, thank you!; (b) you could do a lot worse than choosing some of the beers in this section.

{% for beer in site.data.beers %}

{% if beer.Rating == '5' %}

{% if beer.BCX == "B" %}
  {% assign BCX = "bottle" %}
{% endif %}
{% if beer.BCX == "C" %}
  {% assign BCX = "cask" %}
{% endif %}
{% if beer.BCX == "X" %}
  {% assign BCX = "can" %}
{% endif %}

  <span class="beers_rating5">
  {{ beer.Brewery }} - {{ beer.Beer }} &#9733;&#9733;&#9733;&#9733;&#9733;
  </span>
  <span class="beers_country">({{ beer.Country }})</span>
  <span class="beers_abv">{{ beer.ABV }}%</span>
  <span class="beers_style">{{ beer.Style }}</span>
  <span class="beers_bcx">({{ BCX }})</span>
  <br />
  <span class="beers_review">{{ beer.Review }}</span>

{% endif %}

{% endfor %}


---
layout: page
title: Homepage
---
<div class="container">
 {% assign num = 0 %}
  {% for post in site.posts %}
      {% assign rownum = num | modulo:3 %}
      {% if rownum == 0 %}
      </div>
      <div class="row text-center">
      {% endif %}
          <div class="col-lg-4 col-lg-offset-0 col-md-4 col-md-offset-0 col-sm-4 col-sm-offset-0 col-xs-10 col-xs-offset-1 post-block">
              <a href="{{ post.url | prepend: site.baseurl }}">
              <div class="post-card">
                  <img src="./assets/images/{{ post.image }}"/>
                  <!-- <div class="mdl-card__title"> -->
                  <h2>{{ post.title }}</h2>
                  <!-- </div> -->

                  <!-- <div class="mdl-card__supporting-text"> -->
                  {{ post.description | truncate:5 }} Click to see more info.
                  <!-- </div> -->
                  <!-- <div class="post-card__fade"></div> -->
              </div>
              </a>
          </div>
      {% assign num = num | plus: 1 %}
  {% endfor %}
      </div>
</div>
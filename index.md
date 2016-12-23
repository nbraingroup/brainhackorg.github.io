---
layout: page
title: Homepage
---

<div class="container">
 {% assign num = 0 %}
  {% for post in site.posts %}
      {% assign rownum = num | modulo:3 %}
      {% if rownum == 0 %}
      <div class="row text-center">
      {% endif %}
          <div class="col-lg-4 col-lg-offset-0 col-md-4 col-md-offset-0 col-sm-4 col-sm-offset-0 col-xs-10 col-xs-offset-1 post-block">
              <a href="{{ post.url | prepend: site.baseurl }}">
              <div class="post-card">
                  <img src="./assets/images/{{ post.image }}"/>
                  <h3>{{ post.title }}</h3>

                  <div class="post-card__fade">
                    {{ post.description | truncate:150 }}
                  </div>

              </div>
              </a>
          </div>
      {% if rownum == 2 %}
      </div>
      {% endif %}
      {% assign num = num | plus: 1 %}
  {% endfor %}
  {% if rownum != 2 %}
      </div>
  {% endif %}
</div>

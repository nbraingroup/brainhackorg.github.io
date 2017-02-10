---
layout: page
title: Homepage
---

<div class="grid">
 {% assign num = 0 %}
  {% for post in site.posts %}

      {% if post.big == 1 %}
          <div class="entry big">
      {% else %}
          <div class="entry small">
      {% endif %}

  			<div class="entry-thumbnail">
    				<a href="{{ post.url | prepend: site.baseurl }}">
                <img src="./assets/images/{{ post.image }}"  alt="{{ post.title }}" title="{{ post.title }}" /><span class="overlay"></span>
    				</a>

            {% if post.category %}
    				<div class="category"><ul class="post-categories">
    	          <li><a href="http://brainhack.org/categories/brainhack-global-2017/" rel="category tag">{{ post.category }}</a></li></ul>
            </div> <!-- end .category -->
            {% endif %}

    				<span class="month">Jan<span class="date">16</span></span>
  			</div><!-- end .entry_thumbnail -->

  			<h2 class="title"><a href="{{ post.url | prepend: site.baseurl }}">
        {% if post.big == 1 %}
            {{ post.title | truncate:45 }}
        {% else %}
            {{ post.title | truncate:20 }}
        {% endif %}
        </a></h2>
  			<p class="postinfo">posted by <a href="http://brainhack.org/author/cameron-craddock/" title="Posts by cameron.craddock" rel="author">cameron.craddock</a></p>

  			<div class="entry-content">
  			    <div class="bottom-bg">
  					    <div class="excerpt">        
                    <p>
                        {% if post.big == 1 %}
                            {{ post.description | truncate:150 }}
                        {% else %}
                            {{ post.description | truncate:75 }}
                        {% endif %}
                    </p>
  						      <div class="textright">
  							        <a href="{{ post.url | prepend: site.baseurl }}" class="readmore"><span>&raquo;</span>&raquo;</a>
  						      </div><!-- end .textright -->
  					    </div><!-- end .excerpt -->
  				  </div><!-- end .bottom-bg -->
  			</div><!-- end .entry-content -->

      </div><!-- end .entry -->

      {% assign num = num | plus: 1 %}
  {% endfor %}
</div>

<script type="text/javascript">
  jQuery('.grid').masonry({
    itemSelector: '.entry',
    columnWidth: 122,
    animate: true});
    </script>

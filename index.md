---
layout: main-page
title: Homepage
---


<!-- <p class="whitetext">Enter a search term below to filter the projects and resources:<p>
<p><input type="text" class="quicksearch" placeholder="Search" /></p> -->

<div class="grid">
 {% assign num = 0 %}
  {% for post in site.posts %}

      {% if post.big == 1 %}
          <div class="entry entry-big">
      {% else %}
          <div class="entry entry-small">
      {% endif %}

  			<div class="entry-thumbnail">
            {% if post.project_url %}
    				   <a href="{{ post.project_url }}">
            {% else %}
               <a href="{{ post.url | prepend: site.baseurl }}">
            {% endif %}
                <img src="./assets/images/{{ post.image }}"  alt="{{ post.title }}" title="{{ post.title }}" /><span class="overlay"></span>
    				</a>

            {% if post.project_categories %}
          				<div class="category">
                    <ul class="post-categories">
                        <li>
                            {{ post.project_categories }}
                        </li>
                    </ul>
                  </div> <!-- end .category -->
            {% endif %}

  			</div><!-- end .entry_thumbnail -->

  			<h2 class="title featured"><a href="{{ post.url | prepend: site.baseurl }}">
        {% if post.big == 1 %}
            {{ post.title | truncate:45 }}
        {% else %}
            {{ post.title | truncate:25 }}
        {% endif %}
        </a>
        </h2>

  			<div class="entry-content">
  			    <div class="bottom-bg">
  					    <div class="excerpt">        
                    <p>
                        {% if post.big == 1 %}
                            {{ post.description | truncate:150 }}
                        {% else %}
                            {{ post.description | truncate:60 }}
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
// quick search regex
var qsRegex;
// init Isotope
var $grid = jQuery('.grid').isotope({
  itemSelector: '.entry',
  layoutMode: 'masonry',
  masonry: {
    columnWidth: 236,
    gutter: 8
  },
  filter: function() {
    return qsRegex ? jQuery(this).text().match( qsRegex ) : true;
  }
});
// use value of search field to filter
var $quicksearch = jQuery('.quicksearch').keyup( debounce( function() {
  qsRegex = new RegExp( $quicksearch.val(), 'gi' );
  $grid.isotope();
}, 200 ) );
// debounce so filtering doesn't happen every millisecond
function debounce( fn, threshold ) {
  var timeout;
  return function debounced() {
    if ( timeout ) {
      clearTimeout( timeout );
    }
    function delayed() {
      fn();
      timeout = null;
    }
    timeout = setTimeout( delayed, threshold || 100 );
  }
}

</script>

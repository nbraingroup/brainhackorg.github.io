---
layout: page
title: video-lectures
---



# Brainhack Video Lectures and Tutorials
Talks and hands-on tutorials from previous Brainhack events are available on YouTube using the following play lists:

- [Brainhack Global 2017](https://www.youtube.com/playlist?list=PLNt4AJV1JZbfcRh9gEdHu47edoQE76bp5)
- [Neurohackweek 2016](https://www.youtube.com/playlist?list=PLEdFhTRBFLObkatJOX9wp3BCueH4wNSl7)
- [Brainhacking 101 (tutorials from AMX)](https://www.youtube.com/playlist?list=PLNt4AJV1JZbfq0vdD4vcITV7x3OqGxLKp)
- [Brainhack Vienna 2016](https://www.youtube.com/playlist?list=PLNt4AJV1JZbcCs84XEbN9XdXBXN9U-kyT)
- [Brainhack AMX 2015](https://www.youtube.com/playlist?list=PLNt4AJV1JZbe8wO4vG9cOkFiSazJGuHjw)
- [Brainhack EDT 2014](https://www.youtube.com/playlist?list=PLNt4AJV1JZbfcRh9gEdHu47edoQE76bp5)

<!-- <script src="https://hackpad.com/ZP53JJlhGyJ.js?format=html"></script> -->

<input type="text" class="quicksearch" placeholder="SEARCH VIDEOS" />

<div class="grid">
 {% assign num = 0 %}
  {% for post in site.posts %}
    {% if post.video-url %}
      <div class="entry entry-video">
  			<div class="entry-thumbnail">            
    				<a href="https://www.youtube.com/watch?v={{ post.video-url }}">            
              <img src="http://img.youtube.com/vi/{{ post.video-url }}/0.jpg" height="218" width="297" alt="thumbnail" />
              <span class="overlay"></span>
    				</a>
            {% if post.video_categories %}
          				<div class="category">
                    <ul class="post-categories">
                        <li>
                            {{ post.video_categories }}
                        </li>
                    </ul>
                  </div> <!-- end .category -->
            {% endif %}
  			</div><!-- end .entry_thumbnail -->

  			<h2 class="title featured">
        <a href="https://www.youtube.com/watch?v={{ post.video-url }}">      
            {{ post.title | truncate:30 }}        
        </a>
        </h2>
  			<div class="entry-content">
  			    <div class="bottom-bg">
  					    <div class="excerpt">        
                    <p>                        
                      {{ post.description | truncate:100 }}                        
                    </p>
  						      <div class="textright">
  							        <a href="https://www.youtube.com/watch?v={{ post.video-url }}" class="readmore"><span>&raquo;</span>&raquo;</a>
  						      </div><!-- end .textright -->
  					    </div><!-- end .excerpt -->
  				  </div><!-- end .bottom-bg -->
  			</div><!-- end .entry-content -->

      </div><!-- end .entry -->

      {% assign num = num | plus: 1 %}
    {% endif %}
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

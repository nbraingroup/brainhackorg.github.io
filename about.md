---
layout: page
title: About
---

<div class="container" id="pubtable">
  <header>
          <h1>About</h1>
          <h2>Information about the brainhack organization and hosting a brainhack</h2>
          <p>Answering the next generation of open questions in neuroscience will require very large data sets and complex analytical methods. The purpose of Brainhack is to bridge the data science and neuroscience research communities by bringing them together to collaborate on a multitude of projects. Brainhack is a unique conference that convenes researchers from across the globe and a myriad of disciplines to work together on innovative projects related to neuroscience. Year after year, global Brainhack events have brought together researchers to participate in open collaboration, and regional Brainhack events keep the momentum going throughout the year.

          These collaborative workshops combine elements of Hackathons and Unconferences, with a variety of educational activities, to accelerate the adaptation of data science and computational methods in Neuroscience. Much of the conference is allocated to open working time during which attendees are encouraged to work together in interdisciplinary teams on projects that utilize computational techniques to solve problems in neuroscience. Periodic unconference sessions provide an opportunity for attendees to share their expertise on topics that become relevant through the course of the event. In parallel to these activities, an educational track provide hands-on tutorials on relevant tools such as python, github, cloud computing, and innovative statistical methods.</p>

          <h2>Who is Brainhack.org?</h2>
          <h3>Board</h3>
          <p>The board is currently made up of the founders of Brainhack. The board meets quarterly to plan future Brainhack events and discuss other business.</p>
          <ul>
          <li>Cameron Craddock, director</li>
          <li>Daniel Margulies</li>
          <li>Pierre Bellec</li>
          <li>Nolan Nichols</li>
          <li>Tal Yarkoni</li>
          </ul>

          <h3>Current Members</h3>
          <p>The Brainhack organization is composed of individuals that have previously hosted brainhack events and those that plan to host events in the future. Members include:</p>
          <Insert table with members>

          <h3>How to Become a Member</h3>
          <p>If you would like to join the organization please contact a board member or email info@brainhack.org.</p>

          <h2>Brainhack Publications</h2>
          <h3>Brainhack Proceedings</h3>
          <p>We publish short reports describing projects completed at Brainhack events that occured during the year in a Annual Brainhack Proceedings.</p>

          <h3>Brainhack Thematic Series</h3>
          <p>We invite full length publications that describe projects worked on as part of Brainhack or that are consistent with the Brainhack Proceedings to be published in the GigaScience Brainhack Thematic Series.</p>

          <h3>Brainhack Outcomes</h3>
          <p>Below is a brief list of some of the projects that have been created at Brainhack events. More detailed information can be found in the <a href="https://gigascience.biomedcentral.com/articles/10.1186/s13742-016-0147-0">Brainhack Proceedings</a> and in our recent publication on <a href="https://gigascience.biomedcentral.com/articles/10.1186/s13742-016-0121-x">Brainhack</a>.</p>
          <div id="projectgrid" class="col-md-12">
          <table>
            <tr>
              <th>Project</th>
              <th>Brainhack Event</th>
            </tr>
            <tr>
              <td>A child psychiatrist and a 3D video artist initiated a collaboration to develop a movie to be shown to participants during resting-state fMRI scans to reduce head motion in hyperkinetic populations</td>
              <td>2012 Brainhack &amp; Unconference (Leipzig)</td>
            </tr>
            <tr>
              <td>The ABIDE Preprocessing Initiative is an ongoing project to share preprocessed versions of the Autism Brain Imaging Data Exchange (ABIDE) dataset</td>
              <td>2012 Brainhack &amp; Unconference (Leipzig)</td>
            </tr>
            <tr>
              <td>An analysis to identify differences in cortical thickness and structural covariance between individuals with autism spectrum disorder and neurotypical controls</td>
              <td>2012 Brainhack &amp; Unconference (Leipzig)</td>
            </tr>
            <tr>
              <td>A project team amassed a dataset of 14,781 structural MRI scans to estimate the distribution of brain sizes across individuals for optimizing scan acquisition parameters</td>
              <td>Brainhack 2013 Paris</td>
            </tr>
            <tr>
              <td>The development team of LORIS, an open source database system for neuroimaging and phenotypic data, have repeatedly used Brainhack as an opportunity to meet and collaborate on new features</td>
              <td></td>
            </tr>
            <tr>
              <td>An early version of the Daydreaming app, an Android application for real-time assessment of usersŐ mind-wandering</td>
              <td>Brainhack 2013 Paris</td>
            </tr>
            <tr>
              <td>The Clubs of Science project has built a web-based visualization of the social web underlying neuroimaging research</td>
              <td>Brainhack Montreal 2015</td>
            </tr>
            <tr>
              <td>The linkRbrain tool for integrating and querying neuroimaging data with activation peaks from the literature and gene expression data was partially developed and first tested</td>
              <td>Brainhack 2013 Paris</td>
            </tr>
          </table>
          </div>

  <section id="main_content">
    <noscript>
    <!-- bibtex source hidden by default, show it if JS disabled -->
      <style>
        #bibtex { display: block;}
      </style>
    </noscript>

    <table id="pubTable" class="display"></table>

    <script type="text/javascript" src="/javascripts/bib-list.js"></script>

    <script type="text/javascript">
      $(document).ready(function() {
        bibtexify("2016_brainhack_proceedings.bib", "pubTable", {'visualization':false, 'tweet': 'brainhackorg'});
        });
    </script>
  </section>
  <footer>  </footer>

---
layout: post
title:  "Predicting RTMS Outcomes"
date:   2017-1-11 10:21:06
project_categories: Brainhack EDT Toronto Challenge
image: toronto_rtms_challenge-466x180.png
big: 1
description: Identify ≥85% reliable predictors of outcome for rTMS in depression, using resting-state fMRI
---
## Summary
### The Challenge  
Identify ≥85% reliable predictors of outcome for rTMS in depression, using resting-state fMRI  
Thanks to more than 25 years of neuroimaging studies, we now have detailed information about what major depression looks like in the brain – at least, at the group level…  
### The problem  
Our patients present themselves for treatment as individuals, not groups! And as of 2014, we still don’t have any reliable way of using neuroimaging to help us select the right treatment for each individual patient in the clinic.
Enter machine learning. Over the last few years, automated classification algorithms have made substantial progress on the problem of classifying individuals based on fMRI scans. Accuracies over 90% have recently been achieved in distinguishing healthy controls from depression patients, bipolar from schizophrenia patients, younger from older individuals, and sleeping from waking brains.  
Could we use these same techniques to predict whether individual patients will or will not respond to a given treatment? It’s recently been accomplished for [electroconvulsive therapy (ECT)](http://www.ncbi.nlm.nih.gov/pubmed/25092248), using resting-state functional MRI. So perhaps it’s not too far-fetched to propose doing the same thing for a more targeted brain stimulation treatment: repetitive transcranial magnetic stimulation (rTMS).  
### Here’s what we have to work with:  
The MRI-Guided rTMS Clinic at the Toronto Western Hospital has collected 10 minute resting-state fMRI scans and accompanying T1 anatomical scans in about 150 patients. The scans were obtained 1 week before they began a course of rTMS, targeting the dorsomedial prefrontal cortex. For each of these patients, we have pre- and post-treatment scores of depression symptom severity, on a standardized scale (the Beck Depression Inventory-II). Based on their symptom improvement, the sample divides into roughly equal proportions of treatment responders and non-responders (with response defined as ≥50% symptom improvement).  
### Our challenge to you is as follows:  
Develop a robust, automated classifier that can achieve ≥85% reliable prediction of treatment response or non-response based on the fMRI scans obtained prior to treatment. Use any set of features you wish: seed-based whole-brain functional connectivity maps, cross-correlation matrices, graph theoretical measures, dynamical measures of connectivity, or something more exotic. Use any classification algorithm you wish: support vector machines, multiple regression models, gaussian process classifiers, or your own “special sauce” method. Use any validation method you wish as well, but we want these models to generalize well, so the more robust your demonstration, the better!  
If you think you’re up to the challenge, please join us virtually or in person for the [2014 Toronto BrainHack EDT](http://brainhack.org/brainhack_edt/). We’ll be hosting the event over the weekend of Oct 18-19 at the University of Toronto’s Institute of Medical Science, at the computer lab in the Discovery Commons. Videoconferencing and high speed Ethernet / WiFi connections are available on site. Data will be accessible onsite or ahead of time via the Ontario Brain Institute’s BrainCode database. Lunch will be provided. Please do bring your own computer however – the local CPUs are limited in power.  

## Contact  
For more information or to RSVP, please contact the Downar lab via Katie Dunlop at [katharine.dunlop@gmail.com](mailto: katharine.dunlop@gmail.com)
Hosts:  
Dr. Jonathan Downar  
Director, MRI-Guided rTMS Clinic, Toronto Western Hospital  
Dr. Stephen Strother  
Senior Scientist, Rotman Research Institute  
Katie Dunlop  
MSc Candidate, Institute of Medical Science  
When:  
October 18-19, 2014, 9:00 a.m. to 5:00 p.m. (…)  
Where:  
Discovery Commons, Room 3172, Institute of Medical Science, University of Toronto  
1 King’s College Circle, Toronto, ON M5S 1A8 [Find Us](http://dc.med.utoronto.ca/content/find-us)  

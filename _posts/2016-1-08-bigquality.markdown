---
layout: post
title:  "Big Quality Control"
date:   2016-1-08 10:42:06
project_categories: Brainhack 2013
image: logo_qc_work_group1-190x180.png
description: Here we propose to address this question on a large and heterogeneous dataset, all the data acquired at the CENIR (Center of NeuroImaging Research) on a 3T Trio and a 3T Verio Siemens.
---

## Summary: MRI data quality control over a wide range of acquisition parameters
A reliable and automatic quality control of MRI data is still an important challenge. Here we propose to address this question on a large and heterogeneous dataset: all the data acquired at the CENIR (CEnter of NeuroImaging Research) on a 3T Trio and a 3T Verio Siemens. (10 000 subject acquired in 300 different projects , around 4 Tb. )
We would like to address two different objectives : 1_ Outlier detection, with an automatic classification of specific artefacts 2_ Acquisition parameters effect on resulting measures : the amount of heterogeneous (in term of acquisition parameters) datasets give us the opportunity to explore the influence of the acquisition parameters on the reliability (reproducibility) of the processing results (biomarkers). In that context, we are interested in optimizing the acquisitions parameters with respect to the variability of extracted biomarkers.
Detail of the different interdependent steps to achieve :
_ Extract the acquisition parameters from the dicom data, and construct a structured database. Sorry but I lost my note, so let see what is in the data : how many subjects how many functional runs how many different acquisition parameters for each acquisition type (fMIR, DWI, anatomical images, relaxometry, ASL spectroscopy …)
_ Extract quality indices (at volume or slice level). They must be specific for each modality : fMRI (ASL ?) DWI and anatomical images. For outlier detection quality indices are mainly define on raw data or after a minimal preprocessing (realignment) but it may be also instructive to look at specific processing step. For instance for DWI data, the residual of a the DTI tensor fit is very useful to see the remaining artefact. For the second objective we need to define indices to evaluate the reliability of a specific process (i.e. Local measures vs global measures) . This is a more difficult question since it will be dependent of the specific question.
The only constrain here is to have all process running automatically on a cluster.
_ Automatic detection of outlier with a classification of the artefacts. From our visual expertise we can observed different common artefact : _ spikes _ black slices (manly for DTI acquisitions) _ global mean signal fluctuations _ ghosting artefact (they often happen more pronounces in some time points) _ subject motion within the volume acquisition which lead to scramble volume or interslice mean signal modulation (an alternate succession of darker and brighter slices). Although those artefacts may occur all at the same time, they are most of the time distinct and it would be useful to have an automatic classification. one should then define specific quality indices to have an accurate detection of each artefact. An important issue of outlier detection is to define a proper threshold. The advantage of a large (and heterogeneous) dataset is that on can infer those threshold from robust statistic extracted from all the subject.
_ From Quality Control to parameter optimization. If one can define quality indices specific to the resulting process, one can then explore those indices over the range of value of each acquisition parameters to see if one can deduce what is the best acquisition parameters set. Let’s use the heterogeneity of acquisition parameters to address this question. For instance is the measure of integration of the default network

## What can I do?  
2 types of interaction is welcome : discussion or action. If you want to give a try, I’ll give access to our small cluster (30 nodes of 12 core, running with torque on centos6 ) and let’s process as much as possible.
many different expertise : _ database from dicom data _ automatic pipeline processing (if possible in relation with the database) _ quality control or artefact experiences. _ bio marker definition _ statistic

## How can I join?
Send me an email [romain.valabregue@upmc.fr](mailto: romain.valabregue@upmc.fr).   

## Who are the members?
Romain Valabregue in charge of data acquisition at the CENIR.

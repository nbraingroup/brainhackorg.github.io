---
layout: post
title:  "Autoseg SIN"
date:   2017-1-9 10:59:06
categories: Project
image: autoseg.png
description:  NI-DM is a format of describing neuroimaging experiments results. NeuroVault is a database for storing unthresholded statistical maps.
---
## Summary
Deep-Brain-Stimulation (DBS) is a widely used and highly-effective treatment in various diseases, the most common of which is Parkinson’s Disease (PD). In DBS-surgery of PD patients, an electrode is implanted into the subthalamic nucleus, a small subcortical structure of the brain. After surgery, it is important to ensure correct placement of DBS electrodes within the nucleus. To do so, a MATLAB® toolbox has been developed that is capable to localize DBS electrodes based on postoperative MR or CT data (LEAD-toolbox, Horn et al. 2013 – Abstract: Automatic reconstruction of DBS-Electrode Placement from post-operative MRI-images. Journal of Neural Transmission). Furthermore, the toolbox can be used to analyze connectomic influences between the DBS electrodes and the rest of the brain.
For now, the toolbox relates the electrodes exclusively to atlas data of subcortical structures (e.g. Jakab et al., 2012; Keuken et al., 2013; Prodoehl et al., 2008; Sarnthein et al., 2013; Tzourio-Mazoyer et al., 2002; Yelnik et al., 2003) and operates in MNI-space. To improve this procedure, it would be very valuable contribution to also be able to relate electrode placement to patient-specific subcortical structures. The STN as the primary target for DBS surgery is a small structure, but can be seen well on T2-weighted images because of its high iron content (Dormont et al., 2004).
The goal of this Hackathon project is to establish an algorithm that is capable to automatically shape out (segment) the nucleus from T2-weighted MR images in an observer-independent fashion.
## What can I do?
The LEAD-toolbox is constantly being developed and our small team is looking for collaborators and people that are interested in DBS and imaging. It has not yet been publicly released but this step will follow soon. Since the toolbox is a comparably small project, it is open to all ideas and suggestions related to the topic of post-operative DBS-electrode localization and visualization. Anybody willing to contribute ideas to the project is very warmly welcome. A clear goal of the Hackathon will be to set up a (preliminary) pipeline of subcortical segmentation based on patient and atlas data and to make contact to people interested to the field of DBS. Therefore, this project is a quite methodological and thus open to anybody interested in intensity-based brain segmentation. Ideas that go beyond this proposal that are related to DBS and imaging are also very welcome.


## Contact  
Andreas Horn  
[andres.horn@charite.de](mailto: andres.horn@charite.de)  

---
layout: post
title:  "Brain Parcellation"
date:   2016-1-03 10:42:06
project_categories: Brainhack 2013 Project Software
image: fig_clusters-222x153.png
description: In this project, we intend to focus on what would be optimal pre-processing choices in both diffusion- and functional-based clustering in order to optimize the clustering and make values and parcellations numerically comparable using a set of standards.  
---
## Summary:
Most connectivity-based clustering studies focus on choosing an appropriate clustering method or finding the optimal parameters given a specific clustering algorithm. However, before clustering is applied, many decisions are taken that can greatly affect the outcome of the parcellation: the choice of the connectivity fingerprints (in the case of anatomical connectivity: full tracts through white matter [Anwander et al., 2007; Johansen-Berg et al., 2004] or grey matter end-points endpoints [Bach et al., 2011]; In the case of fMRI, direct temporal correlation, or similarity of the correlation patterns to other cortical regions, etc) [Craddock et al. 2012; Blumensath et al. 2013]. The application or not of data smoothing, the choice of similarity measure between fingerprints (correlation, mutual information, independence of components).  

The consequences of these choices can be as important as the choice of clustering algorithm itself and its parameters and finding an optimal solution is not a simple problem. Notwithstanding, in most studies these matters are usually not investigated and the choices that are deemed more convenient for the specific objective at hand are taken. No study up to date has systematically characterized the effects and meaning of all these choices in the final parcellations/connectivity values.  

In this project, we intend to focus on what would be optimal pre-processing choices in both diffusion- and functional-based clustering in order to optimize the clustering and make values and parcellations numerically comparable using a set of standards.  

[ Data provided: pre-processed data from the publicly available NKI enhanced dMRI and fMRI sets of the fcon 1000 NITRC/INDI project to address the describe challenges (including registration and surface reconstruction). Also MRtrix tractography based connectivity ]

## What can I do?  
– Bring your positive aura and enthusiasm! – Contribute with data that could be used for this purpose – Contribute with clustering algorithms or different preprocessing steps to test – Help out with the implementation of the pipeline to test our results in brainhack – Bring in your expertise on the preprocessing and clustering issues and caveats in the different modalities – bring ideas about possible standards to evaluate our results (i.e, maximum agreement between fMRI and dMRI parcellations, maximal agreement with neuroanatomical parcellations [i. e. juelich cytoarchitectonic], maximal reproducibility, etc.) – meet us at brainhack!

## How can I join?
Drop me a mail! moreno@cbs.mpg.de

## Who are the members?
David Moreno-Dominguez: moreno@cbs.mpg.de [www.cbs.mpg.de/~moreno](www.cbs.mpg.de/~moreno)

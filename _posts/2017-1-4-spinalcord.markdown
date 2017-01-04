---
layout: post
title:  "Spinal Cord Gray Matter Segmentation Using Atlas Deformation"
date:   2017-1-4 10:59:06
categories: Project
image: spinalcord.png
description: We are currently working on an automatic segmentation method for the spinal cord gray matter on T2*-weighted images, based on the deformation (using ANTs) of a probabilistic map of the gray matter.
---
# Spinal Cord Gray Matter Segmentation Using Atlas Deformation

## Summary
The Spinal Cord Toolbox (SCT) is a comprehensive software enabling the registration of patient’s MR images on a generic template and the extraction of multi-parametric MR data in individual spinal cord tracts (http://sourceforge.net/projects/spinalcordtoolbox/). Currently, the SCT does not take the patient’s gray matter morphology into account for the deformation of white matter tracts; therefore resulting in possible tract position errors (e.g., tracts falling outside the spinal cord or overlapping the gray matter).

We are currently working on an automatic segmentation method for the spinal cord gray matter on T2*-weighted images, based on the deformation (using ANTs) of a probabilistic map of the gray matter. The resulting deformation field will be applied to the MNI-Poly-AMU white matter atlas and its integrity will be checked. During Brainhack, we will continue the development of this method. We would also like to discuss new possibilities to assess the integrity of the spinal cord white matter atlas

## Contact
Benjamin De Leener

[benjamin.de-leener@polymtl.ca](mailto: benjamin.de-leener@polymtl.ca)

[www.neuro.polymtl.ca](www.neuro.polymtl.ca)

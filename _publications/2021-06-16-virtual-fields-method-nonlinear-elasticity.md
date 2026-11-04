---
title: "General Finite-Element Framework of the Virtual Fields Method in Nonlinear Elasticity"
collection: publications
permalink: /publication/2021-virtual-fields-method-nonlinear-elasticity
redirect_from:
  - /publication/2021-6-16-paper-title-number-1
excerpt: ' '
date: 2021-6-16
venue: 'Journal of Elasticity'
paperurl: 'https://link.springer.com/article/10.1007/s10659-021-09842-8'
citation: 'Yue Mei, Jiahao Liu, Xu Guo, Brandon Zimmerman, Thao D. Nguyen, Stéphane Avril. (2021). &quot;General Finite-Element Framework of the Virtual Fields Method in Nonlinear Elasticity.&quot; <i>Journal of Elasticity</i>. 145(1-2): 265-294.'
header:
  teaser:
    - publications/2021-eye-biomechanics.webp
    - publications/2021-kinematics-configuration.png
---


**Abstract**
This paper presents a method to derive the virtual fields for identifying constitutive model parameters using the Virtual Fields Method (VFM). The VFM is an approach to identify unknown constitutive parameters using deformation fields measured across a given volume of interest. The general principle for solving identification problems with the VFM is first to derive parametric stress field, where the stress components at any point depend on the unknown constitutive parameters, across the volume of interest from the measured deformation fields. Applying the principle of virtual work to the parametric stress fields, one can write scalar equations of the unknown parameters and solve the obtained system of equations to deduce the values of unknown parameters. However, no rules have been proposed to select the virtual fields in identification problems related to nonlinear elasticity and there are multiple strategies possible that can yield different results. In this work, we propose a systematic, robust and automatic approach to reconstruct the systems of scalar equations with the VFM. This approach is well suited to finite-element implementation and can be applied to any problem provided that full-field deformation data are available across a volume of interest. We also successfully demonstrate the feasibility of the novel approach by multiple numerical examples. Potential applications of the proposed approach are numerous in biomedical engineering where imaging techniques are commonly used to observe soft tissues and where alterations of material properties are markers of diseased states.

![Reference, intermediate, and current configuration kinematics used in the VFM framework](/images/publications/2021-kinematics-configuration.png)

[Download paper here](https://link.springer.com/article/10.1007/s10659-021-09842-8)
---
title: "A massive MPI parallel framework of smoothed particle hydrodynamics with optimized memory management for extreme mechanics problems."
collection: publications
permalink: /publication/2023-mpi-sph-memory-management
redirect_from:
  - /publication/2023-10-9-paper-title-number-4
date: 2023-10-9
excerpt: ' '
venue: 'Computer Physics Communication'
paperurl: 'https://www.sciencedirect.com/science/article/pii/S0010465523003156'
citation: 'Jiahao Liu, Xiufeng Yang, Zhilang Zhang, Moubin Liu. (2023). &quot;A massive MPI parallel framework of smoothed particle hydrodynamics with optimized memory management for extreme mechanics problems.&quot; <i>Computer Physics Communication</i>. 108970.'
header:
  teaser:
    - publications/2023-10-impact-resolution-study.jpg
    - publications/2023-10-domain-decomposition.jpg
---

**Abstract**
The dynamic failure process of structures under extreme loadings is very common in many fields of engineering and science. The smoothed particle hydrodynamics (SPH) method offers inherent benefits in dealing with complex interfaces and large material deformations in extreme mechanics problems. However, SPH simulations for 3D engineering applications are time-consuming. To address this issue, we introduce MPI (Message Passing Interface) in our SPH scheme to reduce computational time. Some optimizations are adopted to ensure the massive computation of the SPH method. In particular, an optimized memory management strategy is developed to control the memory footprint. With the present MPI-based massive parallelization of the SPH method, several validation examples are tested and analysed. By comparing the present numerical results with the reference data, the dynamic failure process of complex structures subjected to extreme loadings like explosive and impact loadings can be well captured. A large number of particles, up to 2.04 billion, are adopted in the present simulations. The scaling tests show that the scalability of the massively parallel SPH program achieves a maximum parallel efficiency of 97% on 10020 CPU cores.

![Domain decomposition across processors, with an extended subdomain boundary for ghost particle exchange](/images/publications/2023-10-domain-decomposition.jpg)

[Download paper here](https://www.sciencedirect.com/science/article/pii/S0010465523003156)

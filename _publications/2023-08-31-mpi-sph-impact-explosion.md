---
title: "MPI Massive Parallelization of Smoothed Particle Hydrodynamics for Simulation of Impact and Explosion Problems"
collection: publications
permalink: /publication/2023-mpi-sph-impact-explosion
redirect_from:
  - /publication/2023-8-31-paper-title-number-3
date: 2023-8-31
excerpt: ' '
venue: 'The International Conference on Computational & Experimental Engineering and Sciences'
paperurl: 'https://doi.org/10.32604/icces.2023.010056'
citation: 'Jiahao Liu, Moubin Liu. (2023). &quot;MPI Massive Parallelization of Smoothed Particle Hydrodynamics for Simulation of Impact and Explosion Problems.&quot; <i>The International Conference on Computational & Experimental Engineering and Sciences</i>. 25(3), 1-1.'
header:
  teaser:
    - publications/2023-shaped-charge-numerical-model.jpg
    - publications/2026-jet-breakup-scaling.jpg
---


**Abstract**
The dynamic failure process of structures under impact and explosive loading is very common in both military and industrial fields. However, the conventional mesh-based method has some shortcomings, such as large mesh distortion and sliding surface treatment. Some typical phenomena are difficult to be simulated. The smoothed particle hydrodynamics (SPH) method has natural advantages in treating large material deformations in impact and explosion problems. To make the SPH method suitable for the impact and explosion problems, it is also improved by some treatments to avoid inherent stress instability and unphysical oscillation. However, numerical calculations for 3D engineering applications, especially by the SPH method, are time-consuming. For this reason, we introduce MPI (Message Passing Interface) in our SPH scheme to reduce computational time. Some optimizations are introduced to enable the large-scale computing of the SPH method. In particular, the memory footprint is controlled. With the present MPI massive parallelization ofthe SPH model, several validation examples are tested and analyzed. By comparing present numerical results with the reference data, we demonstrate that the parallel SPH is effective for modeling various impact and explosive problems. In addition, there are up to 2.04 billion particles in our simulation. The weak and strong scaling tests are adopted to show the scalability of the program. The maximum parallel efficiency can reach 97% on 10000 CPU cores. Furthermore, a specific example with impact and explosion problems is well simulated in this work.
[Download paper here](https://doi.org/10.32604/icces.2023.010056)

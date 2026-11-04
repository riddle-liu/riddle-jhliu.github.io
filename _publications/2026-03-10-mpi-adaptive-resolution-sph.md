---
title: "A massive MPI parallel adaptive resolution SPH method for large-scale multiphase flow simulations."
collection: publications
permalink: /publication/2026-mpi-adaptive-resolution-sph
redirect_from:
  - /publication/2026-3-10-paper-title-number-7
date: 2026-3-10
excerpt: ' '
venue: 'Computer Physics Communication'
paperurl: 'https://www.sciencedirect.com/science/article/pii/S0010465526001037'
citation: 'Lingxiao Ma, Jiahao Liu, Xiufeng Yang, Moubin Liu. (2026). &quot;A massive MPI parallel adaptive resolution SPH method for large-scale multiphase flow simulations.&quot; <i>Computer Physics Communication</i>. 110121.'
header:
  teaser:
    - publications/2026-droplet-coalescence.jpg
    - publications/2026-adaptive-ghost-particle.jpg
---

**Abstract**
The Smoothed Particle Hydrodynamics (SPH) method has been demonstrated great capabilities in simulating multiphase flows with large deformations and complex interfacial dynamics. However, 3D large-scale multiphase flow simulations require substantial computational resources, even when adaptive resolution methods are applied. To address this issue, we develop a massive MPI parallel adaptive resolution SPH method for simulating large-scale multiphase flows with complex interface. The method supports different resolutions within each subdomain. A parallel adaptive resolution method is employed to automatically identify refinement regions and dynamically adjust particle resolution through splitting and merging, while avoiding race conditions. To enhance parallel efficiency and scalability with the adaptive resolution method, the framework incorporates several optimized techniques. In particular, a history-based adaptive ghost particle management strategy is developed to dynamically adjust the exchange region according to local interaction demands, thereby reducing unnecessary communication. An axis-by-axis hierarchical load balancing method is introduced to update subdomain boundaries based on the number of interacting particle pairs, ensuring a balanced distribution of computational load. Several numerical examples are conducted to assess the performance of the proposed method, demonstrating its ability to efficiently capture complex multiphase interface dynamics in large-scale 3D simulations. The adaptive resolution method achieves substantial computational savings, reducing memory usage by up to 99% and CPU time by 97% compared with uniform resolution simulations. Weak scaling tests on distributed-memory systems show that the method maintains 93.5% parallel efficiency in a simulation with 1.34 billion particles on 10,976 CPU cores, equivalent to over 80 billion particles at uniform resolution.

![Two colliding droplets coalescing over time](/images/publications/2026-droplet-coalescence.jpg)

![History-based adaptive ghost particle management between subdomains](/images/publications/2026-adaptive-ghost-particle.jpg)

[Download paper here](https://www.sciencedirect.com/science/article/pii/S0010465526001037)

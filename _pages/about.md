---
permalink: /
title: "About Jiahao Liu"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

Jiahao Liu is a Ph.D. candidate at Brown University (Advisor: [Prof. Yuri Bazilevs](https://scholar.google.com/citations?user=U_FvD34AAAAJ&hl=en)) majoring in Mechanics of Solids, and is currently visiting Vanderbilt University.
<!-- postgraduate student in Peking University (Supervisor: [Prof. Moubin Liu](https://scholar.google.com/citations?user=guclLlYAAAAJ&hl=en)) and major in engneering mechanics.  -->
He has been focusing on research about computational fluid-structure interaction, mesh-based methods, meshless methods and high performance computing. He is working on Updated Lagrangian IGA for thin shell and stability of Triply Periodic Minimal Surface Structures. 
<!-- Also, he is working on reduced quadrature; RKPM; jax-based computing as well. -->
  He has immersed himself in computational mechanics, diligently improving his "*yield strength*" and "*fatigue strength*". He is looking forward to simulating everything and building the bridge from theoretical knowledge to engineering applications. In terms of hobbies, he likes music, calligraphy, and all kinds of sports, such as snowboarding, tennis, basketball and swimming.
 <!-- "Stay hungry, Stay foolish." -->

Please feel free to contact him if you have any queries.

<!-- /Русский -->
<p align="right"> (Recent update on 2026/9/16) </p>

## Recent Publications
{% assign recent_pubs = site.publications | sort: "date" | reverse %}
{% for p in recent_pubs limit: 3 %}
* [{{ p.title | markdownify | remove: "<p>" | remove: "</p>" | strip }}]({{ p.url }}), *{{ p.venue }}*, {{ p.date | date: "%Y" }}
{% endfor %}

[All publications &rarr;](/publications/)

## Recent Talks
{% assign recent_talks = site.talks | sort: "date" | reverse %}
{% for t in recent_talks limit: 2 %}
* [{{ t.title }}]({{ t.url }}) ({{ t.type }}), {{ t.location }}, {{ t.date | date: "%Y" }}
{% endfor %}

[All talks &rarr;](/talks/)

## Education
* **Ph.D.** in Mechanics of Solids, Brown University, expected 2028
* **Master's Degree** in Mechanical Engineering, Peking University, 2024
* **Bachelor's Degree** in Engineering Mechanics (Major) and Business Administration (Minor), Dalian University of Technology, 2021

Supervisors and research history are listed in the [CV](/cv/).

## Contact
Room 260, 2001 Grand Ave, Nashville, TN 37212 &middot; [View on Google Maps](https://www.google.com/maps/place/2001+Grand+Ave,+Nashville,+TN+37212)

<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2168.8500778000093!2d-86.79807823032549!3d36.14678789827753!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x886466972597ef41%3A0xead5009322beb3b5!2s2001%20Grand%20Ave%2C%20Nashville%2C%20TN%2037212!5e1!3m2!1sen!2sus!4v1785775163242!5m2!1sen!2sus" title="Map of 2001 Grand Ave, Nashville" style="border:0; width:100%; height:240px;" allowfullscreen="" loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe>

<!-- Besides Meeting Room 250, Brown University Engineering Research Center, 345 Brook St
Providence, Rhode Island 02912

<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5946.164465879494!2d-71.40114382267268!3d41.8265273686397!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89e445cc445ec1eb%3A0x33dbf48bee59674d!2sBrown%20University%20Engineering%20Research%20Center!5e0!3m2!1sen!2sus!4v1755706189301!5m2!1sen!2sus" width="600" height="500" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe> -->
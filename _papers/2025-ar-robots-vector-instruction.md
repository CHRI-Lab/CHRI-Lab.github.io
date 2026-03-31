---
layout: paper
title: 'Going Down the Abstraction Stream with Augmented Reality and Tangible Robots: The Case of Vector
  Instruction'
subtitle: Concreteness fading via AR and tangible robots helps students build intuitive understanding
  of graphical vector addition.
slug: 2025-ar-robots-vector-instruction
authors:
- name: Sergei Volodin
  affiliation: Ecole Polytechnique Fédérale de Lausanne
  photo: /assets/papers/2025-ar-robots-vector-instruction/authors/sergeivolodin.jpg
- name: Hala Khodr
  affiliation: Ecole Polytechnique Fédérale de Lausanne
  photo: /assets/papers/2025-ar-robots-vector-instruction/authors/halakhodr.jpg
- name: Pierre Dillenbourg
  affiliation: Ecole Polytechnique Fédérale de Lausanne
  photo: /assets/papers/2025-ar-robots-vector-instruction/authors/pierredillenbourg.jpg
- name: Wafa Johal
  affiliation: University of Melbourne
  photo: /assets/papers/2025-ar-robots-vector-instruction/authors/wafajohal.jpg
venue: arXiv preprint
year: '2025'
abstract: 'Despite being used in many engineering and scientific areas such as physics and mathematics
  and often taught in high school, graphical vector addition turns out to be a topic prone to misconceptions
  in understanding even at university-level physics classes. To improve the learning experience and the
  resulting understanding of vectors, we propose to investigate how concreteness fading implemented with
  the use of augmented reality and tangible robots could help learners to build a strong representation
  of vector addition.


  We design a gamified learning environment consisting of three concreteness fading stages and conduct
  an experiment with 30 participants. Our results show a positive learning gain. We analyze extensively
  the behavior of the participants to understand the usage of the technological tools — augmented reality
  and tangible robots — during the learning scenario. Finally, we discuss how the combination of these
  tools shows real advantages in implementing the concreteness fading paradigm. Our work provides empirical
  insights into how users utilize concrete visualizations conveyed by a haptic-enabled robot and augmented
  reality in a learning scenario.'
keywords:
- Concreteness Fading
- Augmented Reality
- Tangible Robots
- Vector Addition
- Mathematics Education
- Human-Robot Interaction
- Embodied Learning
- Gamified Learning
figures: true
bibtex: "@article{volodin2025vectorinstruction,\n  title     = {Going Down the Abstraction Stream with\
  \ Augmented Reality and Tangible Robots: The Case of Vector Instruction},\n  author    = {Volodin, Sergei\
  \ and Khodr, Hala and Dillenbourg, Pierre and Johal, Wafa},\n  journal   = {arXiv preprint arXiv:2504.14562},\n\
  \  year      = {2025},\n  url       = {https://arxiv.org/abs/2504.14562},\n  website   = {https://chri-lab.github.io/papers/2025-ar-robots-vector-instruction/}\n\
  }"
---

## Key Findings

<ul class="findings-list">
  <li>**Positive learning gains were observed.** Participants demonstrated measurable improvement in vector addition performance from pre-test to post-test across both Year 10 and Year 12 groups.</li>
  <li>**AR and tangible robots effectively support concreteness fading.** The three-stage progression (enactive, iconic, symbolic) was successfully instantiated using the Cellulo robot and augmented reality overlays.</li>
  <li>**Performance improved with advancing abstraction stages.** Analysis of absolute error angles across game levels indicated that participants adapted to increasingly abstract representations over time.</li>
  <li>**Gamification reduced mathematical anxiety.** The use of game-like elements, team play, and gradual difficulty scaling contributed to an approachable and engaging learning experience.</li>
  <li>**Rich behavioral data revealed distinct usage patterns.** Timeline and correlation analyses of AR and robot interaction metrics provided empirical insight into how learners engage with concrete versus abstract visualizations.</li>
</ul>

## Method

The study employed a gamified learning environment built around the concreteness fading framework, progressing through three stages: enactive (physical robot movement), iconic (graphical pictorial representation), and symbolic (abstract vector notation). Participants used a Cellulo tangible robot — a small haptic-enabled robot — to set the velocity of a virtual ship by physically moving the robot in the desired direction, with augmented reality overlays displaying directional feedback as arrows on a paper-based game sheet. The game consisted of 10 levels in which players had to navigate a ship to a goal position under the influence of wind and river-current forces, requiring correct graphical vector addition.

Thirty participants were organized into teams and completed a pre-test, the learning activity, and a post-test. The activity was displayed across tablet screens embedded beneath the main paper working sheet, cycling through the three concreteness fading stages for each level. Behavioral data were collected across multiple modalities, including AR tracking metrics (tablet orientation, coordinates, and their derivatives) and robot usage timelines, enabling detailed analysis of how participants interacted with the tools at each stage of abstraction.

Quantitative analyses included pre/post-test score comparisons, absolute error angle measurements per level, timeline visualizations of device usage, and correlation analyses of AR interaction metrics. This multi-modal approach allowed the researchers to characterize not only learning outcomes but also the behavioral dynamics of moving through the concreteness fading stages.

## Results

The experiment with 30 participants showed a positive learning gain from pre-test to post-test for both Year 10 and Year 12 groups, supporting the hypothesis that the concreteness fading game leads to improved understanding of vector addition. Analysis of absolute error angles across the 10 game levels revealed a general improvement in accuracy over the course of the activity, with confidence intervals indicating meaningful reductions in directional error. Timeline analyses showed distinct patterns of device engagement across the three concreteness fading stages. Correlation analyses of AR metrics (sheet orientation, coordinates, and their derivatives) revealed high correlation values for the first paper sheet, suggesting more stable and deliberate interaction during early, more concrete stages. Behavioral data confirmed that the combination of AR and tangible robots was usable and effective for embodying the transition from concrete to abstract mathematical representations.

## Figures

<div class="paper-figures">
  <figure class="paper-figure">
    <img src="{{ '/assets/papers/2025-ar-robots-vector-instruction/fig1.png' | relative_url }}" alt="Figure 1">
    <figcaption>Activity Flow. The main working sheet (shown as C) contains 10 game levels located across a river (labeled A, B, ..., I). For each level, participants need to set the correct velocity to reach the gold (yellow circles with gold plates on the main working sheet). The velocity is set on a separate paper sheet (shown in A). The participant grabs the robot with their hand and moves it in the direction they want to set; the direction is shown in AR as a green arrow. Next, the robot is placed at the starting point (dock) of the level (shown in B), and the robot moves in the direction determined by the velocity, and also by the wind and the river's current. The tablet screens below the main sheet show the three stages of concreteness fading: Enactive, Iconic, and Symbolic.</figcaption>
  </figure>
  <figure class="paper-figure">
    <img src="{{ '/assets/papers/2025-ar-robots-vector-instruction/fig2.png' | relative_url }}" alt="Figure 2">
    <figcaption>Illustration of concreteness fading. The physical/enactive representation refers to an actual moving ship. The pictorial/iconic representation refers to the notion of a moving ship, and the idealized/symbolic representation refers to the velocity vectors of the wind (brown), the river (blue), and the boat (green).</figcaption>
  </figure>
  <figure class="paper-figure">
    <img src="{{ '/assets/papers/2025-ar-robots-vector-instruction/fig3.png' | relative_url }}" alt="Figure 3">
    <figcaption>Software architecture of the activity, detailing in particular the paper-based localisation system used to track the robot and the tablets on the working sheet.</figcaption>
  </figure>
  <figure class="paper-figure">
    <img src="{{ '/assets/papers/2025-ar-robots-vector-instruction/fig4.png' | relative_url }}" alt="Figure 4">
    <figcaption>Top: screenshot of level 'A' in the game showing the ship (robot) at the dock (bottom left), leaves and environmental elements indicating wind and current forces.</figcaption>
  </figure>
  <figure class="paper-figure">
    <img src="{{ '/assets/papers/2025-ar-robots-vector-instruction/fig5.png' | relative_url }}" alt="Figure 5">
    <figcaption>Three stages of concreteness fading implemented in the learning activity, progressing from enactive (physical robot interaction) to iconic (graphical pictorial) to symbolic (abstract vector) representations.</figcaption>
  </figure>
  <figure class="paper-figure">
    <img src="{{ '/assets/papers/2025-ar-robots-vector-instruction/fig6.png' | relative_url }}" alt="Figure 6">
    <figcaption>Pre- and post-test average scores for Year 10 and Year 12 teams.</figcaption>
  </figure>
  <figure class="paper-figure">
    <img src="{{ '/assets/papers/2025-ar-robots-vector-instruction/fig7.png' | relative_url }}" alt="Figure 7">
    <figcaption>Graphical addition done right. To obtain the direction of the answer, or total ship's velocity correctly (shown in red), the vectors must be added graphically using the tip-to-tail method.</figcaption>
  </figure>
  <figure class="paper-figure">
    <img src="{{ '/assets/papers/2025-ar-robots-vector-instruction/fig8.png' | relative_url }}" alt="Figure 8">
    <figcaption>Distribution of pre- and post-test scores. The color indicates which levels were solved by the participants during the learning activity.</figcaption>
  </figure>
  <figure class="paper-figure">
    <img src="{{ '/assets/papers/2025-ar-robots-vector-instruction/fig9.png' | relative_url }}" alt="Figure 9">
    <figcaption>Absolute Error Angle for each level (95% confidence interval). The color of the bar indicates the concreteness fading stage associated with each level.</figcaption>
  </figure>
  <figure class="paper-figure">
    <img src="{{ '/assets/papers/2025-ar-robots-vector-instruction/fig10.png' | relative_url }}" alt="Figure 10">
    <figcaption>Timeline of the gameplay over devices for both participant groups.</figcaption>
  </figure>
  <figure class="paper-figure">
    <img src="{{ '/assets/papers/2025-ar-robots-vector-instruction/fig11.png' | relative_url }}" alt="Figure 11">
    <figcaption>XY plots for the metrics used in the experiment.</figcaption>
  </figure>
  <figure class="paper-figure">
    <img src="{{ '/assets/papers/2025-ar-robots-vector-instruction/fig12.jpeg' | relative_url }}" alt="Figure 12">
    <figcaption>Timelines for one of the games for AR metrics. The top two charts show rotation (Euler angles for the x and y axes), with additional metrics displayed below.</figcaption>
  </figure>
  <figure class="paper-figure">
    <img src="{{ '/assets/papers/2025-ar-robots-vector-instruction/fig13.png' | relative_url }}" alt="Figure 13">
    <figcaption>Correlation coefficients between all AR metrics (angle, coordinate, and their derivatives). High values for sheet 1 indicate more stable and deliberate interaction during the early concrete stage.</figcaption>
  </figure>
  <figure class="paper-figure">
    <img src="{{ '/assets/papers/2025-ar-robots-vector-instruction/fig14.png' | relative_url }}" alt="Figure 14">
    <figcaption>The velocity setting stage, showing a participant interacting with the Cellulo robot to set the ship's direction on the paper sheet.</figcaption>
  </figure>
</div>


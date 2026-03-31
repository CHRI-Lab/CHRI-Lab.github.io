---
layout: paper
title: Using Fitts' Law to Benchmark Assisted Human-Robot Performance
subtitle: A formal benchmarking framework that quantifies how task difficulty and robot autonomy jointly
  shape performance and cognitive load in shared control.
slug: 2024-fitts-law-hrc-benchmark
authors:
- name: Jiahe Pan
  affiliation: The University of Melbourne
  photo: /assets/papers/2024-fitts-law-hrc-benchmark/authors/jiahepan.jpg
- name: Jonathan Eden
  affiliation: The University of Melbourne
  photo: /assets/papers/2024-fitts-law-hrc-benchmark/authors/jonathaneden.jpg
- name: Denny Oetomo
  affiliation: The University of Melbourne
  photo: /assets/papers/2024-fitts-law-hrc-benchmark/authors/dennyoetomo.jpg
- name: Wafa Johal
  affiliation: The University of Melbourne
  photo: /assets/papers/2024-fitts-law-hrc-benchmark/authors/wafajohal.jpg
venue: IEEE International Conference on Robot and Human Interactive Communication (RO-MAN) / ICRA
year: '2024'
abstract: Shared control systems aim to combine human and robot abilities to improve task performance.
  However, achieving optimal performance requires that the robot's level of assistance adjusts the operator's
  cognitive workload in response to the task difficulty. Understanding and dynamically adjusting this
  balance is crucial to maximizing efficiency and user satisfaction. In this paper, we propose a novel
  benchmarking method for shared control systems based on Fitts' Law to formally parameterize the difficulty
  level of a target-reaching task. With this we systematically quantify and model the effect of task difficulty
  (i.e. size and distance of target) and robot autonomy on task performance and operators' cognitive load
  and trust levels. Our empirical results (N=24) not only show that both task difficulty and robot autonomy
  influence task performance, but also that the performance can be modelled using these parameters, which
  may allow for the generalization of this relationship across more diverse setups. We also found that
  the users' perceived cognitive load and trust were influenced by these factors. Given the challenges
  in directly measuring cognitive load in real-time, our adapted Fitts' model presents a potential alternative
  approach to estimate cognitive load through determining the difficulty level of the task, with the assumption
  that greater task difficulty results in higher cognitive load levels. We hope that these insights and
  our proposed framework inspire future works to further investigate the generalizability of the method,
  ultimately enabling the benchmarking and systematic assessment of shared control quality and user impact,
  which will aid in the development of more effective and adaptable systems.
keywords:
- Human-Robot Collaboration
- Shared Control
- Fitts' Law
- Benchmarking
- Cognitive Load
- Trust
- Teleoperation
- Task Difficulty
venue_logo: https://www.ieee-ras.org/images/logos/ieee-ras-logo.png
figures: true
bibtex: "@inproceedings{pan2024fitts,\n  title     = {Using Fitts' Law to Benchmark Assisted Human-Robot\
  \ Performance},\n  author    = {Pan, Jiahe and Eden, Jonathan and Oetomo, Denny and Johal, Wafa},\n\
  \  booktitle = {Proceedings of the IEEE International Conference on Robot and Human Interactive Communication\
  \ (RO-MAN)},\n  year      = {2024},\n  note      = {Project website: https://sites.google.com/view/autonomyfitts/home},\n\
  \  website   = {https://chri-lab.github.io/papers/2024-fitts-law-hrc-benchmark/}\n}"
---

## Key Findings

<ul class="findings-list">
  <li>**Task difficulty and robot autonomy both significantly affect task performance.** Movement time and error rates varied systematically with the Fitts' Law index of difficulty and the level of robot assistance.</li>
  <li>**Performance can be formally modelled using an adapted Fitts' Law.** Incorporating robot autonomy as a parameter into the classical Fitts' model captured the difficulty–performance relationship across shared control conditions.</li>
  <li>**Cognitive load and trust perceptions are shaped by task difficulty and autonomy level.** Higher task difficulty increased perceived cognitive load, while robot autonomy modulated users' trust ratings.</li>
  <li>**Fitts' Law offers a promising proxy for real-time cognitive load estimation.** Because greater task difficulty reliably increased subjective workload, the index of difficulty may serve as an indirect, real-time cognitive load indicator in adaptive systems.</li>
  <li>**The framework supports replicable and generalizable evaluation of shared control.** By formally parameterizing reaching tasks, the method addresses the lack of a common benchmark for assessing shared control efficacy across different setups.</li>
</ul>

## Method

We conducted a within-subjects teleoperation study (N=24) in which participants used a Novint Falcon haptic controller to move a robot arm's end-effector to a sequence of targets displayed on screen. Task difficulty was manipulated by varying the amplitude (distance to target) and width (target size) of each reaching motion according to Fitts' Law, yielding a range of Index of Difficulty (ID) values. Three levels of robot autonomy were applied using a blended shared-control scheme that continuously mixed human commands with an autonomous controller, allowing systematic variation of the degree of robot assistance.

Participants completed target-reaching trials across all combinations of task difficulty and autonomy level, following a training phase to familiarise them with the interface. Objective measures included movement time and task accuracy, while subjective measures comprised the NASA-TLX for cognitive load and the Multi-Dimensional Measure of Trust (MDMT) for trust. An eye-tracker (Tobii) was also integrated into the setup for supplementary data collection.

The adapted Fitts' model was fit to the movement time data with both ID and autonomy level as predictors, and statistical analyses (including post-hoc comparisons) were used to identify significant effects of each factor on all dependent measures. This allowed us to characterise how the classical linear ID–MT relationship shifts under different levels of robot assistance.

## Results

Across 24 participants, both task difficulty (Fitts' ID) and robot autonomy level had significant effects on task performance. Movement time increased with higher ID values and decreased with greater robot assistance, consistent with Fitts' Law predictions. The adapted model incorporating autonomy as an additional parameter provided a good fit to the observed data, suggesting the relationship can generalise across conditions. Perceived cognitive load (NASA-TLX) was higher for more difficult tasks and was modulated by autonomy level, supporting the use of ID as a proxy for cognitive workload. Trust (MDMT) scores also varied with autonomy and task difficulty, with users reporting different levels of capacity and moral trust depending on the degree of robot assistance provided. Post-hoc analyses revealed specific pairwise differences across ring difficulty levels, confirming that finer-grained manipulations of ID produce measurable and distinguishable changes in both objective and subjective outcomes.

## Figures

<div class="paper-figures">
  <figure class="paper-figure">
    <img src="{{ '/assets/papers/2024-fitts-law-hrc-benchmark/fig1.png' | relative_url }}" alt="Figure 1">
    <figcaption>An illustration of Fitts' Law. Amplitude (A) and Width (W) determine the index of difficulty of the reaching motion.</figcaption>
  </figure>
  <figure class="paper-figure">
    <img src="{{ '/assets/papers/2024-fitts-law-hrc-benchmark/fig2.png' | relative_url }}" alt="Figure 2">
    <figcaption>Experimental setup (a) and the task visualization (b). The target-reaching task was performed via a Novint Falcon controller with visual feedback on screen. The ring of targets and the position of the end-effector at each time instant were displayed.</figcaption>
  </figure>
  <figure class="paper-figure">
    <img src="{{ '/assets/papers/2024-fitts-law-hrc-benchmark/fig3.png' | relative_url }}" alt="Figure 3">
    <figcaption>Visualization of the ring geometry (a) and the reaching sequence used in the experiment.</figcaption>
  </figure>
  <figure class="paper-figure">
    <img src="{{ '/assets/papers/2024-fitts-law-hrc-benchmark/fig4.png' | relative_url }}" alt="Figure 4">
    <figcaption>Experimental procedure including the training phase and the main study phase.</figcaption>
  </figure>
  <figure class="paper-figure">
    <img src="{{ '/assets/papers/2024-fitts-law-hrc-benchmark/fig5.jpeg' | relative_url }}" alt="Figure 5">
    <figcaption>Boxplots showing the distributions of each measure against ring number, grouped by autonomy level. Differences observed from post-hoc analyses are indicated.</figcaption>
  </figure>
  <figure class="paper-figure">
    <img src="{{ '/assets/papers/2024-fitts-law-hrc-benchmark/fig6.jpeg' | relative_url }}" alt="Figure 6">
    <figcaption>Figure 6.</figcaption>
  </figure>
  <figure class="paper-figure">
    <img src="{{ '/assets/papers/2024-fitts-law-hrc-benchmark/fig7.png' | relative_url }}" alt="Figure 7">
    <figcaption>Figure 7.</figcaption>
  </figure>
  <figure class="paper-figure">
    <img src="{{ '/assets/papers/2024-fitts-law-hrc-benchmark/fig8.png' | relative_url }}" alt="Figure 8">
    <figcaption>Figure 8.</figcaption>
  </figure>
  <figure class="paper-figure">
    <img src="{{ '/assets/papers/2024-fitts-law-hrc-benchmark/fig9.png' | relative_url }}" alt="Figure 9">
    <figcaption>Figure 9.</figcaption>
  </figure>
  <figure class="paper-figure">
    <img src="{{ '/assets/papers/2024-fitts-law-hrc-benchmark/fig10.png' | relative_url }}" alt="Figure 10">
    <figcaption>Figure 10.</figcaption>
  </figure>
  <figure class="paper-figure">
    <img src="{{ '/assets/papers/2024-fitts-law-hrc-benchmark/fig11.png' | relative_url }}" alt="Figure 11">
    <figcaption>Figure 11.</figcaption>
  </figure>
  <figure class="paper-figure">
    <img src="{{ '/assets/papers/2024-fitts-law-hrc-benchmark/fig12.png' | relative_url }}" alt="Figure 12">
    <figcaption>Figure 12.</figcaption>
  </figure>
</div>


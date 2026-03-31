---
layout: paper
title: Investigating the Impact of Robot Degree of Redundancy on Learning from Demonstration
subtitle: How robot kinematic redundancy shapes human teaching effort and downstream robot learning outcomes.
slug: 2026-robot-redundancy-lfd
authors:
- name: Muhammad Bilal
  affiliation: The University of Melbourne
  photo: /assets/papers/2026-robot-redundancy-lfd/authors/muhammadbilal.jpg
- name: D. Antony Chacon
  affiliation: The University of Melbourne
  photo: /assets/papers/2026-robot-redundancy-lfd/authors/dantonychacon.jpg
- name: Nir Lipovetzky
  affiliation: The University of Melbourne
  photo: /assets/papers/2026-robot-redundancy-lfd/authors/nirlipovetzky.jpg
- name: Denny Oetomo
  affiliation: The University of Melbourne
  photo: /assets/papers/2026-robot-redundancy-lfd/authors/dennyoetomo.jpg
- name: Wafa Johal
  affiliation: The University of Melbourne
  url: https://wafa.johal.org
  photo: /assets/papers/2026-robot-redundancy-lfd/authors/wafajohal.jpg
venue: ACM/IEEE International Conference on Human-Robot Interaction (HRI)
year: '2026'
abstract: 'Learning from Demonstration (LfD) allows robots to acquire skills from human demonstrations,
  making them more accessible to a wider range of users. Among different approaches, kinesthetic teaching
  allows humans to manipulate the robot joints directly, making it an effective method for demonstrating
  constrained tasks. However, robots with kinematic redundancy enable multiple joint configurations to
  achieve a desired task, which could influence human teaching performance. On one hand, it could make
  teaching easier by allowing more freedom to demonstrate the task; on the other, it also increases the
  number of joints that need to be manipulated, potentially affecting the cognitive and physical load
  of the demonstrator. Therefore, it is crucial to investigate how the number of degrees of redundancy
  (DoR) impacts human performance during kinesthetic demonstrations, and how these demonstrations in turn
  influence robot performance. We simulated high and low DoR by locking one joint on a 7-DoF Panda robotic
  arm. We conducted a within-subject user study (N = 24) with two conditions: unconstrained (high DoR)
  and constrained (low DoR). A motion capture system was used to record participants'' physical interaction
  with the robot while they demonstrated two tasks: button pressing and cuboid block insertion. The results
  show that the robot''s DoR significantly affects mental workload, demonstration time, number of failed
  attempts, and physical interaction with the robot. Joint constraints also significantly influenced robot
  performance, measured by task completion using the learned model. These findings highlight the importance
  of considering robot DoR when demonstrating constrained tasks, enabling novice users to provide effective
  demonstrations.'
keywords:
- Learning from Demonstration
- Kinesthetic Teaching
- Kinematic Redundancy
- Human-Robot Interaction
- Mental Workload
- Robot Performance
- User Study
- Degrees of Freedom
acknowledgements: 'This work was partially supported by the Australian Research Council (Grants No.: DE210100858;
  CE260100108; DP260101082; FT250100459).'
bibtex: "@inproceedings{bilal2026redundancy,\n  author    = {Bilal, Muhammad and Chacon, D. Antony and\
  \ Lipovetzky, Nir and Oetomo, Denny and Johal, Wafa},\n  title     = {Investigating the Impact of Robot\
  \ Degree of Redundancy on Learning from Demonstration},\n  booktitle = {Proceedings of the 21st ACM/IEEE\
  \ International Conference on Human-Robot Interaction (HRI '26)},\n  year      = {2026},\n  month  \
  \   = {March},\n  address   = {Edinburgh, Scotland, UK},\n  publisher = {ACM},\n  pages     = {9 pages},\n\
  \  doi       = {10.1145/3757279.3785606},\n  isbn      = {979-8-4007-2128-1},\n  website   = {/papers/2026-robot-redundancy-lfd/}\n\
  }"
---

## Key Findings

<ul class="findings-list">
  <li>**Reduced redundancy increases mental workload.** Demonstrating tasks under the constrained (low DoR) condition imposed a significantly higher mental workload on users.</li>
  <li>**Constrained conditions slow down teaching.** Task demonstration time increased as the degree of redundancy was reduced, making the teaching process less efficient.</li>
  <li>**Fewer degrees of redundancy lead to more failures.** The constrained condition resulted in significantly more failed demonstration attempts compared to the unconstrained condition.</li>
  <li>**Users physically interact more with the robot under constraint.** Reduced redundancy caused participants to make increased and more varied physical contact with robot joints during demonstrations.</li>
  <li>**Demonstration quality under constraint degrades robot learning.** Demonstrations collected under reduced redundancy negatively affected subsequent robot task-completion performance.</li>
</ul>

## Method

We designed a within-subject study (N = 24) using a 7-DoF Franka Panda robotic arm to compare two conditions: an unconstrained condition (high degree of redundancy, all joints free) and a constrained condition (low degree of redundancy, one joint locked). This manipulation allowed us to isolate the effect of kinematic redundancy without changing the robot platform or tasks. Participants were asked to provide kinesthetic demonstrations for two constrained tasks: button pressing and cuboid block insertion.

A motion capture system was used to record participants' hand positions and contacts with individual robot joints throughout each demonstration, enabling fine-grained joint-level analysis of physical interaction patterns. Mental workload was assessed using a validated subjective measure, and demonstration time and failed attempts were logged automatically. The combination of subjective, behavioural, and motion-capture data provides a multi-faceted picture of how redundancy affects the human side of the LfD process.

Following the human demonstration phase, a robot learning model was trained on the collected demonstrations and evaluated on task completion rate, allowing us to directly link human demonstration quality—shaped by the DoR condition—to downstream robot performance. The full dataset (InteractLFD) collected during the study is released as supplementary material to support reproducibility and future research.

## Results

The robot's degree of redundancy had a significant effect across all measured outcomes. Under the constrained (low DoR) condition, participants reported higher mental workload, took longer to complete demonstrations, and made more failed attempts than in the unconstrained condition. Motion capture data revealed that reduced redundancy led to increased physical interaction with robot joints, suggesting users compensated for the restricted configuration space by manipulating the arm more extensively. Downstream robot performance was also affected: models trained on demonstrations collected under the constrained condition achieved lower task completion rates than those trained on unconstrained demonstrations, for both the button-pressing and cuboid block insertion tasks. Together, these results indicate that robot kinematic redundancy is an important design consideration that directly shapes both the human teaching experience and the quality of the learned robot behaviour.

## Figures

<!-- Add figures below using this pattern:
<div class="paper-figures">
  <figure class="paper-figure">
    <img src="{{ '/assets/papers/2026-robot-redundancy-lfd/fig1.png' | relative_url }}" alt="Figure 1">
    <figcaption>Figure 1: Caption here.</figcaption>
  </figure>
</div>
-->

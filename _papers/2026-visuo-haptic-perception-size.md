---
layout: paper
title: Modelling Visuo-Haptic Perception Change in Size Estimation Tasks
subtitle: How our brains drift, reset, and adapt when vision and touch disagree about object size over
  time.
slug: 2026-visuo-haptic-perception-size
authors:
- name: Jian Zhang
  affiliation: University of Melbourne
  photo: /assets/authors/jianzhang.jpg
- name: Wafa Johal
  affiliation: University of Melbourne
  photo: /assets/authors/wafajohal.jpg
- name: Jarrod Knibbe
  affiliation: The University of Queensland
  photo: /assets/authors/jarrodknibbe.jpg
venue: ACM CHI Conference on Human Factors in Computing Systems (CHI '26)
year: '2026'
abstract: Tangible interactions involve multiple sensory cues, enabling the accurate perception of object
  properties, such as size. Research has shown, however, that if we decouple these cues (for example,
  by altering the visual cue), then the resulting discrepancies present new opportunities for interactions.
  Perception over time though, not only relies on momentary sensory cues, but also on a priori beliefs
  about the object, implying a continuing update cycle. This cycle is poorly understood and its impact
  on interaction remains unknown. We study (N=80) visuo-haptic perception of size over time and (a) reveal
  how perception drifts, (b) examine the effects of visual priming and dead-reckoning, and (c) present
  a model of visuo-haptic perception as a cyclical, self-adjusting system. Our work has a direct impact
  on illusory perception in VR, but also sheds light on how our visual and haptic systems cooperate and
  diverge.
keywords:
- Visuo-Haptic Perception
- Haptic Illusions
- Virtual Reality
- Sensory Integration
- Perceptual Drift
- Visual Priming
- Proprioception
- Size Estimation
venue_logo: https://sigchi.org/wp-content/uploads/2024/01/cropped-sigchi-icon-192x192.png
bibtex: "@inproceedings{zhang2026visuohaptic,\n  author    = {Jian Zhang and Wafa Johal and Jarrod Knibbe},\n\
  \  title     = {Modelling Visuo-Haptic Perception Change in Size Estimation Tasks},\n  booktitle = {Proceedings\
  \ of the 2026 CHI Conference on Human Factors in Computing Systems},\n  series    = {CHI '26},\n  year\
  \      = {2026},\n  pages     = {18 pages},\n  publisher = {ACM},\n  address   = {New York, NY, USA},\n\
  \  doi       = {10.1145/3772318.3791140},\n  isbn      = {979-8-4007-2278-3/2026/04},\n  location  =\
  \ {Barcelona, Spain},\n  website   = {https://chri-lab.github.io/papers/2026-visuo-haptic-perception-size/}\n\
  }"
---

## Key Findings

<ul class="findings-list">
  <li>**Perception drifts toward overestimation over time.** For passive haptic objects, perceived size increasingly exceeds actual size, following a curve toward a local asymptote.</li>
  <li>**Active shape-changing devices skew perception differently.** When a device physically shrinks, subsequent size perception drifts toward underestimation rather than overestimation.</li>
  <li>**Visual priming anchors and stabilises perception.** Revealing the true device appearance sets a more accurate initial perception and reduces perceptual drift across the full experience.</li>
  <li>**Intermittent priming acts as perceptual dead-reckoning.** Selectively showing the device at key moments resets perception toward the primed value, analogous to navigational dead-reckoning.</li>
  <li>**Visuo-haptic integration can be modelled as a first-order control system.** Perceptive discrimination acts as an amplifier, and the feedback loop is modulated by the user's confidence in their perception.</li>
</ul>

## Method

The study recruited 80 participants divided into four groups, each engaging in one-hour sessions in virtual reality. Conditions varied across two haptic device types — a fixed-size passive device and a custom-built active shape-changing device that dynamically altered its size between 6 cm and 8 cm — and three visual priming strategies: no priming, correct visual priming (revealing the true device), and misleading priming (revealing a device of a different size).

Participants completed repeated forced-choice tasks to estimate perceived object size at multiple time points throughout the session. Between estimation tasks, acclimation games simulated prolonged, natural exposure and practice with the device. This design allowed the researchers to track how perception evolved over time under sustained illusory conditions.

By controlling when and what participants saw of the physical proxy device, the study isolated the contributions of visual priming and prior knowledge to perceptual updating. The resulting dataset was used to derive and validate a first-order control system model of visuo-haptic sensory integration, capturing the cyclical, self-adjusting nature of perception over extended interaction.

## Results

Participants consistently overestimated the size of passive haptic objects over time, with drift following a curve toward a local asymptote. When an active shape-changing device shrank from 8 cm to 6 cm, perception drifted in the opposite direction, toward underestimation. Visual priming with the true device produced more accurate initial estimates and substantially reduced drift across the session. Misleading priming skewed perception toward the false size shown. Intermittent correct priming functioned as dead-reckoning, partially resetting perception at each reveal. These patterns were captured by a first-order control system model in which perceptive discrimination amplifies the sensory signal and feedback is weighted by confidence. The illusion threshold for grasping (approximately 17% JND for 6 cm objects reported in prior work) was shown to erode meaningfully over a one-hour session, with implications for the deployment of visuo-haptic illusions in prolonged VR interactions.


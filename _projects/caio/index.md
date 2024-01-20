---
title: CAIO
summary: Cognitive and Affective Interaction-Oriented
tags:
- reasoning
- caio
date: 'Apr 2015'
showthedate : false

# Optional external URL for project (replaces project detail page).
#external_link: http://example.org
links:
- icon: user
  icon_pack: fas
  name: Carole Adam
  url: http://magma.imag.fr/content/carole-adam

- icon: user
  icon_pack: fas
  name: Damien Pellier
  url: http://magma.imag.fr/content/damien-pellier

- icon: user
  icon_pack: fas
  name: Humbert Fiorino
  url: http://magma.imag.fr/content/humbert-fiorino 

- icon: user
  icon_pack: fas
  name: Sylvie Pesty
  url: http://magma.imag.fr/content/sylvie-pesty



image:
  caption: CAIO Architecture
  focal_point: Smart

# slides: caio_slides
---

One of my interests is to make robots able to autonomously sustain interactions with users, and in order to do
so, they have to be able to reason about the users’ and their environment. During my PhD, I have
been working on a Cognitive Architecture able to reason on Emotion, named CAIO (Cognitive and
Affective Interaction-Oriented) Architecture [3, 4]. This architecture, based on symbolic reasoning,
showed promising results in modeling cognitive processes and specifically allowing decision making
based on emotions. As shown in the figure, this architecture works as a two loops process, similar to the Dual-Process Theory - a deliberative loop generating intentions and a sensorimotor loop handling
reflexes.

More recently, we have been working on second order reasoning in the context of the
CoWriter project [5]. In the CoWriter project, the child’s teaches a Nao robot how to write. We use the
learning by teaching paradigm to enhance motivation and engagement. In a collaborative learning task
between a robot and a child, the idea is to model the child’s understanding and the child’s believes of the
understanding of the co-learner robot. This way the robot could detect misunderstandings in view to
correct them; or the robot could even create misunderstandings to enhance learning (by fostering
questioning).
Since my arrival on the CoWriter project, we initiated a project on diagnosis of dysgraphia using data collected
via a graphic tablet (Wacom). Our first results using RNN are very promising (a patent and a journal paper have
been submitted). This work will later on be integrated in the CoWriter handwriting activities to adapt the learning
path according to the diagnosis and the learner’s handwriting difficulties.
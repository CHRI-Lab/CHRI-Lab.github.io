---
title: Behavioural Analysis in HRI
summary: Understanding human actions, intentions is key
tags:
- affective computing
- cowriter
date: "2016-04-27T00:00:00Z"

# Optional external URL for project (replaces project detail page).
links:
- icon: user
  icon_pack: fas
  name: Dominique Vaufreydaz
  url: https://research.vaufreydaz.org/


image:
  caption: Photo by Dominique Vaufreydaz and Wafa Johal
  focal_point: Smart
---

In the field of human-robot interaction (HRI) as in many other technical fields, an innumerable number of different
metrics to analyze the interaction can be found in as many studies. Even-though many of these metrics are not

comparable between studies, we observe that the research community in HRI, but also in many other
research domain, is starting to seek for reproducibility [10]; a consensus begins to appear concerning
common measures that can be used across a wide range of studies. In social HRI, the evaluation of
the quality of an interaction is complex because it is very task dependent. However, certain metrics
such as engagement seem to well reflect the quality of interactions between a robot agent and the
human.

One aspect of acceptability of a robot is the home environment in which it is to be able to perceive when it will be
solicited. The goal for the robot is to not disturb the user and to be able to predict that it will be solicited. This is
something we do all the time as humans (we can see a street vendor approaching us and we know they will talk
to us). The process for us human relies on proxemics (speed and angle of approach) but not only.

 
In my work on modeling engagement [11, 12], I used multi-modal data to train a SVM to detect engagement. We

collected data from various sensors embedded in the Kompai robot and reduced the number of crucial features
from 32 to 7. Interestingly shoulder orientation and position of the face in the image are among these crucial
features. If we transpose these features to what humans do, these features seem coherent with behavioral
analysis.
The previous model aimed to predict the engagement, but once the user is engaged, it is important to evaluate its
attitude and mood. Using the COST and HAART dataset, we trained a model to detect social touch. Together with
colleagues, we won the Social Touch Challenge at ICMI 2015 improving the gestures recognition from 60% accuracy
to 70% training a Random Forest Model. [13]
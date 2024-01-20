---
title: CoWriting Kazakh
summary: A social robot to help the transition from Cyrillic to Latin alphabet in Kazakhstan 
tags:
- cowriter
- handwriting
- cowriting_kazakh

date: "2016-04-27T00:00:00Z"

links:
- icon: user
  icon_pack: fas
  name: Anara Sandygulova
  url: https://research.nu.edu.kz/en/persons/anara-sandygulova

- icon: user
  icon_pack: fas
  name: Thibault Asselborn
  url: https://people.epfl.ch/thibault.asselborn?lang=en

- icon: user
  icon_pack: fas
  name: Pierre Dillenbourg
  url: https://people.epfl.ch/pierre.dillenbourg?lang=en

- icon: hand-holding-usd
  icon_pack: fas
  name: Funding Agency
  url: https://unige-leadinghouse.ch/projetsarchives/cowriting-kazakh/ 


---

# Project Summary

This research occurred in a special context where Kazakhstan’s recent decision to switch from Cyrillic to the Latin-based alphabet has resulted in challenges connected with teaching literacy, addressing a rare combination of research hypotheses and technical objectives about language learning. Teachers are not necessarily trained to teach the new alphabet, and this could result in a harder challenge for children with difficulties. Prior research studies in Human-Robot Interaction (HRI) have proposed the use of a robot to teach handwriting to children. Drawing on the Kazakhstani case, our study takes an interdisciplinary approach by bringing together smart solutions from robotics, computer vision areas and educational frameworks, language and cognitive studies that will benefit diverse groups of stakeholders. 
 

Relatively little is known about the transfer of writing skills across scripts and it is extremely difficult to isolate the role of motor skills in this transfer, as compared to other cognitive and linguistic skills. Since handwriting combines visual, language, and motor dimensions, neuroimaging does not provide a clear account of cerebral substrates of handwriting.  A recent change of policy in Kazakhstan gave us an opportunity to measure transfer, as the Latin-based Kazakh alphabet has not yet been introduced. With the aim to understand if the script change of the Kazakh language from Cyrillic to Latin would have an effect on handwriting performance of young children and potentially increase the number of children with learning disabilities such as dyslexia and dysgraphia, we investigated the transfer of handwriting skills (from Cyrillic to Latin) in primary school children. To this end, we conducted an analysis of children’s handwriting dynamic data in both scripts (acquired from 200 children aged 6-11 years old who were asked to write a short text on a digital tablet using its stylus) in order to identify if the number of years spent practicing Cyrillic has an effect on the quality of handwriting in the Latin alphabet. The results showed that some of the differences between the two scripts were constant across all grades. These differences thus reflect the intrinsic differences in the handwriting dynamics between the two alphabets. For instance, several features related to the pen pressure on the tablet are quite different.  Other features, however, revealed decreasing differences between the two scripts across grades. While we found that the quality of Cyrillic writing increased from grades 1 to 4, due to increased practice, we also found that the quality of the Latin writing increased as well, despite the fact that all of the pupils had the same absence of experience in writing in Latin. We can therefore interpret this improvement in Latin script as an indicator of the transfer of fine motor control skills from Cyrillic to Latin. This result is especially surprising given that one could instead hypothesize a negative transfer, i.e., that the finger controls automated for one alphabet would interfere with those required by the other alphabet. 
 
## Deliverables 

1) We proposed the first dataset for handwriting recognition of Cyrillic-based languages such as Kazakh and Russian, which is appropriate for the use by machine learning approaches. It contains 121,234 samples of 42 Cyrillic letters. The performance of Cyrillic-MNIST is evaluated using standard deep learning approaches and is compared to the Extended MNIST (EMNIST) dataset. The dataset is available at https://github.com/bolattleubayev/cmnist. This work is under review in Frontiers in Big Data journal. It was conducted in Kazakhstan. 
 

2) We implemented an autonomous social robot that would assist and motivate children in transition from the old Cyrillic alphabet to a new Latin alphabet. The hardware components of the system include a humanoid NAO robot and a tablet with a stylus. The software components of the CoWriting Kazakh system include: a) handwriting recognition of Cyrillic languages trained on over 120,000 samples of the Cyrillic-MNIST dataset; b) Learning by Demonstration (LbD) in robot font to dynamically adapt to each child's individual handwriting style where trajectories of human handwriting are collected in real time; c) Latin-to-Latin Learning by Teaching (LbT): a humanoid robot plays a unique social role and asks for help to learn Kazakh language but since it cannot read Cyrillic script, a child becomes robot's teacher who is committed to try her best to write the words in Latin so that the robot can read and learn Kazakh. Such an approach allows us to keep a child engaged in the learning process that we utilized in the experiment with 67 children. The system was submitted as a demonstration paper titled “CoWriting Kazakh: Learning a new script with a robot - Demonstration”. This demonstration got the “Best Demonstration” award at the prestigious HRI 2020 conference. This work was conducted in Kazakhstan.  

 


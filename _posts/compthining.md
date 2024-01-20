---
title: Working on a Computational Thinking application

# View.
#   1 = List
#   2 = Compact
#   3 = Card
view: 3
date: 2018-08-04

# Optional header image (relative to `static/img/` folder).
header:
  caption: ""
  image: ""




---
Computational Thinking, Kezako? Computational Thinking such a buzz word these days. I got more and more interested by CT when I saw that there was so much debate on its definition and utility to be taught in school. I recently submitted a proposal to get funding for a project dealing with CT but I will not say much more now as it is being reviewed. In July, we received the visit of my good friend Anara from Kazakhstan, who stayed at the lab for a month; just enough to design an experiment and start the development. To get some inspiration we browsed and got some great ideas from the CSunplugged website : https://csunplugged.org/en/ We chose to work on Sorting Networks.

If you are an CS engineer you are very familiar with the classical sorting algorithms such as Insertion Sort, Quick Sort and Bubble Sort (Obama’s favorite) but maybe less familiar with the Sorting Networks. Sorting is everywhere and you use sorting machines all the time, each time you do a Google search, as Google is sorting the search results for you to get the most relevant one on the top of the list. This sorting by relevance can be done in multiple ways. Sorting Networks is one of the ways that as the advantage of allowing for parallel processing of the sorting task. In sorting networks, the only operation applied is comparison. Each thread compares elements of the network two by two and tag them as the higher or lower element of the two. Sorting networks can hence be applied to any kind of element as long as they can be compared (numbers, letters, etc). Another advantage of Sorting Networks is that the number of operation (and hence the execution time of the sorting) can be calculated from the just knowing the number of elements to be sorted (the shape of the network is determined at that time also).   



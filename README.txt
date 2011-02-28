
Paranoid Debate is a game where a small group collaborates to produce a Fermi 
estimate, or an estimated number where algebraic models and estimates can be 
combined to produce a reasonable estimate of the value of interest.  

The paranoid part is that one or more members of the group (assigned randomly) 
gain points if the group's estimate is wrong.

Questions can be found from a variety of sources, including Wikipedia or the 
board game Wits & Wagers.

Random assignment can be generated using dice or playing cards.

The code here is intended to give scores for each player based on a text file 
with a record of a game.  

The file format and the scoring algorithms are still under development, but 
people are encouraged to use and modify this code to help refine the game into 
something that is truly useful for experimenting and practicing techniques for 
developing or disrupting group consensus over quantitative models.

For more on the subject, including links to discussions about game playing 
experiences see the wiki page on the game itself:
http://wiki.lesswrong.com/wiki/Paranoid_debating

Also, wikipedia has an article on Fermi estimation itself:
http://en.wikipedia.org/wiki/Fermi_problem

===========

The project contains a python script that parses and scores game records.

Two game records are included, an initial test script and a record from a game
that was attempted using a verbal understanding of how scoring *should* work
in theory, but which may not have been sensitive to the actual math used.

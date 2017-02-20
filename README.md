# MathSciNet_Graph
This program generates a co-authors network for a given author on the AMS [MathSciNet](http://www.ams.org/mathscinet/index.html), by pulling data from the website.

The function of interest is *make_net(u_id, u_name)* which takes a authors MR Author ID and their name. (Note the name requirment will be removed soon, so as just to require u_id.) This returns an adjacancy matrix for the social network of the author and plots the network. 

Example:
'''python
adj_matrix = make_net('Hurwitz, Adolf', 237054)
'''

**Note that this code generates the network by accessesing the MathSciNet webpage multiple times (if accesible on your network). Do not run it for long durations.**

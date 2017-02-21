# MathSciNet_Graph
This program generates a co-authors network for a given author on the AMS [MathSciNet](http://www.ams.org/mathscinet/index.html), by pulling data from the website.

The function of interest is *make_net(u_id)* where u_id is the author's MR Author ID. This prints the author's clustering coefficient, plots their social network and returns the adjacancy matrix for the network.

Example:
```python
adj_matrix = make_net(237054)
```

```
Generating Network for Hurwitz, Adolf
Scraping Courant, Richard
Scraping Hilbert, David1
Scraping Pólya, George
Scraping Hurwitz, Adolf
Clustering Coefficient for Hurwitz, Adolf, 0.3333333333333333
```

![Output](https://raw.githubusercontent.com/brian-regan/MathSciNet_Graph/master/example_fig.png)

**Note that this code generates the network by accessesing the MathSciNet webpage multiple times (if accesible on your network). Do not run it for long durations.**

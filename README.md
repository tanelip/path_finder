Based on cities (nodes), edges (roads) and weights (road altitudes) finds the path from start (1) to destination
by finding the path which is minimizing the maximum altitude of roads. 

Solution is based on creating Kruskal's Minimum Spanning Tree and using that to deliver the best path with Dijkstras algorithm.

Can be tested by cloning the repository, running python main.py and giving it a path to testdata.

For example: /testidatalarge/graph_ADS2018_1000.txt

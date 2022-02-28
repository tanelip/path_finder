import disjointSet as djs

class Graph:

    def __init__(self, numOfVertices): 
        self.V = numOfVertices
        self.graph = []
        self.nodes = []
        for x in range(1, numOfVertices + 1):
            self.nodes.append(x)
        self.MST = []

    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])

    # -- Sorts all edges according to weight, picks up smallest edge
    #  and uses disjoint set to determine if nodes belong to the same component--
    def kruskalAlgo(self):
        index, edges = 0, 0
        ds = djs.DisjointSet(self.nodes)
        self.graph = sorted(self.graph, key=lambda item: item[2])
        while edges < self.V - 1:
            try:
                s, d, w = self.graph[index]
            except IndexError:
                print("There is no path from source to destination")
                quit()
            index += 1
            x = ds.find(s)
            y = ds.find(d)
            if x != y:
                edges += 1
                self.MST.append([s, d, w])
                ds.union(x, y)

from kruskal import Graph as graph_kruskal
from dijkstra import dijkstra, get_path, Graph
import time


def main():

    # Read file input and remove unnecessary data
    path_to_file = input("Give path to file: ")
    array = []

    with open(path_to_file) as f:
        nodesNum, roadsNum = [int(x) for x in next(f).split()]
        for line in f:
            array.append([int(x) for x in line.split()])

    start = 1
    destination = array[len(array) - 1].pop(0)
    del array[len(array) - 1]

    # Start time
    start_time = time.perf_counter()

    # Initialize graph for Kruskal's algorithm to produce Minimun Spanning Tree
    MST_kruskal = graph_kruskal(nodesNum)

    for s, d, w in array:
        MST_kruskal.addEdge(s, d, w)

    MST_kruskal.kruskalAlgo()

    # Search best available path with lowest max altitude using Dijkstas algorithm and Kruskal's MST
    dijksta_graph = Graph()

    for s, d, w in MST_kruskal.MST:
        dijksta_graph.add_node(s, d)
        dijksta_graph.add_edge(s, d, w)

    predecessor = dijkstra(dijksta_graph.ajd_list, 1)
    path, altitude_max = get_path(predecessor, start, destination)

    # End time
    end_time = time.perf_counter() - start_time

    print(" Best path: ", path, "\n", "Lowest max altitude: ", altitude_max, "\n", "Time elapsed: ", end_time, "seconds")

main()
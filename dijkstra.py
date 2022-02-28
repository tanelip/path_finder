import sys

class Graph:
    def __init__(self):
        self.ajd_list = dict()

    def add_node(self, start, end):
        self.start = start
        self.end = end

        if self.start not in self.ajd_list:
            self.ajd_list[self.start] = []
        if self.end not in self.ajd_list:
            self.ajd_list[self.end] = []

    def add_edge(self, s, e, w):

        self.ajd_list[s].append([e, w])
        self.ajd_list[e].append([s, w])


def dijkstra(graph, start):

    unvisited = {}
    predecessor = {}

    for node in graph:
        unvisited[node] = sys.maxsize

    unvisited[start] = 0
    queue = [start]

    while queue:
        current = queue.pop(0)

        for neighbor in graph[current]:
            distance = unvisited[current] + neighbor[1]

            if distance < unvisited[neighbor[0]]:
                unvisited[neighbor[0]] = distance
                queue.append(neighbor[0])
                predecessor[neighbor[0]] = (current, neighbor[1])

    return predecessor



altitude_max = 0
path = []
def get_path(pred, start, end):

    goal = end
    path.append(goal)
    altitude_max = pred[goal][1]

    while goal != start:
        path.insert(0, pred[goal][0])
        if altitude_max < pred[goal][1]:
            altitude_max = pred[goal][1]
        goal = pred[goal][0]

    return path, altitude_max
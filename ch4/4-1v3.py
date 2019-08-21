#! /usr/bin/python3
import sys

class Node:
    def __init__(self, value, adjacent):
        self.value = value
        self.adjacent = adjacent
        self.visited = False
    def getAdjacent(self):
        return self.adjacent
    def setVisited(self, value):
        self.visited = value
    def getVisited(self):
        return self.visited

graph = { "a" : Node("a", ["b", "c"]),
          "b" : Node("b", ["c"]),
          "c" : Node("c", ["d", "f"]),
          "d" : Node("d", ["e"]),
          "e" : Node("e", ["c", "f"]),
          "f" : Node("f", ["a"]),
          "g" : Node("g", [])
        }

queue = []
def has_route(g, start, end):
    if start == end:
        return True
    queue = [graph[start]]
    graph[start].setVisited(True)
    while len(queue) > 0:
        node = graph[queue.pop(0)]
        for neighbor in node.getAdjacent():
            if neighbor == end:
                return True
            if graph[neighbor].getVisited:
                continue
            graph[neighbor].setVisited(True)
            queue.append(neighbor)
    return False

def main(argv):
    for key, node in graph.items():
        graph[key].setVisited(False)
    if has_route(graph, argv[1], argv[2]):
        print ("Has Route")
    else:
        print ("No Route")

if __name__ == "__main__":
    main(sys.argv)

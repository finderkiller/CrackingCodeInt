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
def has_route(g, start, end):
    if start == end:
        return True
    q = []
    g[start].setVisited(True)
    q.append(g[start])
    while(len(q) != 0):
        cur = q.pop(0)
        for adj in cur.getAdjacent():
            if g[adj].getVisited():
                continue
            if adj == end:
                return True
            else:
                g[adj].setVisited(True)
                q.append(g[adj])
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

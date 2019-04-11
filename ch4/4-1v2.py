#! /usr/local/bin/python3
import sys

class Node:
    def __init__(self, name, children):
        self.name = name
        self.children = children
        self.visited = False
    def getVisited(self):
        return self.visited
    def setVisited(self, visited):
        self.visited = visited
    def getChildren(self):
        return self.children

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
    queue = []
    g[start].setVisited(True)
    queue.append(g[start])
    while len(queue) != 0:
        node = queue.pop()
        for adj in node.getChildren():
            adj_node = g[adj]
            if adj_node.getVisited():
                continue
            if (adj_node.name == end):
                return True
            adj_node.setVisited(True)
            queue.append(adj_node)
    return False

def main(argv):
    if(has_route(graph, argv[1], argv[2])):
        print("has route")
    else:
        print("no route")


if __name__ == "__main__":
    main(sys.argv)
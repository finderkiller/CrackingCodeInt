#! /usr/local/bin/python3
import sys

UNVISITED = "unvisited"
VISITING = "visiting"
VISITED = "visited

projects = {
          "a" : Project2("a"),
          "b" : Project2("b"),
          "c" : Project2("c"),
          "d" : Project2("d"),
          "e" : Project2("e"),
          "f" : Project2("f")
        }

graph = { "a" : ["b", "c"],
          "b" : ["c"],
          "c" : ["d"],
          "d" : ["e"],
          "e" : [],
          "f" : []
        }

class Project2:
    def __init__(self, name):
        self.name = name
        self.state = UNVISITED
        self.children = []
    def getState(self):
        return self.state
    def setState(self, state):
        self.state = state
    def appendChild(self, child):
        self.children.append(child)
    def getChildren(self):
        return self.children

def doDFS(project, order):
    if (project.getState() == VISITIED):
        return True
    if (project.getState() == VISITING):
        return False
    
    project.setState(VISITING)
    for child in project.getChildren():
        if not doDFS(child, order):
            return False
    order.append(project)
    project.setState(VISITED)
    return True

def sol2_find_build_order_dfs(graph):
#init
    for key, value in graph.items():
        for child in value:
            projects[key].appendChild(projects[child])
    order = []
    for key, value in projects.items():
        if (value.getState() == UNVISITED):
            if not doDFS(value, order):
                return []
    order.reverse()
    return order

def main():
#    order = sol1_find_build_order(graph)
    order = sol2_find_build_order_dfs(graph)
    output = []
    if (len(order) != len(projects)):
        print("Error")
    else:
        for project in order:
            output.append(project.getName())
        print(output)

if __name__ == "__main__":
    main()
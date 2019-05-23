#! /usr/bin/python3
UNVISITED = "unvisited"
VISITING = "visiting"
VISITED = "visited"

class Project1:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.dependencies = 0
    def getName(self):
        return self.name
    def appendChild(self, child):
        self.children.append(child)
    def getChildren(self):
        return self.children
    def increaseDependencies(self):
        self.dependencies += 1
    def decreaseDependencies(self):
        self.dependencies -= 1
    def getNumDependencies(self):
        return self.dependencies

class Project2:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.state = UNVISITED
    def getName(self):
        return self.name
    def getState(self):
        return self.state
    def setState(self, state):
        self.state = state
    def appendChild(self, child):
        self.children.append(child)
    def getChildren(self):
        return self.children

# projects = {
#          "a" : Project1("a"),
#          "b" : Project1("b"),
#          "c" : Project1("c"),
#          "d" : Project1("d"),
#          "e" : Project1("e"),
#          "f" : Project1("f")
#        }

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

def sol2_find_build_order_dfs(graph):
    order = []
    #init
    for key, values in graph.items():
        for value in values:
            projects[key].appendChild(projects[value])

    for key, value in projects.items():
        if value.getState() == UNVISITED:
            if not doDFS(value, order):
                return []
    order.reverse()
    return order

def doDFS(project, order):
    if project.getState() == VISITING:
        return False
    if project.getState() == VISITED:               #if visit a visited node, return true
        return True

    project.setState(VISITING)
    for child in project.getChildren():
        if not doDFS(child, order):
            return False
    project.setState(VISITED)
    order.append(project)
    return True


#kind of BFS, traverse child first and put child into order
# time: O(P+D), P is the number of nodes, and D is the number of the dependencies
def sol1_find_build_order(graph):
    # init
    for key, values in graph.items():
        for value in values:
            projects[key].appendChild(projects[value])
            projects[value].increaseDependencies()

    order = []
    ret = []
    project_list = []
    for key, project in projects.items():
        project_list.append(project)

    add_non_depend_project(project_list, order)
#     toBeProcessed = 0
#     while (toBeProcessed < len(order)):
    while(len(order) != 0):
#         current = order[toBeProcessed]
#         if current == None:         # no independent project, there is circle
#             return []
        current = order.pop(0)
        ret.append(current)
        for child in current.getChildren():
            child.decreaseDependencies()
        add_non_depend_project(current.getChildren(), order)
#         toBeProcessed += 1
#     return order
    return ret

def add_non_depend_project(project_list, order):
    for project in project_list:
        if project.getNumDependencies() == 0:
            order.append(project)

def main():
#     order = sol1_find_build_order(graph)
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

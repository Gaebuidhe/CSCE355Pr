# modified DFS Code from https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
# Creator Neelam Yadav
# https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
# Creator Divyanshu Mehta
import sys

class Dfs:
    global graph # stores the dfa Transition tables as a directed graph
    global dfsString #output string for dfs
    global accepting


    # initiates dfs with the searching graph
    def __init__(self, ngraph, naccepting):
        self.graph = ngraph
        self.accepting = naccepting

    # A function used by DFS
    def DFSUtil(self,vis,x):

        #creates string to test accepting
        self.dfsString.append(x)
        vis[x]= True

        for i in self.graph[x]:
            if vis[i] == False:
                self.DFSUtil(vis, i)


    def DFS(self,x):

        # empties the string for new values
        self.dfsString = []
        vis = [False]*(len(self.graph))

        # starts depth first search from point x,
        # for start state in dfa this will be 0
        self.DFSUtil(vis, x)
        return self.dfsString

    def isCyclicUtil(self, v, vis, recStack):

        # Mark current node as vis and
        # adds to recursion stack
        vis[v] = True
        recStack[v] = True

        # checks for cycle checks if cycle has point in accepting
        for n in self.graph[v]:
            if vis[n] == False:
                if self.isCyclicUtil(n, vis, recStack) == True:
                    for i in range(0,len(self.accepting)):
                        if self.accepting[i] in self.DFS(v):
                            return True
            elif recStack[n] == True:
                for i in range(0,len(self.accepting)):
                    if self.accepting[i] in self.DFS(n):
                        return True

        # Node popped, returns false, moves on to next node
        recStack[v] = False
        return False

    # Returns true if graph is cyclic and cycle reaches a final state
    def isCyclic(self):
        vis = [False] * (len(self.graph))
        recStack = [False] * (len(self.graph))
        for node in range((len(self.graph))):
            if vis[node] == False:
                if self.isCyclicUtil(node,vis,recStack) == True:
                    return True
        return False

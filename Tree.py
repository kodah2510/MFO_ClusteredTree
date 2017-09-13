from GlobalVariables import *
import random
class Tree:
    edge_set = []
    def mutate(self):
        global edges
        #find edges not in this edge_set
        notAddedEdges = []
        notAddedEdges.extend(edge for edge in edges if edge not in self.edge_set)

        e_idx = random.randrange(len(notAddedEdges))
        newEdge = notAddedEdges[e_idx]
        self.edge_set.append(newEdge) # this will create a cycle
        #convert to adjlist
        adjList = []
        for e in self.edge_set:
            adjList.insert(e.vertices[0].name, e.vertices[1].name)
            adjList.insert(e.vertices[1].name, e.vertices[0].name)

        #find the cycle
        cycle = self.findCycle(adjList, newEdge.vertices[0].name, newEdge.vertices[1].name)
        #pick a random edge from that cycle
        r_idx = random.randrange(len(cycle)) # remove_edge_index
        remove_edge = cycle[r_idx]
        self.edge_set.remove(remove_edge)
        pass
    def findCycle(self, adjList, src, dst):
        history = []
        visited = []
        for i in range(0, len(adjList)):
            visited.append(False)
        cycle = []
        stack = []
        v = src 
        stack.append(v)
        while(len(stack) != 0):
            v = stack.pop()
            if not visited[v]:
                visited[v] = True
                history.append(v)
                stack.extend(adjList[v])   
            else:
                if(len(history) - history.index(v) > 3): #len(history) - history(index) - 1 > 2 
                    history.append(v)
                    for i in range(0, len(history)):
                        for j in range (i, len(history)):
                            if history[i] in adjList(history[j]):
                                cycle.append(history[i])
                                break
                    break

        res = []
        for i in range(0, len(cycle), 2):
            for e in self.edge_set:
                names = []
                names.append(e.vertices[0].name)
                names.append(e.vertices[1].name)
                if(cycle[i] in names and cycles[i + 1] in names):
                    res.append(e)
        return res
        pass
    def addEdges(self, edges):
        self.edge_set.extend(edges)
        pass

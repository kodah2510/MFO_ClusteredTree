#from setting import edges
import random
import setting as gv
import adjlist as adj
class Tree:
    #edge_set = []
    def __init__(self) :
        self.edge_set = []
    def mutate(self):

        # split the tree into clusters
        # find not added edges
        #  
        #print("mutate")
        #find edges not in this edge_set
        notAddedEdges = []
        notAddedEdges.extend(edge for edge in gv.edges if edge not in self.edge_set)

        e_idx = random.randrange(len(notAddedEdges) - 1)
        newEdge = notAddedEdges[e_idx]
        self.edge_set.append(newEdge) # this will create a cycle
        #convert to adjlist
        adjlist = []
        adjlist = adj.transform(self.edge_set)
        # for e in self.edge_set:
        #     adjlist.insert(e.vertices[0].name, e.vertices[1].name)
        #     adjlist.insert(e.vertices[1].name, e.vertices[0].name)

        #find the cycle
        cycle = self.findCycle(adjlist, newEdge.vertices[0].name, newEdge.vertices[1].name)
        #pick a random edge from that cycle
        r_idx = random.randrange(len(cycle)) # remove_edge_index
        remove_edge = cycle[r_idx]
        self.edge_set.remove(remove_edge)
        pass
    def findCycle(self, adjlist, src, dst):
        stack = []
        cycle = []
        visited = []
        parent = []
        for i in range(0, len(adjlist)):
            parent.append(-1)
            visited.append(False)
        stack.append(src)
        #prev = -1
        while len(stack) != 0:
            u = stack.pop()
            if not visited[u]:
                visited[u] = True
                if u == src:
                    for v in adjlist[u]:
                        if v != dst:
                            if not visited[v]:
                                stack.append(v)
                                parent[v] = u
                else:
                    for v in adjlist[u]:
                        if not visited[v]:
                            stack.append(v)
                            parent[v] = u
                   
        
        cycle = []
        track = dst
        while track != src:
            cycle.append(track)
            track = parent[track]
        cycle.append(src)
        #print(cycle)
            #prev = u
        # history = []
        # visited = []
        # for i in range(0, len(adjlist)):
        #     visited.append(False)
        # cycle = []
        # stack = []
        # v = src 
        # stack.append(v)
        # while(len(stack) != 0):
        #     v = stack.pop()
        #     if not visited[v]:
        #         visited[v] = True
        #         history.append(v)
        #         stack.extend(adjlist[v])   
        #     else:
        #         if(len(history) - history.index(v) > 3): #len(history) - history(index) - 1 > 2 
        #             history.append(v)
        #             for i in range(0, len(history)):
        #                 for j in range (i, len(history)):
        #                     count = 0
        #                     if history[i] in adjlist[history[j]]:
        #                         if count == 1:
        #                         cycle.append(history[i])
        #                     count += 1
        #                         break
        #             break

        res = []
        for i in range(0, len(cycle) - 1, 2):
            for e in self.edge_set:
                names = []
                names.append(e.vertices[0].name)
                names.append(e.vertices[1].name)
                if(cycle[i] in names and cycle[i + 1] in names):
                    res.append(e)
        return res
        pass
    def addEdges(self, edges):
        self.edge_set.extend(edges)
        pass

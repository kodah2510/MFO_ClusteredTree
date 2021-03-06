#from setting import edges
import random
import setting as gv
import adjlist as adj
from collections import deque
import shutil
class Tree:
    #edge_set = []
    def __init__(self) :
        self.edge_set = []
    def mutate(self):
        print("mutate")
        gv.mutateCount += 1
        _id = random.randrange(1000)
        # split the tree into clusters
        # find not added edges
        #  
        #print("mutate")
        #find edges not in this edge_set

        adjlist = []
        adjlist = adj.transform(self.edge_set)
        self.printTree(adjlist, 1)
        #choose a cluster
        cluster_rIdx = random.randrange(len(gv.clusters) - 1)
        while len(gv.clusters[cluster_rIdx].edges) < 3:
            cluster_rIdx = random.randrange(len(gv.clusters))
        mutateCluster = gv.clusters[cluster_rIdx]
        notAddedEdges = []
        notAddedEdges.extend(edge for edge in mutateCluster.edges if edge not in self.edge_set)
        #choose an edge to add
        try:
            e_idx = random.randrange(len(notAddedEdges))
            # while notAddedEdges[e_idx] not in mutateCluster.edges: 
            #     e_idx = random.randrange(len(notAddedEdges) - 1)
            newEdge = notAddedEdges[e_idx]
            self.edge_set.append(newEdge) # this will create a cycle
            #convert to adjlist
            # adjlist = []
            # adjlist = adj.transform(self.edge_set)
           
            # for e in self.edge_set:
            #     adjlist.insert(e.vertices[0].name, e.vertices[1].name)
            #     adjlist.insert(e.vertices[1].name, e.vertices[0].name)

            #find the cycle
            cycle = self.findCycle(adjlist, newEdge.vertices[0].name, newEdge.vertices[1].name)
            #pick a random edge from that cycle

            candidates_for_execution = []
            for e in cycle: 
                if e in mutateCluster.edges:
                    candidates_for_execution.append(e)
            if len(candidates_for_execution) == 1:
                self.edge_set.remove(candidates_for_execution[0])
            elif len(candidates_for_execution) > 1:
                r_idx = random.randrange(len(candidates_for_execution) - 1) # remove_edge_index
                remove_edge = candidates_for_execution[r_idx]
                self.edge_set.remove(remove_edge)
            else: 
                r_idx = random.randrange(len(cycle) - 1) # remove_edge_index
                remove_edge = cycle[r_idx]
                self.edge_set.remove(remove_edge)
            adjlist = []
            adjlist = adj.transform(self.edge_set)
            self.printTree(adjlist, 2)
        except ValueError:
            #print(len(notAddedEdges))
            print(gv.currentGen)

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
    def printTree(self, adjlist, ver):
        file = open('tree.txt','w')
        for i in range(0, len(adjlist)):
            file.write( str(gv.nodes[i].name) + ' ' + 
                        str(gv.nodes[i].x) + ' ' + 
                        str(gv.nodes[i].y) + ' ' +
                        str(gv.nodes[i].cluster) + 
                        '\n')
            
        
        #BFS traverse
        prev = []
        for i in range(0, len(adjlist)):
            prev.append(-1)
        S = []
        Q = deque()
        S.append(gv.srcIndex)
        Q.append(gv.srcIndex)
        while len(Q) != 0:
            u = Q.popleft()
            for v in adjlist[u]:
                if v not in S:
                    prev[v] = u
                    S.append(v)
                    Q.append(v)

        for v in prev: 
            file.write(str(v) + ' ')

        file.close()  
        shutil.move("./tree.txt", "./Processing/tree" + str(ver)+".txt")      
        pass
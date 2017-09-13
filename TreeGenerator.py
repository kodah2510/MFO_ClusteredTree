from random import randrange
from Node import Node
from Edge import Edge
class TreeGenerator:
    def primRST(self, nodes, edges):
        T = []
        s_idx = randrange(len(nodes))
        s = nodes[s_idx]
        C = []
        C.append(s)
        A = []
        A = self.findEligibleEdges(s, edges)
        temp = s
        while(len(C) != len(nodes)):
            if(len(A) == 0): 
                break
            e_idx = randrange(len(A))
            uv = A[e_idx]
            A.pop(e_idx)
            v = uv.findAnother(temp)
            if((v not in C)):
                T.append(uv)
                C.append(v)
                A.extend(self.findEligibleEdges(v, edges))
                temp = v
        return T
        pass    
    def bridgeGen(self, clusters, bridgeSet):
        #each cluster is seem as a node
        nodes = []
        for i in range(0, len(clusters)):
            newNode = Node(i, 0, 0)
            nodes.append(newNode)
        # edges
        edges = []
        for i in range(0, len(nodes) - 1):
            for j in range(i + 1, len(nodes)):
                newEdge = Edge(nodes[i], nodes[j])
                edges.append(newEdge)
        tree = self.primRST(nodes, edges)

        res = []
        for e in tree:
            for bridge in bridgeSet:
                if(e.vertices[0].name in bridge.clusters and e.vertices[1].name in bridge.clusters):
                    e_idx = randrange(len(bridge.edges))
                    res.append(bridge.edge_set[e_idx])
        return res
        pass
    def findEligibleEdges(self, node, edges):
        res = []
        for e in edges:
            if(e.hasNode(node)): 
                res.append(e)
        return res
        pass
    
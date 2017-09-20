class Bridge:
    def __init__(self, i, j):
        self.edge_set = []
        self.clusters = []
        self.clusters.extend([i, j])
        pass
    def isMatched(self, i, j):
        return (i in self.clusters and j in self.clusters)
        pass
    def addEdge(self, edge):
        self.edge_set.append(edge)
        pass
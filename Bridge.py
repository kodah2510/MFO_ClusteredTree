class Bridge:
    edge_set = []
    clusters = []
    def __init__(self, i, j):
        clusters.append(i)
        clusters.append(j)
        pass
    def isMatch(self, i, j):
        if(i in clusters and j in clusters) return True
        return False
        pass
    def addEdge(self, edge):
        edge_set.append(edge)
        pass
class Cluster:
    def __init__(self, name, vertices):
        self.vertices = []
        self.edges = []
        self.name = name
        for val in vertices:
            self.vertices.append(int(val))
        pass
    def addEdge(self, edge):
        self.edges.append(edge)
        pass    
    
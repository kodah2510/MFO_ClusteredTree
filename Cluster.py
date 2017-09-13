class Cluster:
    vertices = []
    edges = []
    def __init__(self, name, vertices):
        self.name = name
        for val in vertices:
            self.vertices.append(int(val))
        pass
    def addEdge(self, edge):
        edges.append(edge)
        pass    
    
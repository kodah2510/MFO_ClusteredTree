class Edge:
    vertices = []
    def __init__(self, a, b):
        self.vertices.extend([a, b])
        pass
    def getWeight(self):
        x1 = vertices[0].x
        x2 = vertices[1].x
        y1 = vertices[0].y
        y2 = vertices[1].y
        x1_sub_x2 = x1 - x2
        y1_sub_y2 = y1 - y2
        return x1_sub_x2 * x1_sub_x2 + y1_sub_y2 * y1_sub_y2
        pass
    def findAnother(self, node):
        for v in self.vertices:
            if(v != node): 
                return v
        return
    def hasNode(self, v):
        return v in self.vertices
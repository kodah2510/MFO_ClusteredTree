from GlobalVariables import * 

class Task:
    def __init__(self):
        self.rank = 0
        self.factorial_cost = 0
        self.objectiveValue = 0
        self.violationConstrain = 0
        pass

class SubTask(Task):
    def computeCost(self, edge_set):
        res = 0
        for e in edge_set:
            res += e.getWeight() 
        return res
        pass

class MainTask(Task):
    def computeCost(self, edge_set):
        global sourceIndex, nodes
        sourceVertex = nodes[sourceIndex]

        pass
        
from Tree import Tree
from GlobalVariables import *

class Individual:
    tree = Tree()
    scalarFitness = -1
    skillFactor = -1
    tasks = []
    def __init__(self, nodes, edges):
        global treeGen, clusters, bridgeSet
        for clus in clusters:
            clus_nodes = []
            for node_idx in clus.vertices:
                clus_nodes.append(nodes[node_idx])
            res = treeGen.primRST(clus_nodes, clus.edges)
            self.tree.addEdges(res)
        bridges = treeGen.bridgeGen(clusters, bridgeSet)
        self.tree.addEdges(bridges)

        #self.tasks = tasks[:]
        pass
    def mutate(self):
        self.tree.mutate()
    def updateSkillFactor(self):
        minTask = min(self.tasks, key=lambda task: task.rank)
        self.skillFactor = self.tasks.index(minTask)
        pass
    def updateScalarFitness(self):
        minTask = min(self.tasks, key=lambda task: task.rank)
        self.scalarFitness = 1 / minTask.rank
        pass
    def eval(self):
        for t in self.tasks:
            t.computeCost(self.tree.edge_set)
        pass
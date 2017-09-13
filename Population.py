from Individual import Individual
from GlobalVariables 
import random
rmp = 0.3
class Population:
    individuals = []
    def __init__(self, tasks):
        global POPULATION
        for i in range(0, POPULATION):
            idv = Individual(tasks)
            self.individuals.append(idv)
    def update():
        # sort the population

        # delete the 
        pass
    def eval(self):
        for idv in self.individuals:
            idv.eval()
        pass
    def assortativeMating(self):
        pa_idx = random.randrange(len(self.individuals))
        pb_idx = -1
        while pb_idx < 0 or pb_idx == pa_idx:
            pb_idx = random.randrange(len(self.individuals))

        pa = self.individuals[pa_idx]
        pb = self.individuals[pb_idx]
        rand = random.uniform(0, 1)
        if(pa.skillFactor == pb.skillFactor) or (rand < rmp):
            self.__crossover(pa, pb)
        else:
            pa.mutate()
            pb.mutate()
            pass
        pass
    def __setSkillFactorForOffSpring(self, child, pa, pb):
        rand = random.uniform(0, 1)
        if(rand < 0.5):
            child.skillFactor = pa.skillFactor
        else:
            child.skillFactor = pb.skillFactor
        pass
    def __crossover(self, pa, pb):
        global nodes
        combinedEdges = []
        combinedEdges = self.__combine(pa, pb)
        ca = Individual(nodes, combinedEdges)
        cb = Individual(nodes, combinedEdges)
        self.__setSkillFactorForOffSpring(ca, pa, pb)
        self.__setSkillFactorForOffSpring(cb, pa, pb)
        pass
    def __combine(self, pa, pb):
        distinctEdges = pa.tree.edge_set
        distinctEdges.extend(edge for edge in pb.tree.edge_set if edge not in pa.tree.edge_set)
        return distinctEdges
        pass
    def ranking(self):
        global POPULATION
        for i in range(0, len(self.individuals[0].tasks)): 
            sorted(self.individuals, key=lambda idv.tasks[i]: idv.tasks[i].factorialCost)
            for j in range(0, POPULATION):
                self.individuals[j].tasks[i] = j
        pass
    def updateSkillFactor(self):
        for idv in self.individuals:
            idv.updateSkillFactor()
        pass
    def updateScalarFitness(self):
        for idv in self.individuals:
            idv.updateScalarFitness()
        pass
    
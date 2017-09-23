import setting as gv
from Individual import Individual
import random
rmp = 0.3
class Population:
    individuals = []
    def __init__(self):
        for i in range(0, gv.POPULATION):
            print("Initialize " + "individual " + str(i))
            idv = Individual(gv.tasks, gv.nodes, gv.edges)
            self.individuals.append(idv)
            
    def update(self):
        # sort the population
        self.individuals = sorted(self.individuals, key=lambda idv: idv.scalarFitness)
        # delete 
        for i in range(0, len(self.individuals) - gv.POPULATION):
            self.individuals.pop(i)
        pass
    def eval(self):
        for idv in self.individuals:
            for t in range(0, len(idv.tasks)):
                idv.eval(t)
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
            pa.eval(pa.skillFactor)
            pb.mutate()
            pb.eval(pb.skillFactor)
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
        combinedEdges = []
        combinedEdges = self.__combine(pa, pb)
        ca = Individual(gv.tasks, gv.nodes, combinedEdges)
        cb = Individual(gv.tasks, gv.nodes, combinedEdges)
        self.__setSkillFactorForOffSpring(ca, pa, pb)
        self.__setSkillFactorForOffSpring(cb, pa, pb)

        # ca.eval(ca.skillFactor)
        # cb.eval(cb.skillFactor)

        ca.eval(0)
        ca.eval(1)

        cb.eval(0)
        cb.eval(1)
        self.individuals.append(ca)
        self.individuals.append(cb)

        pass
    def __combine(self, pa, pb):
        distinctEdges = pa.tree.edge_set
        distinctEdges.extend(edge for edge in pb.tree.edge_set if edge not in pa.tree.edge_set)
        return distinctEdges
        pass
    def ranking(self):
        #print("ranking...")
        for i in range(0, len(self.individuals[0].tasks)): 
            self.individuals = sorted(self.individuals, key=lambda idv: idv.tasks[i].factorialCost)
            for j in range(0, len(self.individuals)):
                self.individuals[j].tasks[i].rank = j + 1   
        # for idv in self.individuals:
        #     print(str(idv.tasks[0].rank) + " " + str(idv.tasks[1].rank))
        pass
    def updateSkillFactor(self):
        #print("update skill factor ...")
        for idv in self.individuals:
            idv.updateSkillFactor()
        pass
    def updateScalarFitness(self):
        #print("update scalar fitness ...")
        try:
            for idv in self.individuals:
                idv.updateScalarFitness()
        except ZeroDivisionError as err:
            print(err)
            pass
        pass
    def printTheBest(self):
        tmp = max(self.individuals, key=lambda idv: idv.scalarFitness)
        res = str(tmp.tasks[0].factorialCost) + " " + str(tmp.tasks[1].factorialCost)
        print(res)
        return res
        pass
    
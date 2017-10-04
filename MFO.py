from Individual import Individual
from Population import Population
from InputHandler import InputHandler
from TreeGenerator import TreeGenerator
import setting as gv
from Task import * 
from Edge import Edge
from Bridge import Bridge
#from matplotlib import pyplot as plt


def main():
    #read input
    inputLink = "Data/4Eil10.clt"
    inputHandler = InputHandler()
    inputHandler.readInput(inputLink)
    inputFileName = inputLink.replace('Data/', '_')
    inputFileName = inputLink.replace('Data/', '')
    #print(nodes)
    #print(clusters)
    #initialize bridgeset
    for i in range(0, len(gv.clusters) - 1):
        for j in range(i + 1, len(gv.clusters)):
            bridge = Bridge(i, j)
            gv.bridgeSet.append(bridge)
    #set cluster for each node
    for i in range(0, len(gv.clusters)):
        for j in range(0 , len(gv.clusters[i].vertices)):
            nodeName = gv.clusters[i].vertices[j]
            gv.nodes[nodeName].setCluster(i)
        
    #initialize edges
    for i in range(0, len(gv.nodes) - 1):
        for j in range(i + 1, len(gv.nodes)):
            newEdge = Edge(gv.nodes[i], gv.nodes[j])
            gv.edges.append(newEdge)            
            if(gv.nodes[i].cluster != gv.nodes[j].cluster):
                for k in range(0, len(gv.bridgeSet)):
                    if(gv.bridgeSet[k].isMatched(gv.nodes[i].cluster, gv.nodes[j].cluster)):
                        gv.bridgeSet[k].addEdge(newEdge)
            else:
                gv.clusters[gv.nodes[i].cluster].addEdge(newEdge)
                pass
            newEdge = None
    # for e in edges: 
    #     print(str(e.vertices[0].name) + " " + str(e.vertices[1].name))
    # assign tasks 
    mainTask = MainTask()
    subTask = SubTask()
    gv.tasks.append(mainTask)
    gv.tasks.append(subTask)

    # x = []
    # y = []
    # for n in gv.nodes:
    #     x.append(n.x)
    #     y.append(n.y)
    # plt.scatter(x, y)
    # plt.show()

    # idv = Individual(tasks, gv.nodes, gv.edges)
    # idv.eval(0)
    outputFile = open('output.txt', 'w')
    #STEP 1: Initialize population
    pop = Population()

    # for idv in pop.individuals:
    #     print(idv.tree.edge_set)
    #print(pop.individuals[-1].tree.edge_set)
    #STEP 2: Evaluating
    pop.eval()
    pop.ranking()
    #STEP 3: update scalar fitness and skill factor
    pop.updateScalarFitness()
    pop.updateSkillFactor()
   
    while(gv.currentGen != gv.MAX_GEN):
        #print("cur gen " + str(currentGen))
        #STEP 4: combination and mutation 
        pop.assortativeMating()
        #STEP 4.1: re-calculating the fitness and skill factor
        pop.ranking()
        pop.updateScalarFitness()
        pop.updateSkillFactor()
        pop.update()
        outputFile.write(pop.printTheBest() + "\n")
        gv.currentGen += 1
        pass
    outputFile.close()
    import shutil
    import random
    idNumber = random.randrange(1000)
    shutil.move("./output.txt", "./Output/output"+"_"+ str(idNumber)+"_"+inputFileName+".txt")
    print(gv.mutateCount)
    pass
if __name__=="__main__":
    #setting.init()
    main()
    
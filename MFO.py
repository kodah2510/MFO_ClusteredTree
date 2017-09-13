from GlobalVariables import *
from Individual import Individual
from InputHandler import InputHandler
from TreeGenerator import TreeGenerator

def main():
    #global nodes, clusters, edges, bridgeSet
    #read input
    inputHandler = InputHandler()
    inputHandler.readInput('Data/3eil51.clt')
    #initialize bridgeset
    for i in range(0, numberOfCluster - 1):
        for j in range(i + 1, numberOfCluster):
            bridge = Bridge(i , j)
            bridgeSet.append(bridge)
    #set cluster for each node
    for i in range(0, numberOfCluster):
        for j in range(0 ,clusters[i].vertices.len()):
            nodeName = clusters[i].vertices[i]
            nodes[nodeName].setCluster(i)
        
    #initialize edges
    for i in range(0, dim - 1):
        for j in range(i + 1, dim):
            newEdge = Edge(nodes[i], nodes[j])
            if(nodes[i].cluster != nodes[j].cluster):
                for k in range(0, bridgeSet.len()):
                    if(bridgeSet[k].isMatched(i, j)):
                        bridgeSet[k].addEdge(newEdge)
            else:
                clusters[nodes[i].cluster].addEdge(newEdge)
                pass
            edges.append(newEdge)

    #idv = Individual()
    pop = Population()
    pop.eval()
    pop.ranking()
    pop.updateScalarFitness()
    pop.updateSkillFactor()
    currentGen = 0`
    while(currentGen != MAX_GEN):
        pop.assortativeMating()
        pop.eval()
        pop.update()
        currentGen += 1
if __name__=="__main__":
    main()
    
from Node import Node
from Cluster import Cluster
from GlobalVariables import *
class InputHandler:
    def __init__(self):
        pass
    def readInput(self, link):
        global clusters, nodes, numberOfCluster, sourceIndex, dim
        f = open(link, 'r')
        nextline = f.readline()
        while(nextline.find("DIMENSION") == -1):
            nextline = f.readline()
        tmp = nextline.split(" ")
        dim = int(tmp[1])
        
        nextline = f.readline()
        tmp = nextline.split(" ")
        numberOfCluster = int(tmp[1])

        while(nextline != "NODE_COORD_SECTION\n"):
            nextline = f.readline()
        nextline = f.readline()
       
        while(nextline != "CLUSTER_SECTION:\n"):
            tmp = nextline.split(" ")
            node = Node(int(tmp[0]) - 1, int(tmp[1]), int(tmp[2]))
            nodes.append(node)
            nextline = f.readline()

        while(nextline.find("SOURCE_VERTEX") == -1):
            nextline = f.readline()
        
        tmp = nextline.split(" ")
        sourceIndex = int(tmp[1])
        nextline = f.readline()
        while(nextline != "EOF\n"):
            tmp = nextline.split(" ")
            cluster = Cluster(int(tmp[0]) - 1, tmp[1:])
            clusters.append(cluster)
            nextline = f.readline()
        f.close()   
        pass

# if __name__=="__main__":
#     i = InputHandler()
#     i.readInput('Data/3eil51.clt')
    
    #print(nodes)
    #print(sourceIndex)

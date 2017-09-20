from Node import Node
from Cluster import Cluster
import setting as gv
class InputHandler:
    def __init__(self):
        pass
    def readInput(self, link):
        f = open(link, 'r')
        nextline = f.readline()
        while(nextline.find("DIMENSION") == -1):
            nextline = f.readline()
        tmp = nextline.split(" ")
        
        gv.dim = int(tmp[1])
        
        nextline = f.readline()
        tmp = nextline.split(" ")
        gv.numberOfCluster = int(tmp[1])

        while(nextline != "NODE_COORD_SECTION\n"):
            nextline = f.readline()
        nextline = f.readline()
       
        while(nextline != "CLUSTER_SECTION:\n"):
            tmp = nextline.split(" ")
            node = Node(int(tmp[0]) - 1, int(tmp[1]), int(tmp[2]))
            gv.nodes.append(node)
            nextline = f.readline()

        while(nextline.find("SOURCE_VERTEX") == -1):
            nextline = f.readline()
        
        tmp = nextline.split(" ")
        gv.srcIndex = int(tmp[1])
        nextline = f.readline()
        while(nextline != "EOF\n"):
            tmp = nextline.split(" ")
            cluster = Cluster(int(tmp[0]) - 1, tmp[1:-1])
            gv.clusters.append(cluster)
            nextline = f.readline()
        f.close()   
        print("srcIndex " + str(gv.srcIndex))
        pass
# if __name__=="__main__":
#     i = InputHandler()
#     i.readInput('Data/3eil51.clt')
    
    #print(nodes)
    #print(sourceIndex)

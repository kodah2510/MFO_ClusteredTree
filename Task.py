import setting as gv
import math
from adjlist import transform
from collections import deque
class Task:
    def __init__(self):
        self.rank = 0
        self.factorialCost = math.inf
        self.objectiveValue = 0
        self.violationConstrain = 0
        pass

class SubTask(Task):
    def computeCost(self, edge_set):
        res = 0
        for e in edge_set:
            res += e.weight
        self.factorialCost = res
        pass

class MainTask(Task):
    def computeCost(self, edge_set):
        #print(edge_set)
        # need adjlist transform
        #BFS
        adjlist = []
        adjlist = transform(edge_set)
        S = []
        Q = deque()
        dist = []
        for i in range(0, len(gv.nodes)):
            dist.append(math.inf)
        dist[gv.srcIndex] = 0
        S.append(gv.srcIndex)
        Q.append(gv.srcIndex)

        while len(Q) != 0:
            u = Q.popleft()
            for v in adjlist[u]:
                if v not in S:
                    alt = dist[u] + self.length(u, v, edge_set)
                    if alt < dist[v]:
                        dist[v] = alt 
                    S.append(v)
                    Q.append(v)
        res = 0
        for val in dist:
            res += val
        # print(dist)
        # print("res " +str(res))
        self.factorialCost = res
        pass
    def getCost(self, src, dst, adjlist, edge_set):
        stack = []
        stack.append(src)
        visited = []
        path = []
        history = []
        for i in range(0, len(adjlist)):
            visited.append(False)
        while(len(stack) != 0):
            u = stack.pop()
            if u == dst: 
                for i in range(0, len(history)):
                    for j in range (i, len(history)):
                        if history[i] in adjlist[history[j]]:
                            path.append(history[i])
                            break
                break
            if not visited[u]:
                history.append(u)
                visited[u] = True
                stack.extend(adjlist[u])
        #print(path)
        res = 0
        for i in range(0, len(path)):
            res += self.length(path[i], path[i + 1], edge_set)
        return res
        pass
    def length(self, u, v, edge_set):
        for e in edge_set: 
            name = []
            name.extend([e.vertices[0].name, e.vertices[1].name])
            if (u in name and v in name):
                return e.weight
        pass
    def getNext(self, Q, dist):
        tmp = list(dist)
        node = tmp.index(min(tmp))
        while node not in Q: 
            # print(node)
            # print(tmp)
            tmp.pop(node)
            node = tmp.index(min(tmp))
        return node
        pass
        
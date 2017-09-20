def transform(edge_set):
    adjlist = []
    nodeSet = []
 
    #need to re-examine
    for e in edge_set:
        for n in e.vertices:
            if n.name not in nodeSet:
                nodeSet.append(n.name)
    for i in range(0, len(nodeSet)):
        tmp = []
        adjlist.append(tmp)

    for e in edge_set:
        adjlist[e.vertices[0].name].append(e.vertices[1].name)
        adjlist[e.vertices[1].name].append(e.vertices[0].name)

    #print(adjlist)
    return adjlist
    pass

import rhino3dm as rg
import networkx as nx
import random

def createGridGraph():

    G = nx.star_graph(20)
    G.add_nodes_from([20,21])
    G.add_edges_from([(19,20), (20,6), (8,16), (16,21)])
    return G

def addRandomWeigths(G):

    NG = nx.Graph()
    for u,v,data in G.edges(data=True):
        #w = data['weight'] if 'weight' in data else 1.0
        w = random.randint(1,10)
        if NG.has_edge(u,v):
            NG[u][v]['weight'] += w
        else:
            NG.add_edge(u, v, weight=w)
    
    return NG

def getNodes(G):

    lay =  nx.kamada_kawai_layout(G)

    nodes = []
    for d in lay.values():
        pt = rg.Point3d( d[0], d[1] , 0)
        nodes.append(pt)

    return nodes


def getEdges(G):

    lay =  nx.kamada_kawai_layout(G)

    edges = []
    for e in G.edges:
        p1 = rg.Point3d( lay[e[0]][0], lay[e[0]][1], 0 )
        p2 = rg.Point3d( lay[e[1]][0], lay[e[1]][1], 0 )
        line = rg.LineCurve(p1, p2)
        edges.append(line)

    return edges


"""
G = createGridGraph(3,3)
GW = addRandomWeigrhs(G)

nodes = getNodes(G)
edges = getEdges(G)
"""



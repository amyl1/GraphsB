import networkx as nx

def Graph():
    G = nx.Graph()

    k = 7
    
    for i in range(1,k+2):
        G.add_node(i)

    G.add_edge(1,2)
    G.add_edge(1,3)
    G.add_edge(1,4)
    G.add_edge(1,5)
    G.add_edge(2,1)
    G.add_edge(2,6)
    G.add_edge(2,7)
    G.add_edge(3,1)
    G.add_edge(3,7)
    G.add_edge(4,1)
    G.add_edge(4,7)
    G.add_edge(5,1)
    G.add_edge(5,6)
    G.add_edge(6,2)
    G.add_edge(6,5)
    G.add_edge(7,2)
    G.add_edge(7,3)
    G.add_edge(7,4)


    G.add_nodes_from(G.nodes(), color='never coloured')
    G.add_nodes_from(G.nodes(), label = -1)
    G.add_nodes_from(G.nodes(), visited = 'no')

    return G
# CSC 486 Assignment 5
# Original author: Dr. Patrick Shepherd

import networkx as nx
import matplotlib.pyplot as plt
from copy import deepcopy
from random import random

def get_undirected_scale_free_graph(n):
    a = nx.scale_free_graph(n)
    g = nx.Graph()
    g.add_nodes_from(range(n))
    for e in a.edges():
        g.add_edge(*e)
    del a
    return g

def girvan_newman(G):
    """
    Carries out the Girvan-Newman community detection algorithm on a graph.
    :param G: A networkx graph
    :return: A list of lists of nodes (the communities)
    """

    # To add an edge, use graphName.add_edge(fromNode, toNode)
    # To remove one, use graphName.remove_edge(fromNode, toNode)
    
    # When looking at connected components of a networkx graph, using
    # varName = list(nx.connected_components(graphName)) will give you
    # back a list of lists, each of which represents one connected component.
    
    # Networkx also provides a function to retrieve the edge betweenness
    # centrality on a graph.
    # myDict = nx.edge_betweenness_centrality(graphName)

    # TODO: Task 1
    pass

def kernighan_lin(G):
    """
    Carries out the Girvan-Newman community detection algorithm on a graph.
    :param G: A networkx graph
    :return: A list of lists of nodes (the communities)
    """

    # TODO: Task 2
    pass

def plot_network(G, coms):
    """
    Plot a network with node colors corresponding to communities
    :param G: A networkx graph
    :param coms: A list of communities
    :return: None
    """

    # TODO: Task 3
    pass

def main():
    G = nx.generators.community.connected_caveman_graph(15, 10)
    # G = nx.generators.community.relaxed_caveman_graph(15, 10, .15)
    # G = nx.barbell_graph(20, 0)
    # G = nx.watts_strogatz_graph(100, 4, .1)
    # G = get_undirected_scale_free_graph(100)
    # G = nx.erdos_renyi_graph(100, .1)
    
    # Use the graph created above as input to your two algorithms, and plot them here.

if __name__ == '__main__':
    main()

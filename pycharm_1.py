# CSC 486 - Teamwork 6
# The purpose of this teamwork is to help familiarize you with the PyCharm
# editor and some of its debugging tools available to you.

import networkx as nx
import random


def give_nodes_a_boolean_property(G):
    for i in range(G.number_of_nodes()):
        G.nodes[i]['property'] = False


def set_some_nodes_to_True(G):
    nodes = choose_random_nodes(G)
    for i in nodes:
        G.nodes[i]['property'] = True


def choose_random_nodes(G):
    nodelist = []
    for i in range(3):
        nextnode = random.randint(0, G.number_of_nodes() - 1)
        while nextnode in nodelist:
            nextnode = random.randint(0, G.number_of_nodes() - 1)
        nodelist.append(nextnode)
    return nodelist


def any_infected_neighbors(G, i):

    for nbr in list(G.neighbors(i)):
        if G.nodes[nbr]['property']:
            return True
    return False


def update_node_properties(G):
    updates = []
    for i in range(G.number_of_nodes()):
        if any_infected_neighbors(G, i):
            updates.append(True)
        else:
            updates.append(False)

    for i in range(len(updates)):
        G.nodes[i]['property'] = updates[i]


def get_perc_infected(G):
    count = 0
    total = G.number_of_nodes()
    for i in range(G.number_of_nodes()):
        if G.nodes[i]['property']:
            count += 1
    return count / total


def main():
    G = nx.watts_strogatz_graph(20, 3, .1)

    give_nodes_a_boolean_property(G)

    set_some_nodes_to_True(G)

    for i in range(10):
        update_node_properties(G)
        print(get_perc_infected(G))

if __name__ == '__main__':
    main()

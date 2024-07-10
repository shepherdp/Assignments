import networkx as nx
import matplotlib.pyplot as plt
import random

# A convenient function to create an undirected scale free graph.
def undirected_scale_free_graph(n):
    """
    Create an undirected scale free networkx graph.
    :param n: Number of nodes
    :return: A networkx graph
    """
    H = nx.scale_free_graph(n)
    G = nx.Graph()
    for (u, v) in H.edges():
        G.add_edge(u, v)
    del H
    return G

def set_parameters(G, beta, gamma):
    """
    Give the graph properties 'beta' and 'gamma' that will be used in update().
    :param G: A networkx graph
    :param beta: The probability of transitioning from S to I
    :param gamma: The probability of transitioning from I to R
    :return: None
    """

    # Give the graph properties 'gamma' and 'beta' here
    # Set a graph property by using
    #    graphName.graph['propertyName'] = someValue
    # TODO: Task 1
    pass

def set_initial_states(G, perc_inf=0.1):
    """
    Give each node in the graph a property called 'state'.
    Initialize the state of perc_inf * n nodes to I (infected), and
    initialize all other nodes' states to S (susceptible).
    :param G: A networkx graph
    :param perc_inf: The percentage of the network to infect initially
    :return: None
    """
    # TODO: Task 2
    pass

def get_num_s(G):
    """
    Calculates the number of agents in state S
    :param G: A networkx graph
    :return: The number of agents in state S
    """
    return len([G.nodes[i]['state'] for i in range(G.number_of_nodes()) if
                G.nodes[i]['state'] == 'S'])

def get_num_i(G):
    """
    Calculates the number of agents in state S
    :param G: A networkx graph
    :return: The number of agents in state S
    """
    return len([G.nodes[i]['state'] for i in range(G.number_of_nodes()) if
                G.nodes[i]['state'] == 'I'])

def get_num_r(G):
    """
    Calculates the number of agents in state S
    :param G: A networkx graph
    :return: The number of agents in state S
    """
    return len([G.nodes[i]['state'] for i in range(G.number_of_nodes()) if
                G.nodes[i]['state'] == 'R'])

def set_resistance(G, nodelist=[]):
    """
    Give all nodes a property called 'resistance', and set it to True for
    all nodes in nodelist, and False for all others.
    :param G: A networkx graph
    :param nodelist: The list of nodes to give resistance to
    :return:None
    """
    # TODO: Task 5
    pass

def get_influential_nodes(G):
    """
    Determines the 10 most influential nodes in the network.
    The idea is to look for nodes that you *think* will be most effective
    at slowing the disease if they are given additional resistance.
    :param G: A networkx graph
    :return: A list of 10 integers representing the nodes you chose
    """
    # TODO: Task 6
    pass

def update(G):
    """
    Updates the state of all nodes in the network
    :param G: A networkx graph
    :return: None
    """
    # TODO: Task 3
    # TODO: Task 7
    pass

def run_sim(G, numsteps=100):
    """
    Run a simulation for numsteps steps and plot the resulting curves
    :param G: A networkx graph
    :param numsteps: The number of steps to run the simulation for
    :return: None
    """
    num_s = []
    num_i = []
    num_r = []

    for i in range(numsteps):
        update(G)
        num_s.append(get_num_s(G))
        num_i.append(get_num_i(G))
        num_r.append(get_num_r(G))

    x = list(range(numsteps))
    plt.plot(x, num_s, label='Susceptible')
    plt.plot(x, num_i, label='Infected')
    plt.plot(x, num_r, label='Recovered')
    plt.legend()
    plt.show()

def main():
    # Create your graph called G
    # Set your parameters to their desired values
    # Set your nodes' initial states
    # Run the simulation
    # TODO: Task 4

if __name__ == '__main__':
    main()

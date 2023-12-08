# CSC 486 Teamwork 11

import networkx as nx
import ndlib.models.ModelConfig as mc
import ndlib.models.opinions as opn
import matplotlib.pyplot as plt

def get_graph(topology='random'):
    """
    Returns a networkx graph
    :param topology: string, the name of the desired topology
    :return: a networkx graph object
    """
    n = 100
    if topology == 'random':
        return nx.erdos_renyi_graph(n, 0.2)
    elif topology == 'small world':
        return nx.watts_strogatz_graph(n, 10, .2)
    elif topology == 'scale free':
        H = nx.scale_free_graph(n)
        G = nx.Graph()
        for (u, v) in H.edges():
            G.add_edge(u, v)
        del H
        return G

def get_model(modelname, g):
    """
    Returns an NDLib model
    :param modelname: string, name of the desired model
    :param g: a networkx graph
    :return: an NDLib model
    """
    if modelname == 'majority':
        return opn.MajorityRuleModel(g)
    elif modelname == 'qvoter':
        return opn.QVoterModel(g)
    elif modelname == 'voter':
        return opn.VoterModel(g)
    elif modelname == 'snazjd':
        return opn.SznajdModel(g)
    elif modelname == 'cognitive':
        return opn.CognitiveOpDynModel(g)
    elif modelname == 'algorithmic':
        return opn.AlgorithmicBiasModel(g)
    elif modelname == 'hk':
        return opn.HKModel(g)

def set_configuration(config, modelname):
    """
    Loads a configuration object with values
    :param config: an NDLib configuration object
    :param modelname: string, name of the diffusion model
    :return: None
    """
    if modelname in ['majority', 'voter', 'qvoter', 'snazjd']:
        config.add_model_parameter('fraction_infected', 0.5)
        config.add_model_parameter('q', 4)

    elif modelname == 'algorithmic':
        config.add_model_parameter("epsilon", .32)
        config.add_model_parameter("gamma", 1)

    elif modelname == 'hk':
        config.add_model_parameter("epsilon", .32)

def runtest(model, algorithm, steps=500):
    """
    Runs a single simulation and plots the results
    :param model: an NDLib model object
    :param algorithm: string, name of the algorithm
    :param steps: number of steps to run
    :return: None
    """
    
    # Set up lists to hold data for plots
    x = list(range(steps))
    if algorithm in ['majority', 'voter', 'qvoter', 'snazjd']:
        ys = [[], []]
    else:
        ys = [[] for i in range(100)]

    # Run simulation for a number of steps
    for i in range(steps):
        ret = model.iteration()
        
        # Record data from current step
        if algorithm in ['majority', 'voter', 'qvoter', 'snazjd']:
            ys[0].append(ret['node_count'][0])
            ys[1].append(ret['node_count'][1])
        else:
            for key in ret['status']:
                ys[key].append(round(ret['status'][key], 5))
            for j in range(100):
                if j not in ret['status'].keys():
                    ys[j].append(ys[j][-1])

    beginning_ops = len(set([line[0] for line in ys]))
    ending_ops = len(set([line[-1] for line in ys]))

    if algorithm in ['algorithmic', 'hk']:
        print(f'Number of different beginning opinions: {beginning_ops}')
        print(f'Number of different ending opinions:    {ending_ops}')

    # Plot data
    numlines = len(ys)
    for i in range(numlines):
        if numlines == 2:
            plt.plot(x, ys[i], label=f'Opinion={i}', alpha=.5)
        else:
            plt.plot(x, ys[i], alpha=.5)
    if numlines == 2:
        plt.legend()
    plt.show()

def main():

    algorithm = 'voter'
    g = get_graph(topology='random')

    config = mc.Configuration()
    set_configuration(config, algorithm)

    model = get_model(algorithm, g)
    model.set_initial_status(config)

    runtest(model, algorithm)

if __name__ == '__main__':
    main()

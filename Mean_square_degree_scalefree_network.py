import random
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

N = 10000

## Creation of a Scale free graph with a mean degree of 10.
## https://networkx.org/documentation/stable/reference/generated/networkx.generators.random_graphs.barabasi_albert_graph.html#networkx.generators.random_graphs.barabasi_albert_graph
ba = nx.barabasi_albert_graph(N, 10)
## Generation of degree associated with each node from the principle of assortativity
## https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.assortativity.average_degree_connectivity.html
meank = nx.average_degree_connectivity(ba)
a = meank.values()

## Squared the degree values of each node
def multiply(meank, value):
    for key in meank.keys():
        meank[key] = meank[key] ** value
    
new_dict = multiply(meank, 2)

## Compute mean square degree
square_meank = meank.values()
sum_square_meank = sum(square_meank)
meank_square_degree = sum_square_meank/len(square_meank)
meank_square_degree


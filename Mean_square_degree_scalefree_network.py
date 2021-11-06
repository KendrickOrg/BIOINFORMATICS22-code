import random
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

N = 10000

## Creation of a Scale free graph with a mean degree of 10.
## https://networkx.org/documentation/stable/reference/generated/networkx.generators.random_graphs.barabasi_albert_graph.html#networkx.generators.random_graphs.barabasi_albert_graph
G = nx.barabasi_albert_graph(N, 10)
## The sequence of degree obtained from the generated graph.
actual_degrees = [d for v, d in G.degree()]
actual_degrees = list(actual_degrees)
## Square degrees
square_degrees = [i**2 for i in actual_degrees]
## Sum of square degree
sum_square_degre = sum(square_degrees)
## Mean square degree
mean_square_degre = sum_square_degre/N
mean_square_degre

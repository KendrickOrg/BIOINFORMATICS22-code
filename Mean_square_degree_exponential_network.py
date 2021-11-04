## Compute the mean square degree in an exponential network
import random
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
N = 10000

degree_sequence = np.random.exponential(scale=10, size=N)
degree_sequence = degree_sequence.astype(int)

degree = degree_sequence[0:N-1]
mean_square = degree*degree
sum_mean_square = sum(mean_square)
meank_square_degree = sum_mean_square/N
meank_square_degree

import matplotlib.pyplot as plt
import csv
import numpy as np
import EoN
import networkx as nx
import pandas as pd
import scipy.interpolate
from collections import defaultdict
import random

N = 10**4
G = nx.barabasi_albert_graph(N, 10)
tmin = 0
tmax = 200
simulationRuns = 50
tau = 0.025    #transmission rate
gamma = 0.1     #recovery rate
rho = 0.005
step = 0.1     #step size
kave = 10
initial_infecteds = 50
xx = np.arange(0, tmax, step)
yy = np.arange(0, tmax, step)

#def _simple_test_transmission_(u, v, p):

#    if ((dt >= tmin) and (dt <= tmax)):
#        p = (1-np.exp(-tau*kave*dt))
#    return random.random()<p

#def f(u,v):
#    ni= 0
#    for ni in G.neighbors(v):
#        ni = ni + 1
#    p = 1-np.exp(-tau*ni*dt)
#    return random.random()<p

dt = 0.1
infecteds = range(initial_infecteds)

def f(u,v,infecteds):
    ni=0
    for ni in G.neighbors(v):
        if ni in infecteds:
            ni = ni + 1
        p = 1-np.exp(-tau*ni*dt)
        return random.random()<p


k = 1000
for counter in range(simulationRuns):
    t, S, I, R = EoN.discrete_SIR(G, test_transmission=f, args = (infecteds,), initial_infecteds = initial_infecteds)
    incidence = np.empty([S.size])
    x=0
    while ((x+k) <= (S.size)-1):
        incidence[x] = -(S[x+k]-S[x])/(t[x+k]-t[x])
        x = x + 1
    if counter == 0:
        plt.plot(t, S, color = 'gray', alpha = 0.3, label = 'S')
        plt.plot(t, I, color = 'red', alpha = 0.3, label = 'I')
    plt.plot(t, S, color = 'gray', alpha = 0.3)  
    plt.plot(t, I, color = 'red', alpha = 0.3)
    
  

    

    


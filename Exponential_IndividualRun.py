import matplotlib.pyplot as plt
import csv
import numpy as np
import EoN
import networkx as nx
import pandas as pd
import random


colors = ['#5AB3E6','#FF2000','#009A80','#E69A00', '#CD9AB3', '#0073B3','#F0E442']

rho = 0.0001
tau = 0.025 #transmission rate
gamma = 0.1 
Nbig=10000

iterations = 50
tmin = 0
tmax = 200
initial_infecteds = 50

PlPk = {}
exponent = 9.49

for k in range(1,10000):
    PlPk[k]= (1-np.exp(-1./exponent))*(np.exp(-1*(k-1)/exponent))
    kave = 10

normfact= sum(PlPk.values())
for k in PlPk:
    PlPk[k] /= normfact

def PsiPowLaw(x):
    #print PlPk
    rval = 0
    for k in PlPk:
        rval += PlPk[k]*x**k
    return rval

def DPsiPowLaw(x):
    rval = 0
    for k in PlPk:
        rval += k*PlPk[k]*x**(k-1)
    return rval

def get_G(N, Pk):
    while True:
        ks = []
        for ctr in range(N):
            r = random.random()
            for k in Pk:
                if r<Pk[k]:
                    break
                else:
                    r-= Pk[k]
            ks.append(k)
        if sum(ks)%2==0:
            break
    G = nx.configuration_model(ks)
    return G

dt = 0.1
xx = np.arange(0, tmax, dt)
yy = np.arange(0, tmax, dt)


infecteds = range(initial_infecteds)

def f(u,v,infecteds):
    ni=0
    for ni in Gbig.neighbors(v):
        if ni in infecteds:
            ni = ni + 1
        p = 1-np.exp(-tau*ni*dt)
        return random.random()<p

def process_degree_distribution(Gbig,  color, Psi, DPsi, symbol):
    for counter in range(iterations): 
        t, S, I, R = EoN.discrete_SIR(Gbig, test_transmission=f, args = (infecteds,), initial_infecteds = initial_infecteds)
        incidence = - np.diff(S)
        for x in range(1, S.size-1):
            incidence[x] = -(S[x+1]-S[x])/(t[x+1]-t[x])
        incidence = np.concatenate(([0], incidence))
        if counter == 0:
            plt.plot(t, incidence, color = 'gray', alpha = 0.3, label = 'Individual simulation run') 
        plt.plot(t, incidence, color = 'gray', alpha = 0.3)
    
Gbig = get_G(Nbig, PlPk)
process_degree_distribution(Gbig,  colors[3], PsiPowLaw, DPsiPowLaw, 'd')


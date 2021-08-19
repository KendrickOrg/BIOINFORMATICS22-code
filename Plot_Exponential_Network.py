import matplotlib.pyplot as plt
import csv
import numpy as np
import EoN
import networkx as nx
import pandas as pd
import random


x = np.arange(-0.1, 200, 0.1)


colors = ['#5AB3E6','#FF2000','#009A80','#E69A00', '#CD9AB3', '#0073B3','#F0E442']

rho = 0.0001
tau = 0.025 #transmission rate
gamma = 0.1 
Nbig=10000

iterations = 50
tmax = 200

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


def process_degree_distribution(Gbig,  color, Psi, DPsi, symbol):
    for counter in range(iterations): 
        t, S, I1, R = EoN.fast_SIR(Gbig, tau, gamma, rho=rho, tmax = tmax)
        if counter == 0:
            plt.plot(t, I1*1./Gbig.order(), color = 'gray', alpha=0.3, label='Individual simulation run')
        plt.plot(t, I1*1./Gbig.order(), color = 'gray', alpha=0.3)

Gbig = get_G(Nbig, PlPk)
process_degree_distribution(Gbig,  colors[3], PsiPowLaw, DPsiPowLaw, 'd')


df1 = pd.read_csv('Sources/Aparicio_ExpoS.csv')
df1 = df1.loc[:, '{#status->#S}']
inc1 = - df1.diff()*11.5


df2 = pd.read_csv('Sources/Stroud_HMS.csv')
df2 = df2.loc[:, '{#status->#S}']
inc2 = - df2.diff()*60


df3 = pd.read_csv('Sources/Stroud_ExpoS.csv')
df3 = df3.loc[:, '{#status->#S}']
inc3 = - df3.diff()*50


plt.plot(x, inc1, '--', label='Aparicio simulation', color='green')
plt.plot(x, inc2, label='Homogeneous Mixing', color='red')
plt.plot(x, inc3, '-.', label='Stroud simulation', color='blue')

plt.xlabel('Time')
plt.ylabel('New infections per day')
plt.title('Exponential Network')
plt.legend()

plt.show()
plt.savefig('Plot/Exponential_network.png')

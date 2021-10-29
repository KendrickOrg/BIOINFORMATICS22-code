import matplotlib.pyplot as plt
import csv
import numpy as np
import EoN
import networkx as nx
import pandas as pd
import random



N = 10**4
kave = 10

tmin = 0
tmax = 200
simulationRuns = 50

tau = 0.025    #transmission rate
gamma = 0.1     #recovery rate
rho = 0.005
step = 0.1     #step size

step_max_plot = 1200

xx = np.arange(0, step_max_plot*step, step)
yy = np.arange(0, step_max_plot*step, step)

plt.figure(figsize=(12,8))
plt.ylim(0.0,800)

nb_initial_infecteds = 50
initial_infecteds = range(nb_initial_infecteds)


df1 = pd.read_csv('Stock/Aparicio_ScaleFree.csv')
df1 = df1.loc[:, '{#status->#S}']

inc1 = - df1.diff()/0.1
inc1 = inc1[:step_max_plot]

df2 = pd.read_csv('Stock/Stroud_HMS.csv')
df2 = df2.loc[:, '{#status->#S}']

inc2 = - df2.diff()/0.1
inc2 = inc2[:step_max_plot]

df3 = pd.read_csv('Stock/Stroud_ScaleS.csv')
df3 = df3.loc[:, '{#status->#S}']

inc3 = - df3.diff()/0.1
inc3 = inc3[:step_max_plot]

plt.plot(xx, inc1, '--', label = 'Aparicio simulation', color = 'green')
plt.plot(xx, inc2, label = 'Homogeneous mixing simulation', color = 'red')
plt.plot(xx, inc3, '-.', label = 'Stroud simulation', color = 'blue')

plt.xlabel('Time')
plt.ylabel('New infections per day')
plt.title('Scale Free network')
plt.legend()
plt.show()
plt.savefig('Plot/ScaleFree.png')


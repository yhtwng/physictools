import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

omega = 1
Q = 5 #mettre plus de 1/2 pour régime pseudo-périodique, 1/2 pour critique, moins de 1/2 pour apériodique
C = 1
E = 1
init = [0,0] #[uc initial uc0, intensité initiale i0]

def equ_odeint(X, t):
    return[X[1]/C, C*(-omega/Q)*(X[1]/C)-omega**2*X[0]+omega**2*E] #[dérivée de uc -> i/C, dérivée de i -> C *(- omega/Q *i/C -w²0*uc+w²0E)] [fonction dérivées]

t = np.linspace(0, 50, 1000) #np.linspace(début, fin, nb de points) [liste de temps]

X = odeint(equ_odeint, init, t) #X = [[uc0,i0], [uc1,i1], ... [ucj,ij]]

uc = [] #création liste positions
i = [] #création liste vitesses
for j in range (len(X)):
    uc.append(X[j,0]) #récupération uc0, uc1, ... ucj
    i.append(X[j,1]) #récupération i0, i1, ..., ij
    
plt.plot(t, uc)
plt.title("Tension en fonction du temps")
plt.xlabel("Temps en s")
plt.ylabel("Tension en V")
plt.show()

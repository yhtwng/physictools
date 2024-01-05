import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

omega = 1
init = [1,0] #[position initiale x0, vitesse initiale v0]

def equ_odeint(X, t):
    return[X[1], - omega**2*X[0]] #[dérivée de x -> v, dérivée de v -> - omega²*x] [fonction dérivées]

t = np.linspace(0, 15, 100) #np.linspace(début, fin, nb de points) [liste de temps]

X = odeint(equ_odeint, init, t) #X = [[x0,v0], [x1,v1], ... [xi,vi]]

x = [] #création liste positions
v = [] #création liste vitesses
for i in range (len(X)):
    x.append(X[i,0]) #récupération x0, x1, ... xi
    v.append(X[i,1]) #récupération v0, v1, ..., vi
    
plt.plot(t, x)
plt.title("Position en fonction du temps")
plt.xlabel("Temps en s")
plt.ylabel("Position en m")
plt.show()
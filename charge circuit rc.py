import matplotlib.pyplot as plt
import numpy as np

tau = 1

def f(u):
    return (1 - u)
def Euler(a, b, N):
    t = np.linspace(a, b, N) #np.linspace(début, fin, nb de points) [liste temps]

    u = [0] #condition initiale [liste tension]

    for i in range (N-1) : #for i in range (nb de points-1):
        u.append(u[i] + f(u[i])*(t[1] - t[0])) #u.append(u[i] + f(u[i])*pasdutemps)
        
    return t, u
t1, u1 = Euler(0, 6*tau, 1000)
plt.plot(t1, u1)
plt.title("charge du condensateur en fonction du temps")
plt.xlabel("temps en s")
plt.ylabel("tension en V")
plt.show()

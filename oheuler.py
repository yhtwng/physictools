import matplotlib.pyplot as plt

omega = 1

def Euler(N, a, b, x0, v0): #def Euler(nb de points, début, fin, position initiale, vitesse initiale):
    t = [a] #initialisation du temps
    x = [x0] #initialisation x
    v = [v0] #initialisation v
    h = (b-a)/float(N) #pas
    for i in range (N):
        t.append(t[i] + h)
        v.append(v[i] - omega**2*x[i]*h) #dv/dt = - omega² * x
        x.append(x[i] + v[i]*h) #dx/dt = v
    return t,x,v

t1, x1, v1 = Euler(5000, 0, 15, 1, 0) #récupération des listes calculées par Euler
plt.plot(t1, x1)
plt.xlabel("temps en s")
plt.ylabel("position en m")
plt.show()

plt.plot(t1,v1)
plt.xlabel("temps en s")
plt.ylabel("vitesse en m")
plt.show()
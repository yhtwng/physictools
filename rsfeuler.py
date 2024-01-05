import matplotlib.pyplot as plt

omega = 1
Q = 5 #mettre plus de 1/2 pour régime pseudo-périodique, 1/2 pour critique, moins de 1/2 pour apériodique
C = 1
E = 1

def Euler(N, a, b, uc0, i0): #def Euler(nb de points, début, fin, uc initiale, i initiale):
    t = [a] #initialisation du temps
    uc = [uc0] #initialisation uc
    i = [i0] #initialisation i
    h = (b-a)/float(N) #pas
    for j in range (N):
        t.append(t[j] + h)
        i.append(i[j] + (C*(-omega/Q)*(i[j]/C)-omega**2*uc[j]+omega**2*E)*h) #di/dt = C *(- omega/Q *i/C -w²0*uc+w²0E)
        uc.append(uc[j] + i[j]*h/C) #duc/dt = i/C
    return t,uc

t1, uc1 = Euler(5000, 0, 50, 0, 0) #récupération des listes calculées par Euler
plt.plot(t1, uc1)
plt.xlabel("temps en s")
plt.ylabel("tension en V")
plt.show()

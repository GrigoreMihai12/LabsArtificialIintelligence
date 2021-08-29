import random
import CitireAfisareFisier
import math

listacoordonate = CitireAfisareFisier.readfromfille()


def generaredistante():
    distante = [[0 for col in range(len(listacoordonate))] for row in range(len(listacoordonate))]
    for i in range(0, len(listacoordonate)):
        for j in range(0, len(listacoordonate)):
            distante[i][j] = int(math.sqrt((listacoordonate[i].get_x() - listacoordonate[j].get_x()) ** 2 + (
                        listacoordonate[i].get_y() - listacoordonate[j].get_y()) ** 2))
    return distante


A = generaredistante()


def generaresolutierandom():
    solutierandom = []
    for i in range(0, len(listacoordonate)):
        solutierandom.append(i)
    random.shuffle(solutierandom)
    return solutierandom


def calcularecost(sol):
    cost = 0
    for i in range(0, (len(sol) - 1)):
        cost = cost + A[sol[i]][sol[i + 1]]
    cost = cost + A[sol[-1]][sol[0]]
    return cost


def generarevein(sol, a, b):
    p = sol[a]
    sol[a] = sol[b]
    sol[b] = p
    return sol


def greedy():
    cost = 0
    pozitii = []
    pozitii.append(0)
    count = 0
    for i in range(0, len(listacoordonate) - 1):
        min = 99999999
        poz = -1
        for j in range(0, len(listacoordonate)):
            if pozitii[count] != j and j not in pozitii :
                if A[pozitii[count]][j] < min:
                    min = A[pozitii[count]][j]
                    poz = j
        cost = cost + min
        count = count + 1
        pozitii.append(poz)
    cost = cost + A[0][pozitii[count]]
    print(len(pozitii))
    CitireAfisareFisier.afisare(cost, pozitii)


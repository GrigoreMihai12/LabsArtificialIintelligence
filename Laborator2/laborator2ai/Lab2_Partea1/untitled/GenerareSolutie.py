import random
import CitireAfisareFisier


capacitateruscac, listaobiecte = CitireAfisareFisier.readfromfille()


def generaresolutie():
    numar = [0 for i in range(len(listaobiecte))]
    for i in range(0, len(listaobiecte)):
        numar[i] = random.randint(0, 1)
    return numar


def calcularegreutate(numar):
    greutate = 0
    for i in range(0, len(listaobiecte)):
        greutate = greutate + numar[i] * listaobiecte[i].get_greutate()
    return greutate


def verificaresolutie(greutate):
    if greutate > capacitateruscac:
        return False
    else:
        return True


def calculvaloare(numar):  # functia de fitness
    valoare = 0
    for i in range(0, len(listaobiecte)):
        valoare = valoare + numar[i] * listaobiecte[i].get_valoare()
    return valoare


def calcularevecini(poatesolutie, numarvecini):
    poatesolutie[numarvecini - 1] = (poatesolutie[numarvecini - 1] + 1) % 2
    return poatesolutie


def celmaibunvecinnontabu(poatesolutie, tabulist):
    best = [0] * len(poatesolutie)
    poz = 0
    for i in range(0, len(poatesolutie)):
        if tabulist[i] == 0:
            poatesolutie1 = poatesolutie[:]
            vecin = calcularevecini(poatesolutie1, i)
            if verificaresolutie(calcularegreutate(vecin)) == True:
                if calculvaloare(best) < calculvaloare(vecin):
                    best = vecin[:]
                    poz = i
    return best, poz

def UpdateMemory(list, poz, iteratii):
    for i in range(0, len(list)):
        if list[i] != 0:
            list[i] = list[i] - 1
    list[poz] = iteratii
    return list


def maximsolutie(sol1, sol2):
    if calculvaloare(sol1) > calculvaloare(sol2):
        return sol1
    else:
        return sol2


def celmaibunvecinnontabu1(poatesolutie, tabulist, bestsolutie, longmem):
    best = [0] * len(poatesolutie)
    poz = 0
    for i in range(0, len(poatesolutie)):
        if tabulist[i] == 0:
            poatesolutie1 = poatesolutie[:]
            vecin = calcularevecini(poatesolutie1, i)
            if verificaresolutie(calcularegreutate(vecin)) == True:
                if calculvaloare(best) < calculvaloare(vecin):
                    best = vecin[:]
                    poz = i
    if best > bestsolutie:
        return best, poz
    else:
        for i in range(0, len(poatesolutie)):
            if tabulist[i] == 0:
                poatesolutie1 = poatesolutie[:]
                vecin = calcularevecini(poatesolutie1, i)
                if verificaresolutie(calcularegreutate(vecin)) == True:
                    if (calculvaloare(best) - (0.7 * longmem[i])) < (calculvaloare(vecin) - (0.7 * longmem[i])):
                        best = vecin[:]
                        poz = i
        return best, poz

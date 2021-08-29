import random
import CitireAfisareFisier
from Solutie import Solutie

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


def calculvaloare(numar): #functia de fitness
    valoare = 0
    for i in range(0, len(listaobiecte)):
        valoare = valoare + numar[i] * listaobiecte[i].get_valoare()
    return valoare


def bestsolutie(solutii):
    best = Solutie(0, 0, 0)
    for solutie in solutii:
        if solutie.get_valoare() > best.get_valoare():
            best = solutie
    return best


def calcularevecini(poatesolutie, numarvecini):
    poatesolutie[numarvecini - 1] = (poatesolutie[numarvecini - 1] + 1) % 2
    if poatesolutie[numarvecini - 1] == 0:
        return -1
    else:
        return poatesolutie


def maximsolutie(solutie1, solutie2):
    if calculvaloare(solutie1) < calculvaloare(solutie2):
        return True
    else:
        return False

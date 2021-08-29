import random
import CitireAfisareFisier
import math

listacoordonate = CitireAfisareFisier.readfromfille()


def getcapacitate():
    return len(listacoordonate)


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


def GenerarePopulatie(marimepopulatie):
    populatii = []
    for i in range(0, marimepopulatie):
        individ = generaresolutierandom()
        populatii.append(individ)
    return populatii


def CalculareFitnessPopulatie(populatii):
    fitness = []
    for i in range(0, len(populatii)):
        fitnessindivid = calcularecost(populatii[i])
        fitness.append(fitnessindivid)
    return fitness


def GenerareParinte(populatie, tournir):
    competitie = []
    p = 0
    while p < tournir:
        candidat = populatie[random.randint(0, (len(populatie) - 1))][:]
        competitie.append(candidat)
        p = p + 1
    best = []
    fitnessmaxim = 999999
    for i in range(0, len(competitie)):
        if fitnessmaxim > calcularecost(competitie[i]):
            best = competitie[i][:]
            fitnessmaxim = calcularecost(competitie[i])
    return best


def GenerareCopii(mama, tata):
     p = random.randint(0, (len(mama) - 2))
     copil1 = mama[0:p][:]
     for i in range(0, len(tata)):
         if tata[i] not in copil1:
             copil1.append(tata[i])
     copil2 = tata[0:p][:]
     for i in range(0, len(mama)):
         if mama[i] not in copil2:
             copil2.append(mama[i])
     return copil1, copil2


def GenerareParintisiCopii(populatie, fitness, marime, tournir):
    parinti = []
    copii = []
    for i in range(0, marime):
        parinte1 = GenerareParinte(populatie, tournir)
        parinte2 = GenerareParinte(populatie, tournir)
        parinti.append(parinte1)
        parinti.append(parinte2)
        copil1, copil2 = GenerareCopii(parinte1, parinte2)
        copii.append(copil1)
        copii.append(copil2)
    return parinti, copii

def Swap(copil):
    a = random.randint(0, (len(copil) - 1))
    b = random.randint(0, (len(copil) - 1))
    p = copil[a]
    copil[a] =  copil[b]
    copil[b] = p
    return copil

def GenerareMutatii(copii, probmutatie):
    mutatii = []
    for copil in copii:
        if random.random() > probmutatie:
            copil1 = copil[:]
            copil2 = Swap(copil1)
            mutatii.append(copil2)
        else:
            mutatii.append(copil)
    return mutatii


def GenerareSupravietuitori(mutatii, parinti, marimepopulatie):
    total = mutatii[:] + parinti[:]
    total.sort(key = calcularecost)
    best = total[0:marimepopulatie]
    return best

'''
def GenerareParinte1(populatie):
    tournament = random.randint(2, len(populatie) - 1)
    competitie = []
    iteratii = 0
    while iteratii < tournament:
        candidat = populatie[random.randint(0, (len(populatie) - 1))][:]
        competitie.append(candidat)
        iteratii = iteratii + 1
    best = []
    fitnessmaxim = 999999
    for i in range(0, len(competitie)):
        if fitnessmaxim > CalculareFitness(competitie[i]):
            best = competitie[i][:]
            fitnessmaxim = CalculareFitness(competitie[i])
    return best
'''

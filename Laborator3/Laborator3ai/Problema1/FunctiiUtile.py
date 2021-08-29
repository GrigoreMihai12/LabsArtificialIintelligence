import CitireAfisareFisier
import random

capacitateruscac, listaobiecte = CitireAfisareFisier.readfromfille()

def getcapacitate():
    return capacitateruscac


def generarepoatesolutierandom():
    numar = [0 for i in range(len(listaobiecte))]
    for i in range(0, len(listaobiecte)):
        numar[i] = random.randint(0, 1)
    return numar


def calcularegreutate(sir):
    greutate = 0
    for i in range(0, len(listaobiecte)):
        greutate = greutate + sir[i] * listaobiecte[i].get_greutate()
    return greutate


def verificare(poatesolutie):
    if calcularegreutate(poatesolutie) > capacitateruscac:
        return False
    else:
        return True


def generaresolutiirandom():
    poatesolutie = generarepoatesolutierandom()
    while verificare(poatesolutie) == False:
        poatesolutie = generarepoatesolutierandom()
    return poatesolutie


def GenerarePopulatie(capacitate):
    populatie = []
    for i in range(0, capacitate):
        individ = generaresolutiirandom()
        populatie.append(individ)
    return populatie


def CalculareFitnessIndivid(individ):
    valoare = 0
    for i in range(0, len(listaobiecte)):
        valoare = valoare + individ[i] * listaobiecte[i].get_valoare()
    return valoare


def CalculareFitnessPopulatie(populatie):
    fitnessindivizi = [0 for _ in range(0, len(populatie))]
    for i in range(0, len(populatie)):
        fitnessindivizi[i] = CalculareFitnessIndivid(populatie[i])
    return fitnessindivizi


def SelectieTournament(populatie):
    candidat1 = populatie[random.randint(0, (len(populatie) - 1))][:]
    candidat2 = populatie[random.randint(0, (len(populatie) - 1))][:]
    if CalculareFitnessIndivid(candidat1) > CalculareFitnessIndivid(candidat2):
        return candidat1
    else:
        return candidat2


def SelectieRuleta(populatie, fitness):
    suma = 0
    ruleta = [0.0 for i in range(0, len(populatie))]
    for i in range(0, len(fitness)):
        suma = suma + fitness[i]
    suma = float(suma)
    p = float(fitness[0])
    ruleta[0] = float(p / suma)
    for i in range(1, len(populatie)):
        p = float(fitness[i])
        ruleta[i] = float(p / suma) + ruleta[i - 1]
    numarrandom = random.random()
    pozitie = -1
    for i in range(0, len(populatie)):
        if numarrandom < ruleta[i]:
            pozitie = i
    return populatie[pozitie]


def Generare2parinti(populatie, fitness):
    if random.random() < 0.5:
        return SelectieTournament(populatie)
    else:
        return SelectieRuleta(populatie, fitness)

def GenerareCopii(mama, tata):
    if len(mama) != len(tata):
        raise ValueError("Parintii(Genomii) nu au aceeasi lungime")
    p = random.randint(0, (len(mama) - 1))
    return mama[0:p] + tata[p:], tata[0:p] + mama[p:]


def GenerareParintisiCopii(populatie, fitness, marimepopulatie):
    copii = []
    parinti = []
    for i in range(0, marimepopulatie):
        parinte1 = Generare2parinti(populatie, fitness)
        parinte2 = Generare2parinti(populatie, fitness)
        parinti.append(parinte1)
        parinti.append(parinte2)
        copil1, copil2 = GenerareCopii(parinte1, parinte2)
        while verificare(copil1) == False or verificare(copil2) == False:
            copil1, copil2 = GenerareCopii(parinte1, parinte2)
        copii.append(copil1)
        copii.append(copil2)
    return parinti, copii


def mutatie(copil, probmutatie):
    copil1 = [0 for _ in range(0, len(copil))]
    for i in range(0, len(copil)):
        if random.random() > probmutatie:
            copil1[i] = (copil[i] + 1) % 2
    return copil1


def GenerareMutatii(copii, probmutatie):
    mutatii = []
    for copil in copii:
        copil1 = mutatie(copil, probmutatie)
        while verificare(copil1) == False:
            copil1 = mutatie(copil, probmutatie)
        mutatii.append(copil1)
    return mutatii


def GenerareSupravietuitori(parinti, mutatii, marimepopulatie):
    total = mutatii[:] + parinti[:]
    total.sort(key = CalculareFitnessIndivid, reverse = True)
    best = total[0:marimepopulatie]
    return best

'''

'''

from FunctiiUtile import *
from Solutie import Solutie
from CitireAfisareFisier import scrieinfisier

def Algoritm(marimepopulatie, numargeneratii,  probmutatie):
    t = 0
    best = []
    low = []
    populatii = [[[]*getcapacitate()]*marimepopulatie] * (numargeneratii + 1)
    fitnesspopulatii = [[] * marimepopulatie] * (numargeneratii + 1)
    populatii[t] = GenerarePopulatie(marimepopulatie)
    fitnesspopulatii[t] = CalculareFitnessPopulatie(populatii[t])
    while t < numargeneratii:
        parinti, copii = GenerareParintisiCopii(populatii[t], fitnesspopulatii[t], marimepopulatie)
        mutatii = GenerareMutatii(copii, probmutatie)
        supravietuitori = GenerareSupravietuitori(parinti, mutatii, marimepopulatie)
        t = t + 1
        populatii[t] = supravietuitori[:]
        fitnesspopulatii[t] = CalculareFitnessPopulatie(populatii[t])
        print(fitnesspopulatii[t][0])
        best.append(fitnesspopulatii[t][0])
        low.append(fitnesspopulatii[t][marimepopulatie-1])
    solutie = Solutie(fitnesspopulatii[t][0], marimepopulatie, calcularegreutate(populatii[t][0]), numargeneratii, probmutatie)
    scrieinfisier(solutie)
    return best, low

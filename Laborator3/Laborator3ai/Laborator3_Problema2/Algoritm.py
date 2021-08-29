from FunctiiUtile import *
from Solutie import Solutie
from CitireAfisareFisier import scrieinfisier

def Algoritm(marimepopulatie, numargeneratii, probmutatie, tournir):
    t = 0
    best = []
    low = []
    populatii = [[[]*getcapacitate()]*marimepopulatie] * (numargeneratii + 1)
    fitnesspopulatii = [[] * marimepopulatie] * (numargeneratii + 1)
    populatii[t] = GenerarePopulatie(marimepopulatie)
    fitnesspopulatii[t] = CalculareFitnessPopulatie(populatii[t])
    while t < numargeneratii:
        parinti, copii = GenerareParintisiCopii(populatii[t], fitnesspopulatii[t], marimepopulatie, tournir)
        mutatii = GenerareMutatii(copii, probmutatie)
        supravietuitori = GenerareSupravietuitori(mutatii, parinti, marimepopulatie)
        t = t + 1
        populatii[t] = supravietuitori[:]
        fitnesspopulatii[t] = CalculareFitnessPopulatie(populatii[t])
        best.append(fitnesspopulatii[t][0])
        low.append(fitnesspopulatii[t][marimepopulatie-1])
    solutie = Solutie(fitnesspopulatii[t][0], marimepopulatie, numargeneratii, probmutatie, tournir)
    scrieinfisier(solutie)
    return best, low

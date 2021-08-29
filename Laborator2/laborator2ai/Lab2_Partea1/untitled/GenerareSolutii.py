import GenerareSolutie
import CitireAfisareFisier
from Solutie import Solutie

def Generare(numariteratii, numariteratiitabu):
    numariteratii1 = numariteratii
    poatesolutie = GenerareSolutie.generaresolutie()
    while GenerareSolutie.verificaresolutie(GenerareSolutie.calcularegreutate(poatesolutie)) == False:
        poatesolutie = GenerareSolutie.generaresolutie()
    bestsolutie = poatesolutie[:]
    tabulist = [0] * len(poatesolutie)
    while numariteratii != 0:
        vecin, poz = GenerareSolutie.celmaibunvecinnontabu(poatesolutie, tabulist)
        tabulist = GenerareSolutie.UpdateMemory(tabulist, poz, numariteratiitabu)
        poatesolutie = vecin[:]
        bestsolutie = GenerareSolutie.maximsolutie(bestsolutie, poatesolutie)
        numariteratii = numariteratii - 1
    solutie = Solutie(bestsolutie, GenerareSolutie.calculvaloare(bestsolutie), numariteratii1, GenerareSolutie.calcularegreutate(bestsolutie), numariteratiitabu)
    CitireAfisareFisier.scrieinfisier(solutie)

def Generare1(numariteratii, numariteratiitabu):
    numariteratii1 = numariteratii
    poatesolutie = GenerareSolutie.generaresolutie()
    while GenerareSolutie.verificaresolutie(GenerareSolutie.calcularegreutate(poatesolutie)) == False:
        poatesolutie = GenerareSolutie.generaresolutie()
    bestsolutie = poatesolutie[:]
    tabulist = [0] * len(poatesolutie)
    longmem = [0] * len(poatesolutie)
    while numariteratii != 0:
        vecin, poz = GenerareSolutie.celmaibunvecinnontabu1(poatesolutie, tabulist, bestsolutie, longmem)
        tabulist = GenerareSolutie.UpdateMemory(tabulist, poz, numariteratiitabu)
        longmem[poz] = longmem[poz] + 1
        poatesolutie = vecin[:]
        bestsolutie = GenerareSolutie.maximsolutie(bestsolutie, poatesolutie)
        numariteratii = numariteratii - 1
    solutie = Solutie(bestsolutie, GenerareSolutie.calculvaloare(bestsolutie), numariteratii1, GenerareSolutie.calcularegreutate(bestsolutie), numariteratiitabu)
    CitireAfisareFisier.scrieinfisier1(solutie)

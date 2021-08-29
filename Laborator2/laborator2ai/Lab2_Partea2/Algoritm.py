import FunctiiUtile
import random
import math
from Solutie import Solutie
import CitireAfisareFisier

def algoritmSA(numariteratii, temperatura, alpha, temperaturaminima):
    numariteratii1 = numariteratii
    FunctiiUtile.greedy()
    temperatura1 = temperatura
    sol = FunctiiUtile.generaresolutierandom()
    while temperatura > temperaturaminima:
        while numariteratii != 0:
            a = random.randint(0, (len(sol) - 1))
            b = random.randint(0, (len(sol) - 1))
            sol1 = sol[:]
            vecin = FunctiiUtile.generarevein(sol1, a, b)
            delta = FunctiiUtile.calcularecost(vecin) - FunctiiUtile.calcularecost(sol)
            if delta < 0:
                sol = vecin[:]
            elif random.uniform(0, 1) < math.exp((-delta) / temperatura):
                sol = vecin[:]
            numariteratii = numariteratii - 1
        numariteratii = numariteratii1
        temperatura = alpha * temperatura
    costsolutie = FunctiiUtile.calcularecost(sol)
    solutie = Solutie(sol, costsolutie, numariteratii1, temperatura1, alpha ,temperaturaminima)
    CitireAfisareFisier.scrieinfisier(solutie)


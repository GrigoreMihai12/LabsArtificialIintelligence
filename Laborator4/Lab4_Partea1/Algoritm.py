from FunctiiUtile import *
from Afisare import *

def algoritm(pop_size, gen_number, prob_mutatie):
    valoareminima = -100
    valoaremaxima = 100
    generatia = 0
    best = []
    low = []

    pop_initiala = initializarepopulatie(pop_size, valoareminima, valoaremaxima)
    minn, maxx = calculareminmaxindivid(pop_initiala)
    best.append(minn)
    low.append(maxx)

    while generatia < gen_number:
        for i in range(0, pop_size):
            p1 = pop_initiala[i]
            p2 = turnir_binar(pop_initiala)
            cop1 = incrucisare(p1, p2)
            cop2 = incrucisare(p2, p1)
            bestt = cop1
            if cop1.get_valoare() > cop2.get_valoare():
                bestt = cop2
            if bestt.get_valoare() < p1.get_valoare():
                pop_initiala[i] = bestt
            m = mutation(pop_initiala[i], prob_mutatie, valoareminima, valoaremaxima)
            if m.get_valoare() < pop_initiala[i].get_valoare():
                pop_initiala[i] = m
        generatia = generatia + 1
        minn, maxx = calculareminmaxindivid(pop_initiala)
        best.append(minn)
        low.append(maxx)

    Individmin = pop_initiala[0]
    for i in range(1, pop_size):
        if Individmin.get_valoare() > pop_initiala[i].get_valoare():
            Individmin = pop_initiala[i]
    scrieinfisier(Individmin)
    return best, low

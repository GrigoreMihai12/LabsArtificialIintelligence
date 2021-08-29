import random
import math
from Individ import *

def calcfitness(x1, x2):
    fitness = -math.cos(x1) * math.cos(x2) * (math.exp(-(x1 - math.pi)**2 - (x2 - math.pi)**2))
    return fitness

def turnir_binar(pop):
    poz1 = random.randint(0, len(pop) - 1)
    poz2 = random.randint(0, len(pop) - 1)
    individ1 = pop[poz1]
    individ2 = pop[poz2]
    if individ1.get_valoare() < individ2.get_valoare():
        return individ1
    else:
        return individ2

'''
def SelectieRuleta(populatie):
    suma = 0.0
    ruleta = [0.0 for _ in range(0, len(populatie))]
    for i in range(0, len(populatie)):
        suma = suma + populatie[i].get_valoare()
    suma = float(suma)
    p = float(populatie[0].get_valoare())
    ruleta[0] = float(p / suma)
    for i in range(1, len(populatie)):
        p = float(populatie[i].get_valoare())
        ruleta[i] = float(p / suma) + ruleta[i - 1]
    numarrandom = random.random()
    pozitie = -1
    for i in range(0, len(populatie)):
        if numarrandom < ruleta[i]:
            pozitie = i
    return populatie[pozitie]
'''


def mutation(mut, prob_mutatie, minn, maxx):
    x = random.random()
    if x < prob_mutatie:
        mut.set_x1(random.uniform(minn, maxx))
    x = random.random()
    if x < prob_mutatie:
        mut.set_x2(random.uniform(minn, maxx))
    return mut

'''
def mutation(mut, minn, maxx):
    x = random.uniform(0, 1)
    if x == 0:
        mut.set_x1(random.uniform(minn, maxx))
    else:
        mut.set_x2(random.uniform(minn, maxx))
    return mut
'''

def incrucisare(p1, p2):
    p = [1, 2]

    x = random.choice(p)
    if x == 1:
        x_copil = (p1.get_x1() + p2.get_x1()) / 2
        y_copil = p1.get_x2()
        z_copil = calcfitness(x_copil, y_copil)
        copil = individ(x_copil, y_copil, z_copil)
    else:
        x_copil = p1.get_x2()
        y_copil = (p1.get_x2() + p2.get_x2()) / 2
        z_copil = calcfitness(x_copil, y_copil)
        copil = individ(x_copil, y_copil, z_copil)
    return copil

'''
def incrucisare(p1, p2):
    x_copil = p1.get_x1()
    y_copil = p2.get_x2()
    z_copil = calcfitness(x_copil, y_copil)
    copil = individ(x_copil, y_copil, z_copil)
    return copil

'''

def initializarepopulatie(pop_size, minn, maxx):
    pop_initiala = []
    for i in range(0, pop_size):
        x1 = random.uniform(minn, maxx)
        x2 = random.uniform(minn, maxx)
        valoare = calcfitness(x1, x2)
        Individ = individ(x1, x2, valoare)
        pop_initiala.append(Individ)
    return pop_initiala

def calculareminmaxindivid(pop_initiala):
    individmin = 1
    individmax = -1
    for i in range(0, len(pop_initiala)):
        if individmin > pop_initiala[i].get_valoare():
            individmin = pop_initiala[i].get_valoare()
        if individmax < pop_initiala[i].get_valoare():
            individmax = pop_initiala[i].get_valoare()
    return individmin, individmax

from Particula import *
from Repo import *

def algoritm(numarparticule, iteratii, w, c1, c2, limitainf, limitasup):
    limite = [limitainf, limitasup]
    globalfitness = 1.0
    globalpozitie = []
    swarm_particule = []
    for i in range(numarparticule):
        swarm_particule.append(Particula(limite, 1.0))
    A = []
    for i in range(0, iteratii):
        for j in range(0, numarparticule):
            swarm_particule[j].evaluate(calcfitness)
            if swarm_particule[j].fitnesspozitiecurenta < globalfitness:
                globalpozitie = list(swarm_particule[j].pozitie)
                globalfitness = float(swarm_particule[j].fitnesspozitiecurenta)
        for j in range(0, numarparticule):
            swarm_particule[j].updateviteza(globalpozitie, c1, c2, w)
            swarm_particule[j].updateposition(limite)
        A.append(globalfitness)
    scrieinfisier(globalpozitie[0], globalpozitie[1], globalfitness)
    return A

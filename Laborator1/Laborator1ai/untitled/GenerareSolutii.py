import GenerareSolutie
import CitireAfisareFisier
import random

def Generare(numariteratii):
    solutii = []
    for i in range(0, int(numariteratii)):
        poatesolutie = GenerareSolutie.generaresolutie()
        greutate = GenerareSolutie.calcularegreutate(poatesolutie)
        if GenerareSolutie.verificaresolutie(greutate) == True:
            solutie = GenerareSolutie.Solutie(poatesolutie, GenerareSolutie.calculvaloare(poatesolutie), numariteratii)
            solutii.append(solutie)

    solutie = GenerareSolutie.bestsolutie(solutii)
    GenerareSolutie.CitireAfisareFisier.scrieinfisier(solutie)


'''
def GenerareRHC(numariteratii):
    numariteratii1 = numariteratii
    solutiefinala = [0] * len(GenerareSolutie.generaresolutie())
    while numariteratii != 0:
        poatesolutie = GenerareSolutie.generaresolutie()
        greutate = GenerareSolutie.calcularegreutate(poatesolutie)
        if GenerareSolutie.verificaresolutie(greutate) == True:
            if GenerareSolutie.maximsolutie(solutiefinala, poatesolutie) == True:
                solutiefinala = poatesolutie[:]
            numarvecini = len(poatesolutie)
            while numariteratii != 0 and numarvecini != 0:
                poatesolutie1 = poatesolutie #copie
                solutienoua = GenerareSolutie.calcularevecini(poatesolutie1, numarvecini)
                if solutienoua != -1:#verificam daca bitul s-a schimbat din 0 in 1
                    greutate = GenerareSolutie.calcularegreutate(solutienoua)
                    if GenerareSolutie.verificaresolutie(greutate) == True:
                        if GenerareSolutie.maximsolutie(solutiefinala, solutienoua) == True:
                            solutiefinala = solutienoua[:]
                            poatesolutie = solutienoua[:]
                            numarvecini = len(poatesolutie)
                            numariteratii = numariteratii - 1
                        else:
                            numariteratii = numariteratii - 1
                numarvecini = numarvecini - 1
    solutiee = GenerareSolutie.Solutie(solutiefinala, GenerareSolutie.calculvaloare(solutiefinala), numariteratii1)
    CitireAfisareFisier.scriereinfisier1(solutiee)
'''

def GenerareRHC(numariteratii):
    numariteratii1 = numariteratii
    solutiefinala = [0] * len(GenerareSolutie.generaresolutie())
    poatesolutie = GenerareSolutie.generaresolutie()
    while GenerareSolutie.verificaresolutie(GenerareSolutie.calcularegreutate(poatesolutie)) != True:
        poatesolutie = GenerareSolutie.generaresolutie()
    solutiefinala = poatesolutie[:]
    while numariteratii != 0:
        bitschimbare = random.randint(0, len(poatesolutie) - 1)
        poatesolutie1 = poatesolutie[:]
        solutienoua = GenerareSolutie.calcularevecini(poatesolutie1, bitschimbare)
        if solutienoua != -1: #verificam daca bitul s-a schimbat din 0 in 1
            greutate = GenerareSolutie.calcularegreutate(solutienoua)
            if GenerareSolutie.verificaresolutie(greutate) == True:
                if GenerareSolutie.maximsolutie(solutiefinala, solutienoua) == True:
                    solutiefinala = solutienoua[:]
                    poatesolutie = solutienoua[:]
        numariteratii = numariteratii - 1

    solutiee = GenerareSolutie.Solutie(solutiefinala, GenerareSolutie.calculvaloare(solutiefinala), numariteratii1)
    CitireAfisareFisier.scriereinfisier1(solutiee)





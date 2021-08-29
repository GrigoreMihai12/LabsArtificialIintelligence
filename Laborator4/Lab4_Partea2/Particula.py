from Functii import *

class Particula:
    def __init__(self, limite, fitnessinitial):
        self.pozitie = []
        self.viteza = []
        self.bestlocal = []
        self.fitnessbestlocal = fitnessinitial
        self.fitnesspozitiecurenta = fitnessinitial

        for i in range(2): #2 variabile
            self.pozitie.append(random.uniform(limite[0], limite[1]))
            self.viteza.append(random.uniform(-1, 1))

    def evaluate(self, calcfitness):
        self.fitnesspozitiecurenta = calcfitness(self.pozitie[0], self.pozitie[1])
        if self.fitnesspozitiecurenta < self.fitnessbestlocal:
            self.fitnessbestlocal = self.fitnesspozitiecurenta
            self.bestlocal = self.pozitie

    def updateviteza(self, bestglobal, c1, c2, w):
        for i in range(2):
            r1 = random.random()
            r2 = random.random()
            cognitiva_viteza = c1 * r1 * (self.bestlocal[i] - self.pozitie[i])
            social_viteza = c2 * r2 * (bestglobal[i] - self.pozitie[i])
            self.viteza[i] = w * self.viteza[i] + cognitiva_viteza + social_viteza

    def updateposition(self, limite):
        for i in range(2):
            self.pozitie[i] = self.pozitie[i] + self.viteza[i]
            if self.pozitie[i] > limite[1]:
                self.pozitie[i] = limite[1]
            if self.pozitie[i] < limite[0]:
                 self.pozitie[i] = limite[0]

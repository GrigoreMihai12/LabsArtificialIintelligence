class Solutie:

    def __init__(self, valoare, populatia, greutate, generatia, probincrucisare):
        self.valoare = valoare
        self.populatie = populatia
        self.greutate = greutate
        self.generatia = generatia
        self.probincrucisare = probincrucisare


    def __str__(self):
        return ("Solutia are valoarea: " + str(self.valoare) + " si are greutea " + str(
            self.greutate) + ". Populatia este formata din: " + str(self.populatie) + " , s-a obtinut dupa si " + str(
            self.generatia) + " generatii cu probabilitatea de incrucisare: " + str(self.probincrucisare) + ".")

class Solutie:

    def __init__(self, valoare, populatia, generatia, probincrucisare, tournir):
        self.valoare = valoare
        self.populatie = populatia
        self.generatia = generatia
        self.probincrucisare = probincrucisare
        self.tournir = tournir

    def __str__(self):
        return ("Solutia are valoarea: " + str(self.valoare) + ". Populatia este formata din: " + str(
            self.populatie) + " , s-a obtinut dupa si " + str(
            self.generatia) + " generatii cu probabilitatea de incrucisare: " + str(
            self.probincrucisare) + " si tournir:" + str(self.tournir) + ".")

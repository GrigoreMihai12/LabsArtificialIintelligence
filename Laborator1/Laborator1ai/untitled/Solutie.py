class Solutie:

    def __init__(self, cod, valoare, numariteratii):
        self.cod = cod
        self.valoare = valoare
        self.numariteratii = numariteratii

    def get_cod(self):
        return self.cod

    def get_valoare(self):
        return self.valoare

    def get_numariteratii(self):
        return self.numariteratii

    def __str__(self):
        return("Solutia are valoarea: " + str(self.valoare) + " si este de forma " + str(self.cod) + ". S-a obtinut dupa " + str(self.numariteratii) + " interatii.")

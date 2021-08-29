class Solutie:

    def __init__(self, cod, valoare, numariteratii, greutate, iteratiitabu):
        self.cod = cod
        self.valoare = valoare
        self.numariteratii = numariteratii
        self.greutate = greutate
        self.iteratiitabu = iteratiitabu

    def get_cod(self):
        return self.cod

    def get_valoare(self):
        return self.valoare

    def get_numariteratii(self):
        return self.numariteratii

    def __str__(self):
        return("Solutia are valoarea: " + str(self.valoare) + " si are greutea " + str(self.greutate) + ". S-a obtinut dupa " + str(self.numariteratii) + " interatii si " + str(self.iteratiitabu) + " iteratii tabu.")

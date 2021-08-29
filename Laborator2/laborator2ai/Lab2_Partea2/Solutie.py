class Solutie:

    def __init__(self, ordine, cost, numariteratii, temp, alpha, min):
        self.ordine = ordine[:]
        self.cost = cost
        self.numariteratii = numariteratii
        self.temp = temp
        self.alpha = alpha
        self.min = min

    def __str__(self):
        return ("Solutia are ordinea oraselor : " + str(self.ordine) + " cu costul " + str(
            self.cost) + ". S-a obtinut dupa " + str(self.numariteratii) + " interatii si avand " + str(
            self.temp) + " temperatura, alpha fiind " + str(self.alpha) + " iar temp minima: " + str(self.min))

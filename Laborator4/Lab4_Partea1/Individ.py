class individ:
    def __init__(self, x1, x2, valoare):
        self.x1 = x1
        self.x2 = x2
        self.valoare = valoare

    def get_x1(self):
        return self.x1

    def get_x2(self):
        return self.x2

    def get_valoare(self):
        return self.valoare

    def set_x1(self, x1):
        self.x1 = x1

    def set_x2(self, x2):
        self.x2 = x2

    def set_valoare(self, valoare):
        self.valoare = valoare

    def __str__(self):
        return ("x1: " + str(self.x1) + " x2: " + str(self.x2) + " valoare functiei: " + str(self.valoare) + ".")

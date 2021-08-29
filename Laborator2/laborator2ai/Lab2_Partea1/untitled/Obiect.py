class Obiect:

    def __init__(self, index, valoare1, greutate1):
        self.greutate = greutate1
        self.valoare = valoare1
        self.index = index

    def get_greutate(self):
        return self.greutate

    def get_valoare(self):
        return self.valoare

    def get_index(self):
        return self.index

    def set_gretate(self,greutate):
        self.greutate = greutate

    def set_valoare(self,valoare):
        self.valoare = valoare

    def set_index(self,index):
        self.index = index

    def __str__(self):
        return(str(self.index) + " " + str(self.greutate) + " " + str(self.valoare))

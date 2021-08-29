class Coordonate:

    def __init__(self, index, x, y):
        self.index = index
        self.x = x
        self.y = y


    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_index(self):
        return self.index

    def set_x(self,x):
        self.x = x

    def set_y(self,y):
        self.y = y

    def set_index(self,index):
        self.index = index

    def __str__(self):
        return(str(self.index) + " " + str(self.x) + " " + str(self.y))

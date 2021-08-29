from Algoritm import *
import matplotlib.pyplot as plt

def main():
    populatia = int(input("Populatie:"))
    generatii = int(input("Generatii:"))
    probabilitateincrucisare = float(input("Probabilitate incrucisare:"))
    b,l = Algoritm(populatia, generatii, probabilitateincrucisare)
    plt.figure()
    plt.plot(b, 'r')
    plt.plot(l, 'b')
    plt.show()
    '''
    for i in range(0, 10):
        Algoritm(100, 10, 0.4)
    for i in range(0, 10):
        Algoritm(100, 10, 0.8)
    for i in range(0, 10):
        Algoritm (100, 50, 0.6)
    for i in range(0, 10):
        Algoritm(100, 20, 0.4)
    for i in range(0, 10):
        Algoritm(150, 50, 0.8)
    for i in range(0, 10):
        Algoritm (150, 100, 0.6)
    for i in range(0, 10):
        Algoritm(150, 150, 0.5)
    for i in range(0, 10):
        Algoritm(200, 50, 0.8)
    for i in range(0, 10):
        Algoritm (200, 150, 0.6)
    for i in range(0, 10):
        Algoritm(200, 200, 0.5)
    '''


main()

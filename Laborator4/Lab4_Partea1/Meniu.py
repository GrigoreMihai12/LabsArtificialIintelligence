from Algoritm import *
import matplotlib.pyplot as plt

def main():
    populatia = int(input("Populatie:"))
    generatii = int(input("Generatii:"))
    probabilitateincrucisare = float(input("Probabilitate incrucisare:"))
    b,l = algoritm(populatia, generatii, probabilitateincrucisare)
    plt.figure()
    plt.plot(b, 'r')
    plt.plot(l, 'b')
    plt.show()
    '''
    for i in range(0, 10):
        algoritm(500, 500, 0.5)
    for i in range(0, 10):
        algoritm(500, 500, 0.7)
    for i in range(0, 10):
        algoritm (500, 400, 0.6)
    for i in range(0, 10):
        algoritm(500, 600, 0.4)
    for i in range(0, 10):
        algoritm(700, 500, 0.5)
    for i in range(0, 10):
        algoritm (700, 400, 0.5)
    for i in range(0, 10):
        algoritm(700, 600, 0.5)
    for i in range(0, 10):
        algoritm(1000, 500, 0.8)
    for i in range(0, 10):
        algoritm (1000, 600, 0.6)
    for i in range(0, 10):
        algoritm(1000, 1000, 0.5)
    '''

main()

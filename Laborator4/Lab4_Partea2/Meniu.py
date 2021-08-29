from Algoritm import *
import matplotlib.pyplot as plt

def main():
    numarparticule = int(input("Introduceti numarul de particule:"))
    iteratii = int(input("Introduceti numarul de iteratii:"))
    w = float(input("w = "))
    c1 = int(input("c1 = "))
    c2 = int(input("c2 = "))
    limitainf = int(input("Limita inferioara:"))
    limitasup = int(input("Limita superioara:"))
    p = algoritm(numarparticule, iteratii, w, c1, c2, limitainf, limitasup)
    plt.plot(p)
    plt.show()
    '''
    for i in range(0, 10):
        algoritm(100, 500, 1, 2, 2, -100, 100)
    for i in range(0, 10):
        algoritm(100, 500, 0.95, 3, 1, -100, 100)
    for i in range(0, 10):
        algoritm(100, 500, 0.85, 2, 2, -100, 100)
    for i in range(0, 10):
        algoritm(100, 500, 1, 3, 1, -100, 100)
    for i in range(0, 10):
        algoritm(100, 500, 0.99, 2, 2, -100, 100)
    for i in range(0, 10):
        algoritm(100, 2000, 0.95, 2, 2, -100, 100)
    for i in range(0, 10):
        algoritm(100, 1000, 0.95, 2, 2, -100, 100)
    for i in range(0, 10):
        algoritm(1000, 500, 0.95, 2, 2, -100, 100)
    for i in range(0, 10):
        algoritm(1000, 700, 0.95, 2, 2, -100, 100)
    for i in range(0, 10):
        algoritm(1000, 1000, 0.95, 2, 2, -100, 100)
    for i in range(0, 10):
        algoritm(2000, 1000, 0.95, 2, 2, -100, 100)
    for i in range(0, 10):
        algoritm(2000, 1500, 0.95, 2, 2, -100, 100)
    for i in range(0, 10):
        algoritm(2000, 1000, 0.95, 2, 2, -100, 100)
    for i in range(0, 10):
        algoritm(50, 2000, 1, 2, 2, -100, 100)
    '''
main()

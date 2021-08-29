from Algoritm import *
#import matplotlib.pyplot as plt

def main():
    populatia = int(input("Populatie:"))
    generatii = int(input("Generatii:"))
    probabilitateincrucisare = float(input("Probabilitate incrucisare:"))
    tournir = int(input("Tournir:"))
    b,l = Algoritm(populatia, generatii, probabilitateincrucisare, tournir)
    #plt.figure()
   # plt.plot(b, 'r')
   # plt.plot(l, 'b')
   # plt.show()

main()

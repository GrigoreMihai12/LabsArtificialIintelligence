from Coordonate import Coordonate


def readfromfille():
    numefisier = input("NumeFisier:")
    file = open(numefisier, "r")
    count = 0
    listacoordonate = []
    while True:
        count += 1
        line = file.readline()
        if count >= 7:
            detalii = line.split()
            if len(detalii) == 3:
                coordonate = Coordonate(int(detalii[0]), int(detalii[1]), int(detalii[2]))
                listacoordonate.append(coordonate)
        if not line:
            break

    return listacoordonate


def scrieinfisier(solutie):
    f = open("DateOut.txt", "a")
    f.write(str(solutie) + "\n")
    f.close()


def afisare(a, b):
    g = open("SolutieGreedy.txt", "a")
    g.write(str(a) + "\n" + str(b))
    g.close


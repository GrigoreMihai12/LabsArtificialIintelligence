from Obiect import Obiect


def readfromfille():
    numefisier = input("NumeFisier:")
    file = open(numefisier, "r")
    count = 0
    listaobiecte = []
    capacitaterucsac = 0
    numartotalobiecte = 0
    while True:
        count += 1
        line = file.readline()
        if count == 1:
            numartotalobiecte = int(line)
        elif count == numartotalobiecte + 2:
            capacitaterucsac = int(line)
        else:
            detalii = line.split()
            if len(detalii) == 3:
                obiect = Obiect(int(detalii[0]), int(detalii[1]), int(detalii[2]))
                listaobiecte.append(obiect)
        if not line:
            break

    return capacitaterucsac, listaobiecte


def scrieinfisier(solutie):
    f = open("DateOut.txt", "a")
    f.write(str(solutie) + "\n")
    f.close()

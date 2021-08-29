def scrieinfisier(x1, x2, fitness):
    f = open("DateOut.txt", "a")
    f.write("x1: " + str(x1) + " x2: " + str(x2) + " valoare functiei: " + str(fitness) + "." + "\n")
    f.close()

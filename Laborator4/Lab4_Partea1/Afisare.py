def scrieinfisier(solutie):
    f = open("DateOut.txt", "a")
    f.write(str(solutie) + "\n")
    f.close()

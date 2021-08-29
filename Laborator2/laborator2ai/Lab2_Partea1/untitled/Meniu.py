import GenerareSolutii


def main():
    numariteratii = int(input("Introduceti numarul de iteratii:"))
    numariteratiitabu = int(input("Introduceti numarul de iteratii tabu:"))
    GenerareSolutii.Generare(numariteratii, numariteratiitabu)
    GenerareSolutii.Generare1(numariteratii, numariteratiitabu)

if __name__ == "__main__":
    main()

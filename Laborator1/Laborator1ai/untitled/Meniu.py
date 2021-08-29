import GenerareSolutii


def main():
    print("Cautare aleatoare:")
    numariteratii = input("Introduceti numarul de iteratii:")
    GenerareSolutii.Generare(numariteratii)
    print("RANDOM HILL-CLIMBING:")
    numariteratii1 = int(input("Introduceti numarul de iteratii:"))
    GenerareSolutii.GenerareRHC(numariteratii1)

if __name__ == "__main__":
    main()

def report_prestiti(l_catalogo, l_prestiti):
    f_report_prestiti = open("report_prestiti.txt", "w", encoding="UTF-8")
    f_esauriti = open("libri_esauriti.txt", "w", encoding="UTF-8")

    num_esauriti = 0

    for catalogo in l_catalogo:
        tot_prestiti = 0

        titolo = catalogo[1]
        num_copie = int(catalogo[-1])

        for prestito in l_prestiti:
            if catalogo[0] == prestito[3]:
                num_prestiti = int(prestito[-1])
                tot_prestiti += num_prestiti

        num_residue = num_copie - tot_prestiti
        print(f"{titolo}: {tot_prestiti} prestiti, {num_residue} copie disponibili", file=f_report_prestiti)

        if num_residue == 0:
            print(f"{titolo}: Esaurito", file=f_esauriti)
            num_esauriti += 1

    if num_esauriti == 0:
        print("Nessun libro esaurito", file=f_esauriti)

    f_report_prestiti.close()
    f_esauriti.close()


def main():
    l_catalogo = []
    l_prestiti = []

    f_catalogo = open("catalogo.txt", "r", encoding="UTF-8")
    for catalogo in f_catalogo:
        parti = catalogo.rstrip().split('"')
        codice = parti[0].strip()
        titolo = parti[1]
        altri_campi = parti[2].strip().split(" ")
        autore = " ".join(altri_campi[:-1])
        copie = altri_campi[-1]

        l_catalogo.append([codice, titolo, autore, copie])
    f_catalogo.close()

    f_prestiti = open("prestiti.txt", "r", encoding="UTF-8")
    for prestito in f_prestiti:
        prestito = prestito.rstrip().split()
        l_prestiti.append(prestito)

    report_prestiti(l_catalogo, l_prestiti)


main()
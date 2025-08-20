def genera_report_corrieri(lista_corrieri, lista_consegne):
    lista_report = []

    f_report_corrieri = open("report_corrieri.txt", "w", encoding="UTF-8")
    for corriere in lista_corrieri:
        id_corriere = corriere[0]
        nome = corriere[1]
        cognome = corriere[2]

        num_pacchi = 0
        num_consegnati = 0
        peso_tot = 0

        for consegna in lista_consegne:
            peso = float(consegna[2])

            if consegna[0] in corriere[3:]:
                num_pacchi += 1
                if consegna[-1] == 'si':
                    num_consegnati += 1
                peso_tot += peso

        lista_report.append([id_corriere, nome, cognome, num_pacchi, num_consegnati, peso_tot])
        print(f"{nome} {cognome} - Pacchi: {num_pacchi} - Consegnati: {num_consegnati} "
              f"- Peso totale: {peso_tot:.1f} kg", file=f_report_corrieri)

    f_report_corrieri.close()

    return lista_report


def genera_non_consegnati(lista_corrieri, lista_consegne):
    f_non_consegnati = open("non_consegnati.txt", "w", encoding="UTF-8")

    for corriere in lista_corrieri:
        nome = corriere[1]
        cognome = corriere[2]

        for consegna in lista_consegne:
            destinatorio = consegna[1]
            if consegna[0] in corriere[3:] and consegna[-1] == 'no':
                print(f"{consegna[0]} - {destinatorio} - {nome} {cognome}", file=f_non_consegnati)

    f_non_consegnati.close()


def genera_statistiche(lista_report):
    f_statistiche = open("statistiche.txt", "w", encoding="UTF-8")

    max_pacchi = 0
    max_pacchi_nome = ""
    max_peso = 0
    max_peso_nome = ""
    num_consegne = 0
    num_consegne_comp = 0

    for corriere in lista_report:
        nome = corriere[1]
        cognome = corriere[2]
        pacchi = corriere[3]
        consegnati = corriere[4]
        peso = corriere[5]

        if pacchi > max_pacchi:
            max_pacchi = pacchi
            max_pacchi_nome = f"{nome} {cognome}"

        if peso > max_peso:
            max_peso = peso
            max_peso_nome = f"{nome} {cognome}"

        num_consegne += pacchi
        num_consegne_comp += consegnati

    perc = num_consegne_comp / num_consegne * 100

    print(f"Corriere più carico: {max_pacchi_nome} ({max_pacchi} pacchi)", file=f_statistiche)
    print(f"Corriere più peso: {max_peso_nome} ({max_peso:.1f} peso)", file=f_statistiche)
    print(f"Percentuale consegne completate: {perc:.2f}%", file=f_statistiche)

    f_statistiche.close()

def main():
    lista_corrieri = []
    lista_consegne = []

    f_corrieri = open("corrieri.txt", "r", encoding="UTF-8")
    for corriere in f_corrieri:
        corriere = corriere.rstrip().split(" ")
        lista_corrieri.append(corriere)
    f_corrieri.close()

    f_consegne = open("consegne.txt", "r", encoding="UTF-8")
    for consegna in f_consegne:
        consegna = consegna.rstrip().split(" ")
        lista_consegne.append(consegna)
    f_consegne.close()

    lista_report = genera_report_corrieri(lista_corrieri, lista_consegne)
    genera_non_consegnati(lista_corrieri, lista_consegne)
    genera_statistiche(lista_report)

main()

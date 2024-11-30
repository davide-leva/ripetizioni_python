def riempi_test():
    lista_regioni = ['piemonte', 'lombardia', 'trentino alto adige']
    lista_comuni = [
        ['Asti', 75000, 300, 'piemonte'],
        ['Milano', 1000000, 300, 'lombardia'],
        ['Torino', 900000, 150, 'piemonte'],
        ['Trento', 80000, 100, 'trentino alto adige']
    ]

    return lista_regioni, lista_comuni

def riempi_utente():
    lista_regioni = []
    lista_comuni = []

    while True:
        regione = input("Inserisci nome regione: ")

        if regione == "":
            break

        lista_regioni.append(regione)


    print("Inserisci informazioni dei comuni (nome, abitanti, superificie, regione)")
    print("Separare i dati con delle virgole")
    while True:
        dati = input("Inserisci informazioni (premere invio per terminare): ")

        if dati == "":
            break

        lista_comuni.append(dati.split(','))

    return lista_comuni, lista_regioni


def calcola_stats(lista_regioni, lista_comuni):
    lista_pop_regione = []

    for regione in lista_regioni:
        abitanti = 0
        for comune in lista_comuni:
            if comune[3] == regione:
                abitanti += comune[1]

        lista_pop_regione.append([regione, str(abitanti)])

    return lista_pop_regione


def main():
    lista_regioni, lista_comuni = riempi_test()
    lista_pop_regione = calcola_stats(lista_regioni, lista_comuni)

    for statistica in lista_pop_regione:
        print(' '.join(statistica))


if __name__ == '__main__':
    main()
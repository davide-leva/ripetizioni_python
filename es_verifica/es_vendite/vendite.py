def calcola_premio(lista_clienti, lista_vendite):
    """Restituisce una lista_premio"""

    lista_premio = []

    for cliente in lista_clienti:
        somma_punti = 0
        for vendita in lista_vendite:
            if cliente[1] == vendita[0]:
                somma_punti += vendita[3]
        info = [str(cliente[0]), str(cliente[1]), str(somma_punti)]
        if somma_punti > 80:
            info.append("Diritto premio")
        lista_premio.append(info)

    return lista_premio


def calcola_spesa_media(lista_clienti, lista_vendite):
    """Resituisce una lista_spesa_media"""

    lista_spesa_media = []

    for cliente in lista_clienti:
        numero_vendite = 0
        spesa_totale = 0
        for vendita in lista_vendite:
            if cliente[1] == vendita[0]:
                print(vendita[1], vendita[2])
                spesa_totale += vendita[1] * vendita[2]
                numero_vendite += 1

        if numero_vendite > 0:
            spesa_media = spesa_totale / numero_vendite
            info = [str(cliente[1]), str(cliente[2]), str(spesa_media)]
            lista_spesa_media.append(info)

    return lista_spesa_media


def main():
    file_clienti = open("clienti.txt", "r", encoding="UTF-8")
    file_vendite = open("vendite.txt", "r", encoding="UTF-8")

    lista_vendite = []
    lista_clienti = []

    for linea in file_clienti:
        linea = linea.strip().split()
        cf = linea[0]
        nt = int(linea[1])
        citta = linea[4]
        info = [cf, nt, citta]
        lista_clienti.append(info)

    for linea in file_vendite:
        linea = linea.strip().split()
        nt = int(linea[0])
        costo = int(linea[2])
        quantita = int(linea[3])
        punti = int(linea[4])
        info = [nt, costo, quantita, punti]
        lista_vendite.append(info)

    file_clienti.close()
    file_vendite.close()

    lista_premio = calcola_premio(lista_clienti, lista_vendite)
    lista_spesa_media = calcola_spesa_media(lista_clienti, lista_vendite)

    file_premio = open("premio.txt", "w", encoding="UTF-8")
    file_spesa_media = open("spesa_media.txt", "w", encoding="UTF-8")

    for info in lista_premio:
        print(" ".join(info), file=file_premio)

    for info in lista_spesa_media:
        print(" ".join(info), file=file_spesa_media)

    file_clienti.close()
    file_spesa_media.close()


main()

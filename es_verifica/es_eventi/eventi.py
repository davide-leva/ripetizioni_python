def calcola_spesa(d_eventi, l_iscrizioni):
    d_spesa = dict()

    for iscrizione in l_iscrizioni:
        codice_evento = iscrizione[0]
        codice_utente = iscrizione[1]
        num_ingressi = int(iscrizione[2])

        evento = d_eventi[codice_evento]
        prezzo = float(evento[2])

        costo = num_ingressi * prezzo
        if codice_utente in d_spesa.keys():
            d_spesa[codice_utente] += costo
        else:
            d_spesa[codice_utente] = costo

    with open("spesa.txt", "w") as f_spesa:
        for codice_utente, spesa_tot in d_spesa.items():
            f_spesa.write(f"{codice_utente}, {spesa_tot:.2f}\n")


def calcola_ingressi(d_eventi, l_iscrizioni):
    d_ingressi = dict()

    for iscrizione in l_iscrizioni:
        codice_evento = iscrizione[0]
        codice_utente = iscrizione[1]
        num_ingressi = int(iscrizione[2])

        evento = d_eventi[codice_evento]
        nome_evento = evento[0]

        if nome_evento in d_ingressi.keys():
            d_ingressi[nome_evento] += num_ingressi
        else:
            d_ingressi[nome_evento] = num_ingressi

    ds_ingressi = sorted(d_ingressi.items(), key=lambda x: x[1], reverse=True)

    with open("ingressi.txt", "w") as f_ingressi:
        for nome_evento, ingressi_tot in ds_ingressi:
            f_ingressi.write(f"{nome_evento}, {ingressi_tot}\n")


def calcola_eventi_per_anno(l_iscrizioni):
    d_eventi_anno = dict()

    for iscrizione in l_iscrizioni:
        codice_evento = iscrizione[0]
        anno = iscrizione[3]

        if anno in d_eventi_anno.keys():
            d_eventi_anno[anno].add(codice_evento)
        else:
            d_eventi_anno[anno] = set()
            d_eventi_anno[anno].add(codice_evento)

    ds_eventi_anno = sorted(d_eventi_anno.items(), key=lambda x: x[0], reverse=False)

    with open("eventi_anno.txt", "w") as f_eventi_anno:
        for anno, s_eventi in ds_eventi_anno:
            num_eventi = len(s_eventi)
            f_eventi_anno.write(f"{anno}, {num_eventi}\n")


def main():
    d_eventi = dict()
    l_iscrizioni = list()

    with open("eventi.txt", "r") as f_eventi:
        for evento in f_eventi:
            evento = evento.rstrip().split(", ")
            codice_evento = evento[0]
            valore_evento = evento[1:]
            d_eventi[codice_evento] = valore_evento

    with open("iscrizioni.txt", "r") as f_iscrizioni:
        for iscrizione in f_iscrizioni:
            iscrizione = iscrizione.rstrip().split(", ")
            l_iscrizioni.append(iscrizione)

    calcola_spesa(d_eventi, l_iscrizioni)
    calcola_ingressi(d_eventi, l_iscrizioni)
    calcola_eventi_per_anno(l_iscrizioni)


main()


def calcola_guadagno(l_voli: list, d_tratte: dict):
    d_guadagni = dict()
    f_guadagni = open("guadagni.txt", "w")

    for volo in l_voli:
        compagnia = volo[3]
        cod_tratta = volo[1]
        tratta = d_tratte[cod_tratta]
        costo = float(tratta[2])
        n_passeggeri = int(volo[2])
        guadagno = costo * n_passeggeri

        if compagnia in d_guadagni.keys():
            d_guadagni[compagnia] += guadagno
        else:
            d_guadagni[compagnia] = guadagno

        for compagnia, guadagno_tot in d_guadagni.keys():
            f_guadagni.write(f"{compagnia}: {guadagno_tot:.2f} euro\n")


def calcola_numero_passeggeri(l_voli: list, d_tratte: dict):
    d_partenze = dict()
    d_arrivi = dict()
    f_partenze = open("partenze.txt", "w")
    f_arrivi = open("arrivi.txt", "w")

    for volo in l_voli:
        cod_tratta = volo[1]
        n_passeggi = int(volo[2])
        tratta = d_tratte[cod_tratta]
        partenza = tratta[0]
        arrivo = tratta[1]

        if partenza in d_partenze.keys():
            d_partenze[partenza] += n_passeggi
        else:
            d_partenze[partenza] = n_passeggi

        if arrivo in d_arrivi.keys():
            d_arrivi[arrivo] += n_passeggi
        else:
            d_arrivi[arrivo] += n_passeggi

    dati_arrivo = sorted(d_arrivi.items(), key=lambda x: x[1])
    for aereoporto, num_passeggeri in dati_arrivo:
        f_arrivi.write(f"{aereoporto}: {num_passeggeri}\n")

    dati_partenze = sorted(d_partenze.items(), key=lambda x: x[1])
    for aereoporto, num_passeggeri in dati_partenze:
        f_partenze.write(f"{aereoporto}: {num_passeggeri}\n")


def main():
    # leggo voli.txt e creo
    l_voli = list()

    # leggo tratte.txt e creo
    d_tratte = dict()

    # chiamo funzioni
    calcola_guadagno(l_voli, d_tratte)
    calcola_numero_passeggeri(l_voli, d_tratte)


main()


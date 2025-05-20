def calcola_ricavi_per_anno(l_prenotazioni, d_films):
    d_ricavi = dict()

    f_ricavi = open("ricavi_per_anno.txt", "w", encoding="UTF-8")
    for prenotazione in l_prenotazioni:
        anno = prenotazione[3]  # nota non e' necessario int() perche' anno e' usata
                                # come chiave e non per eseguire calcoli
        num_biglietti = int(prenotazione[2])
        codice_film = prenotazione[0]

        film = d_films[codice_film]
        prezzo_biglietto = float(film[2])

        ricavo = num_biglietti * prezzo_biglietto
        if anno in d_ricavi.keys():
            d_ricavi[anno] += ricavo
        else:
            d_ricavi[anno] = ricavo

    for anno, ricavo_totale in d_ricavi.items():
        f_ricavi.write(f"{anno}, {ricavo_totale}\n")

    f_ricavi.close()


def calcola_biglietti_venduti(l_prenotazioni, d_films):
    d_biglietti = dict()

    f_biglietti = open("biglietti_venduti.txt", "w", encoding="UTF-8")
    for prenotazione in l_prenotazioni:
        codice_film = prenotazione[0]
        num_biglietti = int(prenotazione[2])

        film = d_films[codice_film]
        nome_film = film[0]

        if nome_film in d_biglietti.keys():
            d_biglietti[nome_film] += num_biglietti
        else:
            d_biglietti[nome_film] = num_biglietti

    sorted_biglietti = sorted(d_biglietti.items(), key=lambda x: x[1], reverse=True)
    for nome_film, biglietti_totali in sorted_biglietti:
        f_biglietti.write(f"{nome_film}: {biglietti_totali}\n")

    f_biglietti.close()


def main():
    d_films = dict()
    l_prenotazioni = list()

    f_films = open("film.txt", "r", encoding="UTF-8")
    for film in f_films:
        film = film.rstrip().split(", ")
        codice_film = film[0]
        valore_film = film[1:]
        d_films[codice_film] = valore_film
    f_films.close()

    f_prenotazioni = open("prenotazioni_cinema.txt", "r", encoding="UTF-8")
    for prenotazione in f_prenotazioni:
        prenotazione = prenotazione.rstrip().split(", ")
        l_prenotazioni.append(prenotazione)
    f_prenotazioni.close()

    calcola_ricavi_per_anno(l_prenotazioni, d_films)
    calcola_biglietti_venduti(l_prenotazioni, d_films)


main()


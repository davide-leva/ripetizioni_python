def read_dict(filename: str):
    """Legge il file passato da parametro e restiuisce un dizionario
    che rappresenta i dati contenuti al suo interno"""

    data = dict()

    file = open(filename, "r")
    for line in file:
        line = line.rstrip().split(" ")
        key = line[0]
        values = line[1:]
        data[key] = values

    return data


def write_dict(d: dict, filename: str):
    file = open(filename, "w")

    for key, value in d.items():
        file.write(f"{key} {value}\n")


def read_list(filename: str):
    """Restituisce il file passato da parametro come lista di lista"""

    data = list()

    file = open(filename, "r")
    for line in file:
        line = line.rstrip().split(" ")
        data.append(line)

    return data


def spesa_studenti(d_insegnati: dict, l_lezioni: list):
    """Restiuisce un dizionario che associa ogni studenti a quanto ha speso"""

    # Creo l'insieme dei codici degli studenti
    s_studenti = set()
    for lezione in l_lezioni:
        s_studenti.add(lezione[1])

    d_spesa_studenti = dict()

    for codice_studente in sorted(s_studenti):
        somma = 0
        for lezione in l_lezioni:
            if lezione[1] == codice_studente:
                ore_prenotate = int(lezione[2])
                insegnante = d_insegnati[lezione[0]]
                tariffa = int(insegnante[1])
                prezzo_lezione = ore_prenotate * tariffa
                somma += prezzo_lezione

        d_spesa_studenti[codice_studente] = somma

    return d_spesa_studenti


def main():
    d_insegnanti = read_dict("insegnanti.txt")
    l_lezioni = read_list("lezioni.txt")

    d_spesa_studenti = spesa_studenti(d_insegnanti, l_lezioni)
    write_dict(d_spesa_studenti, "spesa_studenti.txt")


main()

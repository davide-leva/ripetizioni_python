def file_to_dict(filename):
    file = open(filename, "r")
    data = dict()

    for line in file:
        obj = line.rstrip().split(";")
        data[obj[0]] = obj[1:]

    file.close()
    return data


def file_to_list(filename):
    file = open(filename, "r")
    data = list()

    for line in file:
        obj = line.rstrip().split(";")
        data.append(obj)

    file.close()
    return data


def calcola_spesa_cliente(d_clienti: dict, l_noleggi: list):
    """Restiuisce un dizionario in cui ogni cliente ha la spesa effettuata"""

    d_spese = dict()

    for cod_fiscale in d_clienti.keys():
        spesa_tot = 0
        for noleggio in l_noleggi:
            if noleggio[1] == cod_fiscale:
                km_percorsi = float(noleggio[3])
                tariffa = float(noleggio[4])
                spesa_tot += km_percorsi * tariffa
        d_spese[cod_fiscale] = spesa_tot

    return d_spese


def calcola_guadagno_compagnia(l_noleggi: list):
    """Restituisce un dizionario in cui ogni compagnia ha il guadagno fatto"""

    s_compagnie = set()
    d_guadagni = dict()

    for noleggio in l_noleggi:
        compagnia = noleggio[2]
        s_compagnie.add(compagnia)

    for compagnia in s_compagnie:
        guadagno_tot = 0
        for noleggio in l_noleggi:
            if noleggio[2] == compagnia:
                km_percorsi = float(noleggio[3])
                tariffa = float(noleggio[4])
                guadagno_tot += km_percorsi * tariffa

        d_guadagni[compagnia] = guadagno_tot

    return d_guadagni


def numero_macchine_compagnia():
    """Restituisce il numero di macchina per ogni compagnia"""
    pass


def colore_preferito():
    """Il colore / i colori più frequenti nelle macchine"""
    pass


def calcola_km_cliente():
    """Restituisce i km percorsi da ogni cliente"""
    pass


def spesa_media_cliente():
    """Restituisce la spesa media per km di ogni cliente"""
    pass


def main():
    # 1 Parte. lettura dei file di input
    d_clienti = file_to_dict("clienti.txt")
    d_macchine = file_to_dict("macchine.txt")
    l_noleggi = file_to_list("noleggi.txt")

    # 2 Parte. chiameta delle varie funzioni
    d_spese = calcola_spesa_cliente(d_clienti, l_noleggi)
    for cliente, spesa in d_spese.items():
        print(f" * {cliente} ha speso {spesa:>8.2f}€")

    d_guadagni = calcola_guadagno_compagnia(l_noleggi)
    for compagnia, guadagno in d_guadagni.items():
        print(f" * {compagnia} ha guadagnato {guadagno:>8.2f}€")

if __name__ == '__main__':
    main()

def calcola_spesa_clienti(l_prenotazioni: list, d_corsi: dict):
    with open("spesa_clienti.txt", "w") as f_spesa:
        spesa = dict()

        for prenotazione in l_prenotazioni:
            codice_corso = prenotazione[0]
            codice_cliente = prenotazione[1]
            numero_lezioni = int(prenotazione[2])

            corso = d_corsi[codice_corso]
            prezzo_lezione = float(corso[2])
            
            costo = numero_lezioni * prezzo_lezione
            if codice_cliente in spesa.keys():
                spesa[codice_cliente] += costo
            else:
                spesa[codice_cliente] = costo

        for codice_cliente, spesa_tot in spesa.items():
            f_spesa.write(f"{codice_cliente}, {spesa_tot}\n")


def calcola_numero_lezioni(l_prenotazioni: list, d_corsi: dict):
    with open("prenotazioni_effettuate.txt", "w") as f_pren_eff:
        lezioni = dict()

        for prenotazione in l_prenotazioni:
            codice_corso = prenotazione[0]
            numero_lezioni = int(prenotazione[2])

            corso = d_corsi[codice_corso]
            nome_corso = corso[0]

            if nome_corso in lezioni.keys():
                lezioni[nome_corso] += numero_lezioni
            else:
                lezioni[nome_corso] = numero_lezioni

        sorted_lezioni = sorted(lezioni.items(), key=lambda x: x[1], reverse=True)
        for nome_corso, numero_prenotazioni in sorted_lezioni:
            f_pren_eff.write(f"{nome_corso}: {numero_prenotazioni}\n")


def main():
    d_corsi = dict()
    with open("corsi.txt", "r") as f_corsi:
        for corso in f_corsi:
            corso = corso.rstrip().split(", ")
            chiave = corso[0]
            valore = corso[1:]
            d_corsi[chiave] = valore

    l_prenotazioni = list()
    with open("prenotazioni.txt", "r") as f_prenotazioni:
        for prenotazione in f_prenotazioni:
            prenotazione = prenotazione.rstrip().split(", ")
            l_prenotazioni.append(prenotazione)

    calcola_spesa_clienti(l_prenotazioni, d_corsi)
    calcola_numero_lezioni(l_prenotazioni, d_corsi)


main()

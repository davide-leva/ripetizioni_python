def crea_file_spese_pazienti(l_pazienti, l_prestazioni):
    f_spese_pazienti = open("spese_pazienti.txt", "w")
    for paziente in l_pazienti:
        f_spese_pazienti.write(f"{paziente[0]}, {paziente[1]} ")
        for prestazione in l_prestazioni:
            if prestazione[0] == paziente[0]:
                f_spese_pazienti.write(f"{prestazione[1]}: {prestazione[2]} ")
        f_spese_pazienti.write("\n")
    f_spese_pazienti.close()


def crea_file_spesa_totale(l_pazienti, l_prestazioni):
    f_spesa_totale = open("spesa_totale.txt", "w")
    for paziente in l_pazienti:
        totale = float(paziente[-1]) #importo residuo
        for prestazione in l_prestazioni:
            if prestazione[0] == paziente[0]:
                totale += float(prestazione[2])

        f_spesa_totale.write(f"{paziente[1]} {paziente[2]}: {totale}\n")
    f_spesa_totale.close()


def main():
    l_pazienti = []
    l_prestazioni = []

    f_pazienti = open("pazienti.txt", "r")
    for paziente in f_pazienti:
        paziente = paziente.strip().split(", ")
        l_pazienti.append(paziente)
    f_pazienti.close()

    f_prestazioni = open("prestazioni.txt", "r")
    for prestazione in f_prestazioni:
        prestazione = prestazione.strip().split(", ")
        l_prestazioni.append(prestazione)
    f_prestazioni.close()

    crea_file_spese_pazienti(l_pazienti, l_prestazioni)
    crea_file_spesa_totale(l_pazienti, l_prestazioni)


main()

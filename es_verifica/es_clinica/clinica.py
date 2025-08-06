def crea_file_spese_clienti(l_pazienti, l_prestazioni):
  f_spese_clienti = open("spese_clienti.txt", "w", encoding="UTF-8")

  for paziente in l_pazienti:
    nome = paziente[1]
    cognome = paziente[2]
    print(f"{nome} {cognome} ", end="", file=f_spese_clienti)
    for prestazione in l_prestazioni:
      tipo = prestazione[1]
      costo = int(prestazione[2])
      if paziente[0] == prestazione[0]:
        print(f"{tipo}: {costo} ", end=" ", file=f_spese_clienti)
    print(file=f_spese_clienti)

  f_spese_clienti.close()


def crea_file_spesa_totale(l_pazienti, l_prestazioni):
  f_spesa_totale = open("spesa_totale.txt", "w", encoding="UTF-8")

  for paziente in l_pazienti:
    importo_prestazioni = 0
    nome = paziente[1]
    cognome = paziente[2]
    importo_residuo = int(paziente[-1])
    for prestazione in l_prestazioni:
      if paziente[0] == prestazione[0]:
        costo = int(prestazione[2])
        importo_prestazioni += costo
    spesa_totale = importo_prestazioni + importo_residuo
    print(f"{nome} {cognome}: {spesa_totale}", file=f_spesa_totale)

  f_spesa_totale.close()


def main():
  l_pazienti = []
  l_prestazioni = []

  f_pazienti = open("pazienti.txt", "r", encoding="UTF-8")
  for paziente in f_pazienti:
    paziente = paziente.rstrip().split(", ")
    l_pazienti.append(paziente)
  f_pazienti.close()

  f_prestazioni = open("prestazioni.txt", "r", encoding="UTF-8")
  for prestazione in f_prestazioni:
    prestazione = prestazione.rstrip().split(", ")
    l_prestazioni.append(prestazione)
  f_prestazioni.close()

  crea_file_spese_clienti(l_pazienti, l_prestazioni)
  crea_file_spesa_totale(l_pazienti, l_prestazioni)


main()
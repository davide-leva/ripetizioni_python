# Strutture di input
lista_squadre = []
lista_partite = []
lista_attaccanti = []

# 1. Input di lista_squadre
print("INSERIMENTO squadre:\nInserisci le squadre con il formato comune_sede anno_fondazione nome_squadra\n"
      "Premi ENTER per smettere l'inserimento\n")
while True:
    dati_squadra = input("Inserisci squadra: ")

    if dati_squadra == "":
        break

    squadra = dati_squadra.split()
    lista_squadre.append(squadra)

# 2. Input di lista_partite
print("INSERIMENTO partite:\nInserisci le partite con il formato squadra_vincente squadra_perdente gol_vincente "
      "gol_perdente\nPremi ENTER per smettere l'inserimento\n")
while True:
    dati_partita = input("Inserisci partita: ")

    if dati_partita == "":
        break

    partita = dati_partita.split()
    lista_partite.append(partita)

# 3. Input di lista_attaccanti
print("INSERIMENTO attaccanti:\nInserisci gli attaccanti con il formato nome cognome squadra gol_segnati "
      "Premi ENTER per smettere l'inserimento\n")
while True:
    dati_attaccante = input("Inserisci attaccante: ")

    if dati_attaccante == "":
        break

    attaccante = dati_attaccante.split()
    lista_squadre.append(attaccante)

# Strutture di output
lista_statistiche_squadre = []
lista_migliori_attaccanti = []

# 4. Calcolo di lista_statistiche_squadre
for squadra in lista_squadre:
    punti_totali = 0
    gol_fatti = 0
    gol_subiti = 0
    for partita in lista_partite:
        if squadra[-1] == partita[0]:
            punti_totali += 3
            gol_fatti += int(partita[2])
            gol_subiti += int(partita[3])
        elif squadra[-1] == partita[1]:     # attenzione a non usare solo else altrimenti attribuisce anche partite
                                            # che non sono della squadra
            punti_totali += 1
            gol_fatti += int(partita[3])
            gol_subiti += int(partita[2])

    informazioni = [squadra[-1], punti_totali, gol_fatti, gol_subiti]
    lista_statistiche_squadre.append(informazioni)

# 5. Calcolo di lista_migliori_attaccanti
for squadra in lista_squadre:
    max_gol = 0
    miglior_attaccante = []
    for attaccante in lista_attaccanti:
        if attaccante[2] == squadra[-1]:
            if int(attaccante[3]) > max_gol:
                max_gol = int(attaccante[3])
                miglior_attaccante = attaccante

    informazioni = [squadra[-1], miglior_attaccante]
    lista_migliori_attaccanti.append(informazioni)

# 6. Output per lista_statistiche_squadre
for informazioni in lista_statistiche_squadre:
    print(informazioni[0])
    print("\t* punti:", informazioni[1], "pt")
    print("\t* gol fatti:", informazioni[2], "gol")
    print("\t* gol subiti:", informazioni[3], "gol")
    print()

# 7. Output per lista_migliori_attaccanti
for informazioni in lista_migliori_attaccanti:
    attaccante = informazioni[1]
    print("Il giocatore", attaccante[0], attaccante[1], "è il miglior attaccante per", informazioni[0], "con",
          attaccante[-1], "gol")
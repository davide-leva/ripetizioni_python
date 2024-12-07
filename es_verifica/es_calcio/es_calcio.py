lista_squadre = []
lista_partite = []
lista_attaccanti = []

file_squadre = open("squadre.txt")
for dati_squadra in file_squadre.readlines():
    squadra = dati_squadra.split()
    lista_squadre.append(squadra)

file_partite = open("partite.txt")
for dati_partita in file_partite.readlines():
    partita = dati_partita.split()
    lista_partite.append(partita)

file_attaccanti = open("attaccanti.txt")
for dati_attaccante in file_attaccanti.readlines():
    attaccante = dati_attaccante.split()
    lista_attaccanti.append(attaccante)

lista_statistiche_squadre = []
for squadra in lista_squadre:
    punti_tot = 0
    gol_fatti = 0
    gol_subiti = 0
    for partita in lista_partite:
        if squadra[2] == partita[0]: # la squadra ha vinto
            punti_tot += 3
            gol_fatti += int(partita[2])
            gol_subiti += int(partita[3])
        elif squadra[2] == partita[1]: # la squadra ha perso
            punti_tot += 1
            gol_fatti += int(partita[3])
            gol_subiti += int(partita[2])
        # serve l'elif perchè con l'else considera partite che non sono di una determinata squadra

    info = [squadra[2], punti_tot, gol_fatti, gol_subiti]
    lista_statistiche_squadre.append(info)

lista_migliori_attaccanti = []
for squadra in lista_squadre:
    max_gol = 0
    miglior_giocatore = []

    for attaccante in lista_attaccanti:
        if attaccante[2] == squadra[2]:
            if int(attaccante[3]) > max_gol:
                max_gol = int(attaccante[3])
                miglior_giocatore = attaccante

    info = [squadra[2], miglior_giocatore[0], miglior_giocatore[1], max_gol]
    lista_migliori_attaccanti.append(info)

lista_statistiche_squadre.sort(key=lambda x: x[1], reverse=True)

print("\nClassifica:")
for info in lista_statistiche_squadre:
    print(info[0])
    print("\t* punti:", info[1])
    print("\t* gol fatti:", info[2])
    print("\t* gol subiti:", info[3])

print("\nMigliori attaccanti:")
for info in lista_migliori_attaccanti:
    print(f"Il giocatore {info[1]} {info[2]} è il miglior attaccante per {info[0]} con {info[3]} gol")
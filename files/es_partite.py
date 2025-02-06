lista_giocatori = []
lista_partite = []
lista_statistiche = []

with open("data/giocatori.txt", "r", encoding="UTF-8") as file_giocatori:
    for linea in file_giocatori:
        giocatore = linea.strip().split()
        codice = giocatore[0]
        nome = giocatore[1]
        eta = int(giocatore[2])
        info = [codice, nome, eta]
        lista_giocatori.append(info)

file_partite = open("data/partite.txt", "r", encoding="UTF-8")

for linea in file_partite:
    partita = linea.strip().split()
    codice = partita[0]
    codice_giocatore = partita[1]
    punti = int(partita[2])
    durata = int(partita[3])
    info = [codice, codice_giocatore, punti, durata]
    lista_partite.append(info)

file_partite.close()

for giocatore in lista_giocatori:
    somma_punti = 0
    somma_durata = 0
    numero_partite = 0
    for partita in lista_partite:
        if partita[1] == giocatore[0]:
            somma_punti += partita[2]
            somma_durata += partita[3]
            numero_partite += 1

    media_punti = somma_punti / numero_partite
    media_durata = somma_durata / numero_partite
    info = [giocatore[1], str(media_punti), str(media_durata), str(numero_partite)]
    lista_statistiche.append(info)

with open("data/statistiche.txt", "w", encoding="UTF-8") as file_statistiche:
    for statistica in lista_statistiche:
        print(" ".join(statistica), file=file_statistiche)


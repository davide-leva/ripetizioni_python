lista_studenti = []
lista_appelli = []
lista_voti = []
lista_esami = []
lista_medie_esami = []

while True:
    dati_studente = input("Inserisci ...:")
    studente = dati_studente.split(' ')

    lista_studenti.append(studente)

    domanda = input("Vuoi continuare (si/no)? ")
    if domanda.lower() == 'no':
        break

while True:
    dati_appello = input("Inserisci ...:")
    appello = dati_appello.split(' ')

    lista_appelli.append(appello)

    domanda = input("Vuoi continuare (si/no)? ")
    if domanda.lower() == 'no':
        break

for studente in lista_studenti:
    somma_voti = 0
    numero_voti = 0
    for appello in lista_appelli:
        if studente[0] == appello[0]:
            numero_voti += 1
            somma_voti += int(appello[-1])

    if numero_voti > 0:
        media_voti = somma_voti / numero_voti
        media_laurea = round(int(media_voti / 30 * 110))
        voto_finale = media_laurea + int(studente[-1])
        if voto_finale > 110:
            voto_finale = '110 LODE'

        informazioni = [studente[0], studente[1], studente[2], media_voti, media_laurea, voto_finale]
        lista_voti.append(informazioni)

for appello in lista_appelli:
    nome_esame = ' '.join(appello[1:-2])
    if nome_esame not in lista_esami:
        lista_esami.append(nome_esame)

for esame in lista_esami:
    somma_voti = 0
    numero_voti = 0
    for appello in lista_appelli:
        if ' '.join(appello[1:-2]) == esame:
            somma_voti += int(appello[-1])
            numero_voti += 1

    media_voti = somma_voti / numero_voti
    informazioni = [esame, media_voti]
    lista_medie_esami.append(informazioni)


for elemento in lista_voti:
    print(elemento[1] + " " + elemento[2])
    print("\t* media esami:", elemento[3])
    print("\t* media laurea:", elemento[4])
    print("\t* voto laurea: ", elemento[5])
    print()

min_voto = 30
min_esame = []
max_voto = 0
max_esame = []

for elemento in lista_medie_esami:
    if elemento[1] > max_voto:
        max_voto = elemento[1]
        max_esame = elemento

    if elemento[1] < min_voto:
        min_voto = elemento[1]
        min_esame = elemento

print("L'esame piu' facile e'", max_esame[0], "con voto medio", max_esame[1])
print("L'esame piu' difficile e'", min_esame[0], "con voto medio", min_esame[1])
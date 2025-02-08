lista_studenti = []
with open("studenti.txt") as file_studenti:
    for dati_studente in file_studenti:
        studente = dati_studente.split()
        lista_studenti.append(studente)

lista_corsi = []
with open("corsi.txt") as file_corsi:
    for dati_corso in file_corsi:
        corso = dati_corso.split()
        lista_corsi.append(corso)

lista_ore_totali = []
for studente in lista_studenti:
    ore_frequentate = 0
    for corso in lista_corsi:
        if studente[0] == corso[0]:
            ore_frequentate += int(corso[2])
    
    informazioni = [studente[0], studente[1], studente[2], str(ore_frequentate)]
    if ore_frequentate > 6:
        informazioni.append('Dedicato')
    lista_ore_totali.append(informazioni)

for informazioni in lista_ore_totali:
    print(' '.join(informazioni))

lista_spesa_totale = []
for studente in lista_studenti:
    spesa_totale = 0
    lista_corsi_studente = []
    for corso in lista_corsi:
        if studente[0] == corso[0]:
            spesa_totale += int(corso[2]) * int(corso[3])
            lista_corsi_studente.append(corso[1])

    if spesa_totale != 0:
        corsi = ' '.join(lista_corsi_studente)
        nome = ' '.join(studente[3:])
        informazioni = [studente[0], nome, str(spesa_totale), corsi]
        lista_spesa_totale.append(informazioni)

for informazioni in lista_spesa_totale:
    print(' '.join(informazioni))
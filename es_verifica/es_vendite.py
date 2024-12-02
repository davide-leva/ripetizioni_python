lista_clienti = []
lista_vendite = []
lista_premio = []
lista_spesa_media = []
lista_spesa_annua = []

# 1. Input (clienti)
while True:
    dati_cliente = input("Inserisci codice fiscale, numero di tessera, nome e cognome, città e regione di residenza: ")
    if dati_cliente == "":
        break

    cliente = dati_cliente.split(' ')
    lista_clienti.append(cliente)

# 2. Input (vendite)
while True:
    dati_vendite = input("Inerisci numero tessera, prodotto, costo unitario, quantità, punti scontrino e anno di "
                         "vendita")

    if dati_vendite == "":
        break

    vendita = dati_vendite.split(' ')
    lista_vendite.append(vendita)

# 3. Algoritmo (premio)
for cliente in lista_clienti:
    punti_tot = 0

    for vendita in lista_vendite:
        if cliente[1] == vendita[0]:
            punti_tot += int(vendita[4])

    informazioni = [cliente[0], cliente[1], str(punti_tot)]
    if punti_tot > 80:
        informazioni.append('Diritto premio')
    lista_premio.append(informazioni)

# 4. Algoritmo (spesa media)
for cliente in lista_clienti:
    costo_totale = 0
    numero_spese = 0

    for vendita in lista_vendite:
        if cliente[1] == vendita[0]:
            costo_totale += int(vendita[2]) * int(vendita[3])
            numero_spese += 1

    if numero_spese != 0:
        spesa_media = costo_totale / numero_spese
        informazioni = [cliente[1], cliente[3], str(spesa_media)]
        lista_spesa_media.append(informazioni)


for anno in range(2019, 2024):
    spesa_tot = 0
    for vendita in lista_vendite:
        if int(vendita[-1]) == anno:
            spesa_tot += int(vendita[2]) * int(vendita[3])

    informazioni = [str(anno), spesa_tot]
    lista_spesa_annua.append(informazioni)


# 5. Output (premio)
for elemento in lista_premio:
    print(' '.join(elemento))

# 6. Output (spesa media)
for elemento in lista_spesa_media:
    print(' '.join(elemento))

for elemento in lista_spesa_annua:
    print(' '.join(elemento))
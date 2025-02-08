lista_libri = []
lista_acquisti = []

print("INSERIMENTO LIBRI")
print("Informazioni: codice_libro, titolo, prezzo, copie_disponibili per ogni libro")
while True:
    dati_libro = input("Inserisci libro: ")

    if dati_libro == "":
        break

    libro = dati_libro.split()
    lista_libri.append(libro)


print("INSERIMENTO ACQUISTI")
print("Informazioni: codice_libro, codice_cliente, quantità_acquistata, anno_acquisto")
while True:
    dati_acquisto = input("Inserisci acquisto: ")

    if dati_acquisto == "":
        break

    acquisto = dati_acquisto.split()
    lista_acquisti.append(acquisto)


lista_rimanenze = []
for libro in lista_libri:
    n_acquistati = 0
    for acquisto in lista_acquisti:
        if libro[0] == acquisto[0]:
            n_acquistati += int(acquisto[2])
    
    n_rimasti = int(libro[-1]) - n_acquistati
    titolo = ' '.join(libro[1:-2]) # Se dice che il titolo sarà tutto attaccato invece che fare questo metti direttamente libro[1] in informazioni
    informazioni = [libro[0], titolo, str(n_rimasti)]
    if (n_rimasti == 0):
        informazioni.append('ESAURITO')
    lista_rimanenze.append(informazioni)

for informazioni in lista_rimanenze:
    print(' '.join(informazioni))


lista_clienti = []
for acquisto in lista_acquisti:
    if acquisto[1] not in lista_clienti:
        lista_clienti.append(acquisto[1])

lista_libri_clienti = []
for cliente in lista_clienti:
    n_libri_cliente = 0
    for acquisto in lista_acquisti:
        if lista_acquisti[0] == cliente:
            n_libri_cliente += int(acquisto[2])
    
    informazioni.append([cliente, str(n_libri_cliente)])
    lista_libri_clienti.append(informazioni)

for informazioni in lista_acquisti:
    print(' '.joiin(informazioni))
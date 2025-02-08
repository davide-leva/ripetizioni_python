# Strutture dati di input
lista_clienti = []
lista_prenotazioni = []


# Input di lista clienti
dati_cliente = input("Inserisci dati cliente: ")
while dati_cliente != "":
    cliente = dati_cliente.split(' ') # Questa è lista
    lista_clienti.append(cliente)

    dati_cliente = input("Inserisci dati cliente: ")

# Input di lista_prenotazioni
while True:
    dati_prenotazioni = input("Inserisci dati prenotazione: ")
    
    if dati_prenotazioni == "":
        break

    prenotazione = dati_prenotazioni.split(' ')
    lista_prenotazioni.append(prenotazione)

lista_soggiorni_totali = []

for cliente in lista_clienti:
    giorni_totali = 0

    for prenotazione in lista_prenotazioni:
        if prenotazione[0] == cliente[0]:
            giorni_totali += int(prenotazione[3])

    informazioni = [cliente[0], cliente[1], cliente[2], str(giorni_totali)]
    if giorni_totali >= 100:
        informazioni.append('Ospite Premium')

    lista_soggiorni_totali.append(informazioni)    

print('NUMERO GIORNI')
for informazioni in lista_soggiorni_totali:
    print(' '.join(informazioni))

lista_costo_totale = []
for cliente in lista_clienti:
    spesa_totale = 0

    for prenotazione in lista_prenotazioni:
        if prenotazione[0] == cliente[0]:
            #               costo_giornaliero    * durata_soggiorno
            #               costo_soggiorno
            spesa_totale += int(prenotazione[2]) * int(prenotazione[3])

    if spesa_totale != 0:    
        informazioni = [cliente[0], cliente[3], str(spesa_totale)]
        lista_costo_totale.append(informazioni)

print('\nSPESA TOTALE')
for informazioni in lista_costo_totale:
    print(' '.join(informazioni))
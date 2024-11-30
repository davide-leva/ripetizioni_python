lista_noleggi = []
lista_clienti = []
lista_chilometri = []
lista_costo_medio = []

# 1. Input di lista_clienti
while True: # do-while
    loop = input("Vuoi inserire un cliente? (si/no): ")
    if loop.lower() == 'no':
        break

    cliente = input("Inserisci informazioni cliente: ")
    cliente = cliente.split(' ') # separato i campi
    lista_clienti.append(cliente)

# 2. Input di lista_noleggi
while True: # do-while
    loop = input("Vuoi inserire un noleggio? (si/no): ")
    if loop.lower() == 'no':
        break

    noleggio = input("Inserisci informazioni noleggio: ")
    noleggio = noleggio.split(' ') # separato i campi
    lista_noleggi.append(noleggio)

# 3. Algoritmo per lista_chilometri
for cliente in lista_clienti:
    km_tot = 0
    for noleggio in lista_noleggi:
        if cliente[0] == noleggio[0]:
            km_tot += int(noleggio[4])

    informazioni = [cliente[0], cliente[1], cliente[2], km_tot]
    if km_tot > 1000:
        informazioni.append('Cliente fedeltà')
    lista_chilometri.append(informazioni)

# 4. Algoritmo per lista_costo_medio
for cliente in lista_clienti:
    costo_tot = 0
    giorni_tot = 0
    for noleggio in lista_noleggi:
        if cliente[0] == noleggio[0]:
            costo_tot += int(noleggio[2]) * int(noleggio[3])
            giorni_tot += int(noleggio[3])

    if giorni_tot != 0:
        costo_medio = costo_tot / giorni_tot
        informazioni = [cliente[0], cliente[3], costo_medio]
        lista_costo_medio.append(informazioni)

# 5. Output per lista_chilometri
for elemento in lista_chilometri:
    print(' '.join(elemento))

# 6. Output per lista_costo_medio
for elemento in lista_costo_medio:
    print(' '.join(elemento))

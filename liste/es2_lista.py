lista_clienti = [
    ['urrtn6576c75', 'paolino', 'paperino', 'asti', 'piemonte'],
    ['eryyy657o477', 'rossi', 'paolo', 'asti', 'piemonte'],
    ['yrryr563k457', 'bianchi', 'pietro', 'trento', 'trentino', 'alto', 'adige'],
    ['ruute763g767', 'verdi', 'arianna', 'trieste', 'friuli', 'venezia', 'giulia'],
    ['eretr524p466', 'caio', 'sempronio', 'bolzano', 'trentino', 'alto', 'adige']
]

lista_acquisti = []
spesa_totale = []

for cliente in lista_clienti:
    spesa = 0
    punti_totali = 0  # sommatore del cliente
    for acquisto in lista_acquisti:  # acquisti
        if cliente[0] == acquisto[0]:  # acquisti di cliente
            costo_item = float(acquisto[2]) * float(acquisto[3])
            spesa += costo_item
            punti_totali += acquisto[4]

    spesa_totale.append([cliente[0], punti_totali, spesa])

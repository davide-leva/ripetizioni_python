def genera_report(lista_clienti, lista_iscrizioni):
    f_report = open("report.txt", "w", encoding="UTF-8")

    for cliente in lista_clienti:
        nome = cliente[1]
        cognome = cliente[2]
        stato = cliente[3]

        num_ingressi = 0
        tot_spesa = 0

        for iscrizione in lista_iscrizioni:
            costo = float(iscrizione[2])

            if cliente[0] == iscrizione[0]:
                num_ingressi += 1
                tot_spesa += costo
        
        if stato == "MEMBER":
            tot_spesa *= 0.9
        elif stato == "VIP":
            tot_spesa *= 0.8
        
        print(f"{nome} {cognome} ha speso {tot_spesa:.2f}€ entrando a {num_ingressi} eventi", file=f_report)
    
    f_report.close()


def genera_presenze(lista_clienti, lista_iscrizioni):
    f_presenze = open("presenze.txt", "w", encoding="UTF-8")

    for cliente in lista_clienti:
        nome = cliente[1]
        cognome = cliente[2]

        print(f"{nome} {cognome}: ", end="", file=f_presenze)
        for iscrizione in lista_iscrizioni:
            evento = iscrizione[1]
            costo = float(iscrizione[2])

            if cliente[0] == iscrizione[0]:
                print(f"{evento} {costo:.2f}€ ", end="", file=f_presenze)
        
        print("", file=f_presenze) # per andare a capo
    
    f_presenze.close()


def main():
    lista_clienti = []
    lista_iscrizioni = []

    f_clienti = open("clienti.txt", "r", encoding="UTF-8")
    for cliente in f_clienti:
        cliente = cliente.rstrip().split(", ")
        lista_clienti.append(cliente)
    f_clienti.close()

    f_iscrizioni = open("iscrizioni.txt", "r", encoding="UTF-8")
    for iscrizione in f_iscrizioni:
        iscrizione = iscrizione.rstrip().split(", ")
        lista_iscrizioni.append(iscrizione)
    f_iscrizioni.close()

    genera_report(lista_clienti, lista_iscrizioni)
    genera_presenze(lista_clienti, lista_iscrizioni)


main()

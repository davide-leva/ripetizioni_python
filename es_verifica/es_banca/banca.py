def autorizza(clienti, transazioni):
    autorizzate = []

    with open("autorizzazioni.txt", "w", encoding="UTF-8") as file:
        for cliente in clienti:
            saldo = cliente[2]
            for transazione in transazioni:
                if transazione[1] == cliente[0]:
                    if transazione[5] == "DARE":
                        if transazione[2] > saldo:
                            print(f"La transazione {transazione[0]} è stata RIFUTATA", file=file)
                            continue
                        else:
                            saldo -= transazione[2]
                    else:
                        saldo += transazione[2]
                    
                    print(f"La transazione {transazione[0]} è stata AUTORIZZATA", file=file)
                    autorizzate.append(transazione)
    
    return autorizzate


def calcola_variazioni(clienti, autorizzate):
    stato_conti = []

    with open("variazioni.txt", "w", encoding="UTF-8") as file:        
        for cliente in clienti:
            saldo = cliente[2]
            guadagno = 0
            spesa = 0
            for transazione in autorizzate:
                if transazione[1] == cliente[0]:
                    if transazione[5] == "DARE":
                        spesa += transazione[2]
                        saldo -= transazione[2]
                    else:
                        guadagno += transazione[2]
                        saldo += transazione[2]

            info = [cliente[0], guadagno, spesa, saldo]
            stato_conti.append(info)
            print(f"{cliente[1]} ha guadagnato {guadagno:.2f}€ e speso {spesa:.2f}€, saldo finale: {saldo:.2f}€", file=file)
    
    return stato_conti


def calcola_premi(clienti, stato_conti):
    with open("premi.txt", "w", encoding="UTF-8") as file:
        for stato in stato_conti:
            for cliente in clienti:
                if stato[0] == cliente[0]:
                    punti = cliente[4] + int(stato[2] // 10)
                    if cliente[3] == "BASIC":
                        cashback = int(stato[2] * 0.01)
                    elif cliente[3] == "NEXT":
                        cashback = int(stato[2] * 0.02)
                    else:
                        cashback = int(stato[2] * 0.03)
            stato.append(punti)
            stato.append(cashback)
            print(f"{cliente[1]} ha accumulato {punti} punti e ha diritto a {cashback}€ di cashback", file=file)
    
    return stato_conti


def aggiorna_conti(clienti, stato_conti):
    with open("clienti.txt", "w", encoding="UTF-8") as file:
        for cliente in clienti:
            for stato in stato_conti:
                if cliente[0] == stato[0]:
                    cliente[2] = stato[3] + stato[5]
                    cliente[4] = stato[4]

                    if cliente[4] > 3000 and cliente[3] != "PREMIUM":
                        cliente[4] -= 3000
                        if cliente[3] == "BASIC":
                            cliente[3] = "NEXT"
                        elif cliente[3] == "NEXT":
                            cliente[3] = "PREMIUM"
                        print(f"Il {cliente[1]} ha raggiunto il livello {cliente[3]}")

                    print(f"{cliente[0]} {cliente[1]} {cliente[2]:.2f} {cliente[3]} {cliente[4]}", file=file)


def sono_tutti_premium(clienti):
    for cliente in clienti:
        if cliente[3] != "PREMIUM":
            return False
        
    return True

def main():
    clienti = []
    with open("clienti.txt", "r") as file:
        for linea in file:
            cliente = linea.strip().split()
            iban = cliente[0]
            nome = " ".join(cliente[1:3])
            bilancio = float(cliente[3])
            tipo = cliente[4]
            punti = int(cliente[5])
            info = [iban, nome, bilancio, tipo, punti]
            clienti.append(info)
    
    transazioni = []
    with open("transazioni.txt", "r") as file:
        for linea in file:
            transazione = linea.strip().split()
            codice = transazione[0]
            iban = transazione[1]
            importo = float(transazione[2])
            data = transazione[3]
            ora = transazione[4]
            direzione = transazione[5]
            info = [codice, iban, importo, data, ora, direzione]
            transazioni.append(info)

    autorizzate = autorizza(clienti, transazioni)
    stato_conti = calcola_variazioni(clienti, autorizzate)
    stato_conti = calcola_premi(clienti, stato_conti)
    aggiorna_conti(clienti, stato_conti)

if __name__ == "__main__":
    main()
    
def calcola_guadagni(lista_negozi, lista_prodotti, lista_vendite):
    lista_guadagni = []
    with open("report.txt", "w") as file_report:
        for negozio in lista_negozi:
            guadagno = 0
            for vendita in lista_vendite:
                for prodotto in lista_prodotti:
                    if vendita[0] == negozio[0] and vendita[1] == prodotto[0]:
                        guadagno += prodotto[2] * vendita[2]
            info = [negozio[0], negozio[1], guadagno]
            lista_guadagni.append(info)
            file_report.write(f"Il negozio {negozio[0]} di {negozio[1]} ha guadagnato {guadagno} euro\n")

    return lista_guadagni


def genera_email(lista_negozi, lista_guadagni, lista_prodotti, lista_vendite):
    for negozio in lista_negozi:
        with open(f"email/{negozio[1].lower()}.txt", "w") as file_email:
            file_email.write("FROM: manager@italmaket.it\n")
            file_email.write(f"TO: {negozio[2]}\n")
            file_email.write(f"SUBJECT: Resoconto del mese\n\n")
            file_email.write(f"Resoconto del mese per il negozio di {negozio[1]} in {negozio[3]}\n")
            
            for guadagno in lista_guadagni:
                if guadagno[0] == negozio[0]:
                    file_email.write(f"Il negozio ha guadagnato {guadagno[2]} euro\n")
            
            file_email.write("E' necessario comprare i seguenti lotti:\n")
            for vendita in lista_vendite:
                for prodotto in lista_prodotti:
                    if vendita[0] == negozio[0] and vendita[1] == prodotto[0]:
                        lotti = int(vendita[2] // prodotto[2])
                        file_email.write(f" - {lotti} lotti di {prodotto[1]}\n")


def main():
    lista_negozi = []
    with open("negozi.txt") as file_negozi:
        for linea in file_negozi:
            negozio = linea.strip().split()
            codice = negozio[0]
            comune = negozio[1]
            email = negozio[2]
            posizione = " ".join(negozio[3:])
            info = [codice, comune, email, posizione]
            lista_negozi.append(info)
    
    lista_prodotti = []
    with open("prodotti.txt") as file_prodotti:
        for linea in file_prodotti:
            prodotto = linea.strip().split()
            codice = prodotto[0]
            nome = " ".join(prodotto[1:-2])
            prezzo = float(prodotto[-2])
            quantita = int(prodotto[-1])
            info = [codice, nome, prezzo, quantita]
            lista_prodotti.append(info)
    
    lista_vendite = []
    with open("vendite.txt") as file_vendite:
        for linea in file_vendite:
            vendita = linea.strip().split()
            codice = vendita[0]
            prodotto = vendita[1]
            quantita = int(vendita[2])
            info = [codice, prodotto, quantita]
            lista_vendite.append(info)

    lista_guadagni = calcola_guadagni(lista_negozi, lista_prodotti, lista_vendite)
    genera_email(lista_negozi, lista_guadagni, lista_prodotti, lista_vendite)


if __name__ == "__main__":
    main()

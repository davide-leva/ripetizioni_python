def main():
    file_corsi=open("Corsi.txt","r",encoding="utf-8")
    file_prenotazioni=open("Prenotazioni.txt","r",encoding="utf-8")
    dizcorsi={}
    lista_prenotazioni=[]
    for riga in file_corsi:
        corso=riga.strip().split(", ")
        dizcorsi[corso[0]]=corso[1:]
    for riga in file_prenotazioni:
        prenotazione=riga.strip().split(", ")
        lista_prenotazioni.append(prenotazione)

    calcola_spese_clienti(lista_prenotazioni, dizcorsi)
    calcola_prenotazioni(lista_prenotazioni, dizcorsi)


def calcola_spese_clienti(lista_prenotazioni, dizcorsi):
    file_spesa=open("Spesa_clienti.txt","w",encoding="utf-8")
    dizspese = {}

    for prenotazione in lista_prenotazioni:
        ccorso = prenotazione[0]
        ccliente = prenotazione[1]
        numlezioni = int(prenotazione[2])

        corso = dizcorsi[ccorso]
        prezzo = float(corso[-2])
        if ccliente in dizspese:
            dizspese[ccliente]+=numlezioni*prezzo
        else:
            dizspese[ccliente]=numlezioni*prezzo

    for ccliente, spesa in dizspese.items():
        file_spesa.write(ccliente +", "+ str(spesa) +"\n")


def calcola_prenotazioni(lista_prenotazioni, dizcorsi):
    file_prenotazioni_effettuate=open("prenotazioni_effettutate.txt","w",encoding="utf-8")
    dizore={}
    for prenotazione in lista_prenotazioni:
        ccorso=prenotazione[0]
        ore=int(prenotazione[-2])
        corso=dizcorsi[ccorso]
        nome=corso[0]
        if nome in dizore:
            dizore[nome] += ore
        else:
            dizore[nome]=ore
    ordinato=sorted(dizore.items(), key=lambda x:x[1], reverse=True)

    for nome, lezioni in ordinato:
        file_prenotazioni_effettuate.write(nome +": "+ str(lezioni)+ "\n")


main()

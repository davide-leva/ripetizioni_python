from idlelib.iomenu import encoding


def genera_media_prodotti(lista_prodotti, lista_recensioni):
    f_media = open("media_prodotti.txt", "w", encoding="UTF-8")

    for prodotto in lista_prodotti:
        nome = prodotto[1]
        categoria = prodotto[2]

        num_voti = 0
        somma_voti = 0

        for recensione in lista_recensioni:
            prezzo = float(recensione[1])

            if prodotto[0] ==  recensione[0]:
                num_voti += 1
                somma_voti += prezzo

        if somma_voti > 0:
            media = somma_voti / num_voti
            print(f"{nome} -- {categoria} -- Media {media}", file=f_media)
        else:
            print(f"{nome} -- {categoria} -- Media N/D", file=f_media)

    f_media.close()


def genera_senza_recensioni(lista_prodotti, lista_recensioni):
    f_recensioni = open("senza_recensioni.txt", "w", encoding="utf-8")

    num_recensiti = 0

    for prodotto in lista_prodotti:
        nome = prodotto[0]
        categoria = prodotto[1]

        num_recensioni = 0

        for recensione in lista_recensioni:
            if prodotto[0] == recensione[0]:
                num_recensioni += 1

        if num_recensioni == 0:
            print(f"{nome} -- {categoria}", file=f_recensioni)
        else:
            num_recensiti += 1

    if num_recensiti == 0:
        print("Nessuno", file=f_recensioni)

    f_recensioni.close()


def main():
    lista_prodotti = []
    lista_recensioni = []

    f_prodotti = open("prodotti.txt", "r", encoding="utf-8")
    for prodotto in f_prodotti:
        prodotto = prodotto.rstrip().split()
        lista_prodotti.append(prodotto)
    f_prodotti.close()

    f_recensioni = open("recensioni.txt", "r", encoding="utf-8")
    for recensione in f_recensioni:
        recensione = recensione.rstrip().split()
        lista_recensioni.append(recensione)
    f_recensioni.close()

    genera_media_prodotti(lista_prodotti, lista_recensioni)
    genera_senza_recensioni(lista_prodotti, lista_recensioni)

main()

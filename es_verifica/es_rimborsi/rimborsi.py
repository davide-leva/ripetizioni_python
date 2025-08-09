def genera_report_prestiti(lista_pagamenti, lista_clienti):
    lista_penali = []

    f_prestiti = open("report_prestiti.txt", "w", encoding="UTF-8")
    for cliente in lista_clienti:
        nome = cliente[1]
        cognome = cliente[2]
        importo = int(cliente[-2])

        totale_pagamenti = 0
        rate_saltate = 0
        totale_penale = 0

        for pagamento in lista_pagamenti:
            if pagamento[0] == cliente[0]:
                importi = [int(rata) for rata in pagamento[1:]]
                totale_pagamenti += sum(importi)
                rate_saltate += importi.count(0)
                totale_penale += 20 * rate_saltate

        if rate_saltate > 3:
            totale_penale += 50

        residuo = importo - totale_pagamenti
        print(f"{nome} {cognome}: Totale pagamenti {totale_pagamenti}€, "
              f"Rate saltate {rate_saltate}, Residuo {residuo}€", file=f_prestiti)
        lista_penali.append([nome, cognome, totale_penale, rate_saltate])
    f_prestiti.close()

    return lista_penali


def genera_rate_penali(lista_penali):
    f_penali = open("report_penali.txt", "w", encoding="UTF-8")

    for cliente in lista_penali:
        nome = cliente[0]
        cognome = cliente[1]
        totale_penale = cliente[2]

        if totale_penale == 0:
            continue

        if totale_penale < 50:
            print(f"{nome} {cognome}: Penale Totale {totale_penale}€, "
                  f"rata unica di {totale_penale:.2f}€", file=f_penali)
        elif totale_penale < 100:
            rata = totale_penale/2
            print(f"{nome} {cognome}: Penale Totale {totale_penale}€, "
                  f"rata 1: {rata:.2f}€, rata 2: {rata:.2f}€", file=f_penali)
        else:
            rata = totale_penale/3
            print(f"{nome} {cognome}: Penale Totale {totale_penale}€, rata 1: {rata:.2f}€,"
                  f" rata 2: {rata:.2f}€, rata 3: {rata:.2f}", file=f_penali)

def main():
    lista_clienti = []
    lista_pagamenti = []

    f_clienti = open("clienti.txt", "r", encoding="UTF-8")
    for cliente in f_clienti:
        cliente = cliente.rstrip().split()
        lista_clienti.append(cliente)
    f_clienti.close()

    f_pagamenti = open("pagamenti.txt", "r", encoding="UTF-8")
    for pagamento in f_pagamenti:
        pagamento = pagamento.rstrip().split()
        lista_pagamenti.append(pagamento)
    f_pagamenti.close()

    lista_penali = genera_report_prestiti(lista_pagamenti, lista_clienti)
    genera_rate_penali(lista_penali)


main()

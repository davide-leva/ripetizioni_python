file_spese = open("spese.txt", "r", encoding="UTF-8")
file_condomini = open("condomini.txt", "r", encoding="UTF-8")

lista_spese = []
for linea in file_spese:
    spesa = linea.strip().split()
    ammontare = int(spesa[-1])
    scala = spesa[-2]
    tipo = " ".join(spesa[:-2]) # Riunisco le parole del tipo in un'unica stringa
    info = [tipo, scala, ammontare]
    lista_spese.append(info)


lista_condomini = []
for linea in file_condomini:
    condomino = linea.strip().split()
    scala = condomino[0]
    nome = " ".join(condomino[2:-2])
    millesimi = int(condomino[-2])
    spese = float(condomino[-1])
    info = [scala, nome, millesimi, spese]
    lista_condomini.append(info)


file_spese.close()
file_condomini.close()

lista_spese_condomino = []
for condomino in lista_condomini:
    info = []
    info.append(condomino[1])
    for spesa in lista_spese:
        if condomino[0] == spesa[1]:
            valore_spesa = spesa[2] * condomino[2] / 1000
            info.append(spesa[0] + ":")
            info.append(valore_spesa)
    lista_spese_condomino.append(info)

file_dettaglio_spese = open("dettaglio_spese.txt", "w", encoding="UTF-8")

for info in lista_spese_condomino:
    print(info[0], end=" ", file=file_dettaglio_spese)
    for spesa in info[1:]:
        print(spesa, end=" ", file=file_dettaglio_spese)
    print("", file=file_dettaglio_spese)

file_dettaglio_spese.close()

file_spesa_totale = open("spesa_totale.txt", "w", encoding="UTF-8")

lista_spesa_totale = []
for condomino in lista_condomini:
    spesa_totale = 0
    for spesa in lista_spese:
        if spesa[1] == condomino[0]:
            spesa_totale += spesa[2]

    spesa_condomino = spesa_totale * condomino[2] / 1000
    info = [condomino[1], str(spesa_condomino)]
    lista_spesa_totale.append(info)

for info in lista_spesa_totale:
    print(" ".join(info), file=file_spesa_totale)

file_spesa_totale.close()

file_rate = open("rate.txt", "w", encoding="UTF-8")

for info in lista_spesa_totale:
    nome = info[0]
    spesa = int(info[1])

    print(nome + " totale: " + str(spesa) + " ", end="", file=file_rate)
    if spesa > 1000:
        for i in range(4):
            print("rata", i + 1, spesa / 4, end=" ", file=file_rate)
    else:
        for i in range(3):
            print("rata", i + 1, spesa / 3, end=" ", file=file_rate)

    print(file=file_rate)

file_rate.close()

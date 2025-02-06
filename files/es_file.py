# Apertura file
file_in = open("data/dati.txt", "r", encoding="UTF-8")
file_out = open("data/log.txt", "a", encoding="UTF-8")

lista_persone = []
lista_persone_corretto = []

for line in file_in:
    line = line.strip().split()
    nome = line[0]
    eta = int(line[1])
    info = [nome, eta]
    lista_persone.append(info)

for persona in lista_persone:
    nome = persona[0]
    eta = persona[1] * 2
    info = [nome, str(eta)]
    lista_persone_corretto.append(info)

for info in lista_persone_corretto:
    print(" ".join(info), file=file_out)

file_in.close()
file_out.close()


file_alunni = open("alunni.txt", "r", encoding="UTF-8")
file_interrogazioni = open("interrogazioni.txt", "r", encoding="UTF-8")
file_media_alunni = open("media_alunni.txt", "w", encoding="UTF-8")
file_materie_suff = open("materie_suff.txt", "w", encoding="UTF-8")

lista_alunni = []
lista_interrogazioni = []
lista_media_alunni = []
lista_materie_suff = []

for linea in file_alunni:
    alunno = linea.rstrip('\n').split()
    matricola = alunno[0]
    nome = " ".join(alunno[1:3])
    info = [matricola, nome]
    lista_alunni.append(info)

for linea in file_interrogazioni:
    interrogazione = linea.rstrip('\n').split()
    matricola = interrogazione[0]
    voto = float(interrogazione[1])
    info = [matricola, voto]
    lista_interrogazioni.append(info)

for alunno in lista_alunni:
    somma_voti = 0
    numero_voti = 0
    for interrogazione in lista_interrogazioni:
        if interrogazione[0] == alunno[0]:
            somma_voti += interrogazione[1]
            numero_voti += 1
    info = [alunno[0], alunno[1]]
    if numero_voti == 0:
        info.append("nessun voto")
    else:
        media_voti = somma_voti / numero_voti
        info.append(str(media_voti))
    lista_media_alunni.append(info)

for media_alunno in lista_media_alunni:
    print(" ".join(media_alunno), file=file_media_alunni)

for alunno in lista_alunni:
    materie_suff = 0
    materie_insuff = 0

file_alunni.close()
file_interrogazioni.close()
file_media_alunni.close()
file_materie_suff.close()

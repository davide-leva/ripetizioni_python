def file_to_dict(filename):
    file = open(filename, "r")
    data = dict()

    for line in file:
        obj = line.rstrip().split(", ")
        data[obj[0]] = obj[1:]

    file.close()
    return data


def calcola_media(studenti, esami):
    medie = {}

    for matricola, studente in studenti.items():
        somma_voti = 0
        numero_voti = 0

        for esame in esami.values():
            if esame[0] == matricola:
                somma_voti += int(esame[2])
                numero_voti += 1

        if numero_voti > 0:
            medie[matricola] = somma_voti/numero_voti

    return medie


def studente_media_max(medie, studenti):
    media_max = 0
    matricola_max = ""

    for matricola, media in medie.items():
        if media > media_max:
            matricola_max = matricola

    studente = studenti[matricola_max]
    print(f"Il miglior Studente è {studente[0]} {studente[1]} residente a {studente[3]} e studia {studente[2]}")

def media_materie(esami, materie):
    medie_materie = dict()

    for codice_mat, materia in materie.items():
        somma_voti = 0
        numero_voti = 0

        for codice_esame, esame in esami.items():
            if codice_mat == esame[1]:
                somma_voti += int(esame[2])
                numero_voti += 1

        if numero_voti > 0:
            medie_materie[codice_mat] = somma_voti / numero_voti

    return medie_materie

def main():
    studenti = file_to_dict("studenti.txt")
    esami = file_to_dict("esami.txt")
    materie = file_to_dict("materie.txt")

    medie = calcola_media(studenti, esami)
    medie_materie = media_materie(esami, materie)

    print(medie_materie)

    while True:
        print("\n1. Calcola la media di ogni studente")
        print("2. Trova studente con miglior media")
        print("3. Media voti di una materia")
        print("4. Esci")
        opzione = int(input("Inserisci opzione > "))
        print()



        if opzione == 1:
            for matricola, media in medie.items():
                studente = studenti[matricola]

                print(f"{studente[0]} {studente[1]} ha media {media:.2f}")
        elif opzione == 2:
            studente_media_max(medie, studenti)
            print()
        elif opzione == 3:
            nome_meteria = input("Di quale materia? ")
            trovata = False
            for codice, materia in materie.items():
                if materia[0] == nome_meteria:
                    trovata = True
                    if codice in medie_materie:
                        media = medie_materie[codice]
                        print(f"La media e' {media:.2f}")
                    else:
                        print("Questa materia non ha esami")

            if not trovata:
                print("Materia non esistente, riprova :P")

        elif opzione == 4:

            break
        else:
            print("Comando errato")

main()

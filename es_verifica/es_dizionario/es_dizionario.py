def file_to_dict(filename):
    file = open(filename, "r")
    data = dict()

    for line in file:
        obj = line.rstrip().split(", ")
        data[obj[0]] = obj[1:]

    file.close()
    return data


def calcola_media(esami: dict, studenti: dict):
    """Restituisce la media dei voti di ogni studente"""

    d_medie = dict()

    for matricola in studenti.keys():
        somma = 0
        counter = 0
        for esame in esami.values():
            if esame[0] == matricola:
                somma += int(esame[2])
                counter += 1

        if counter > 0:
            media = somma / counter
            d_medie[matricola] = media

    return d_medie


def media_materie(nome_materia: str, esami: dict, materie: dict):
    """Restituisce la media della materia passata"""

    codice_materia = ""
    for codice, materia in materie.items():
        if materia[0] == nome_materia:
            codice_materia = codice

    somma = 0
    counter = 0
    for esame in esami.values():
        if esame[1] == codice_materia:
            somma += int(esame[2])
            counter += 1

    if counter > 0:
        print(f"La materia {nome_materia} ha media {somma / counter}")
    elif codice_materia != "":
        print(f"La materia non ha esami")
    else :
        print("La materie non esiste")


def citta_residenza(studenti: dict):
    """Restituisce la/e città con più residenti"""

    d_residenti = dict()

    for studente in studenti.values():
        town = studente[3]
        if town in d_residenti.keys():
            d_residenti[town] += 1
        else:
            d_residenti[town] = 1

    max_residenti = max(d_residenti.values())
    for town, residenti in d_residenti.items():
        if residenti == max_residenti:
            print(town)


def media_dipartimento(nome_dipartimento, docenti: dict, esami: dict):
    """Restituisce la media degli esami """

    somma = 0
    counter = 0

    for codice_docente, docente in docenti.items():
        if docente[2] == nome_dipartimento:
            for esame in esami.values():
                if esame[3] == codice_docente:
                    somma += int(esame[2])
                    counter += 1

    if counter > 0:
        print(f"La media del dipartimento {nome_dipartimento} e' {somma / counter}")
    else:
        print(f"Il dipartimento non ha esami")


def studenti_voto_maggiore(voto_riferimento, nome_materia, materie: dict, esami: dict):
    """Visualizza gli studenti che hanno preso un voto maggiore nella materia specificata"""

    # Cerco il codice della materia
    codice_materia = ""
    for codice, materia in materie.items():
        if materia[0] == nome_materia:
            codice_materia = codice


    print(f"Le matricole degli studenti che hanno preso almeno {voto_riferimento} in {nome_materia} sono: ")
    for esame in esami.values():
        if esame[1] == codice_materia and int(esame[2]) > voto_riferimento:
            print(f"\t* Lo studente {esame[0]}")


def esami_anno_di_corso(anno_di_corso, studenti: dict, esami: dict):
    """Restiutisce il numero di esami sostenuti dagli studenti di un determinato
    anno accademico"""

    counter = 0

    for matricola, studente in studenti.items():
        if int(studente[-1]) == anno_di_corso:
            for esame in esami.values():
                if esame[0] == matricola:
                    counter += 1

    return counter


def main():
    d_studenti = file_to_dict("studenti.txt")
    d_esami = file_to_dict("esami.txt")
    d_docenti = file_to_dict("docenti.txt")
    d_materie = file_to_dict("materie.txt")


main()



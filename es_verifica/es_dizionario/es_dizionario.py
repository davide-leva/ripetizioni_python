def read_dict(filename):
    file = open(filename, "r", encoding="UTF-8")
    data = dict()

    for line in file:
        obj = line.strip().split(", ")
        key = obj[0]
        value = obj[1:]
        data[key] = value

    file.close()
    return data


def sort_dict(d: dict):
    """Restiusce il dizionario ordinato per valori decrescenti"""

    d_sorted = dict()
    values = d.values()
    values = sorted(values, reverse=True) # Con reverse vengono ordinati in modo desc

    while len(values) > 0:
        max = values.pop(0)
        for k, v in d.items():
            if v == max:
                d_sorted[k] = v

    return d_sorted


def calcola_media(d_esami: dict, d_studenti: dict):
    """Restituisce la media dei voti di ogni studente"""

    d_medie = dict()

    for matricola in d_studenti.keys():
        somma = 0
        counter = 0
        for esame in d_esami.values():
            if esame[0] == matricola:
                somma += int(esame[2])
                counter += 1

        if counter > 0:
            media = somma / counter
            d_medie[matricola] = media

    return d_medie


def media_materie(nome_materia: str, esami: dict, materie: dict):
    """Restituisce la media della materia passata"""

    # Esempio di ottenimento di chiave a partire dal valore (inverso)
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
    else:
        print("La materie non esiste")


def citta_residenza(studenti: dict):
    """Restituisce la/e città con più residenti"""

    d_residenti = dict()    # è un dizionario delle occorrenze
                            # ovvero conto quanti residenti ho
                            # per ogni città

    # codice per creare il dict delle occorrenze
    for studente in studenti.values():
        town = studente[3]
        if town in d_residenti.keys():
            d_residenti[town] += 1
        else:
            d_residenti[town] = 1

    # ricerca delle chiavi con valore massimo
    # in un dizionario
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


def esami_per_materia(d_materie: dict, d_esami: dict):
    """Restitusce per ogni materia il numero di esami sostenuti in ordine
    decrescente"""

    d_esami_materie = dict() # materia -> n_esami

    for codice_materia, materia in d_materie.items():
        counter = 0
        for esame in d_esami.values():
            if esame[1] == codice_materia:
                counter += 1

        d_esami_materie[materia[0]] = counter

    return sort_dict(d_esami_materie)


def media_docente(d_docenti: dict, d_esami: dict):
    """Visualizza il docente che ha la media dei voti più bassa"""

    media_docenti = dict()

    # Ho costruito il dizionario che associa ad ogni docente la sua media
    for codice_docente, docente in d_docenti.items():
        somma = 0
        counter = 0
        for esame in d_esami.values():
            if esame[3] == codice_docente:
                somma += int(esame[2])
                counter += 1

        if counter > 0:
            nome_docente = f"{docente[0]} {docente[1]}"
            media_docenti[nome_docente] = somma / counter

    # Cerco la media minima
    min_media = min(media_docenti.values())

    # Devo cercare il docente (chiave) che ha una particolare media (valore)
    print("I docenti con la media minima sono: ")
    for docente, media in media_docenti.items():
        if media == min_media:
            print(f" * {docente}")


def main():
    d_studenti = read_dict("studenti.txt")
    d_esami = read_dict("esami.txt")
    d_docenti = read_dict("docenti.txt")
    d_materie = read_dict("materie.txt")


main()
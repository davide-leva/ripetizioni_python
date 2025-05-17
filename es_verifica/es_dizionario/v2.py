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


def calcola_media(d_esami, d_studenti):
    d_medie={}
    for matricola in d_studenti.keys():
        count=0
        somma=0
        for esame in d_esami.values():
            if esame[0]==matricola:
                somma+=int(esame[2])
                count+=1

        if count>0:
            media=somma/count
            d_medie[matricola]=media

    return d_medie

def media_materia(nome_materia, d_esami, d_materie):
    codice_materia=''
    somma=0
    count=0
    for codice, materia in d_materie.items():
        if materia[0]==nome_materia:
            codice_materia=codice
    for esame in d_esami.values():
        if esame[1]==codice_materia:
            somma+=int(esame[2])
            count+=1
    if count>0:
        media=somma/count
        print(media)



def main():
    d_studenti = read_dict("studenti.txt")
    d_esami = read_dict("esami.txt")
    d_docenti = read_dict("docenti.txt")
    d_materie = read_dict("materie.txt")

    d_medie=calcola_media(d_esami, d_studenti)
    print(d_medie)


main()
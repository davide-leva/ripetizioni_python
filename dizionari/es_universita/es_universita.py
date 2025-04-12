file_studenti = open("studenti.txt", "r")
file_esami = open("esami.txt", "r")
file_materie = open("materie.txt", "r")

studenti = dict() # {}
esami = dict()
materie = dict()

for linea in file_studenti:
    studente = linea.rstrip().split(", ")
            #ID            #DATA
    studenti[studente[0]] = studente[1:]

for linea in file_esami:
    esame = linea.rstrip().split(", ")
    esami[esame[0]] = esame[1:]

for linea in file_materie:
    materia = linea.rstrip().split(", ")
    materie[materia[0]] = materia[1:]

print(esami, studenti, materie)
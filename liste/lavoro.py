# Scrivere un programma che acquisca nel main una lista di persona con il loro anno di nascita e di inizio di lavoro
# Una funzione Persone a cui viene passata questa lista deve restituire una nuova lista con i nomi delle persone e l'età
# che avevano quando hanno iniziato a lavorare.

def persone(lista_dati):
    lista_risultato = []

    for i in range(0, len(lista_dati), 3):
        persona = lista_dati[i]
        anno_nascita = lista_dati[i+1]
        anno_lavoro = lista_dati[i+2]
        anni = anno_lavoro - anno_nascita

        lista_risultato.extend([persona, anni])

    return lista_risultato

def main():
    lista_dati = []

    while True:
        nome = input("Inerisci nome persona: ")

        if nome == "":
            break

        anno_nascita = int(input("Inserisci anno di nascita: "))
        anno_lavoro = int(input("Inserisci primo anno di lavoro: "))

        #lista_dati.append(nome)
        #lista_dati.append(anno_nascita)
        #lista_dati.append(anno_lavoro)

        lista_dati.extend([nome, anno_nascita, anno_lavoro])

    lista_risultato = persone(lista_dati)
    print(lista_risultato)


main()
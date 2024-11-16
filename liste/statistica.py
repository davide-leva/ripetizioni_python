# Inserire una sequenza di numeri positivi che termina per 0
# Tramite una funzione statistiche a cui viene passata la sequenza intera
# calcola la somma dei numeri, il minimo, il massimo, la media, la mediana, che devono essere restituiti come lista

def statistiche(sequenza):
    n = len(sequenza)
    somma = sum(sequenza)
    minimo = min(sequenza)
    massimo = max(sequenza)
    media = somma / n


    sequenza.sort()
    if n % 2 == 0:
        mediana = (sequenza[n//2]+sequenza[n//2-1])/2
    else:
        mediana = sequenza[(n-1)//2]

    return [somma, minimo, massimo, media, mediana]

def main():
    sequenza = []

    while True:
        n = int(input("Inserisci numero: "))

        if n == 0:
            break

        sequenza.append(n)

    stats = statistiche(sequenza)
    print(stats)


main()
LIMITE_MAX = 1.8
LIMITE_MIN = 1.65

media_altezze = 0
n_bassi = 0
n_alti = 0
n_totale = 0

while True:
    prompt = input("Inserisci altezza: ")

    if prompt == "":
        break

    altezza = float(prompt) # conversione ("cast") a float

    if altezza < 0 or altezza > 3:
        print("\tAltezza scartata")
        continue

    media_altezze += altezza
    n_totale += 1

    if altezza < LIMITE_MIN:
        n_bassi += 1
    elif altezza > LIMITE_MAX:
        n_alti += 1

media_altezze /= n_totale

print("La altezza media e':", media_altezze)
print("Il numero di alti e':", n_alti)
print("Il numero di bassi e':", n_bassi)

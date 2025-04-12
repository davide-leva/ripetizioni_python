# Le strutture dati primarie di python
D = dict()
L = list()
S = set()

# Il dizionario crea un'associazione tra una CHIAVE e un VALORE

D['chiave'] = 'valore' # Sto associando chiave a valore
print(D['chiave']) # Resituisce il valore che è associato a chiave
# print(D[2]) attenzione ad usare chiavi che non sono contenute

# Creiamo il dizionario delle altezze delle persone
f = open("persone.txt", "r", encoding="UTF-8")
altezze = dict()

for line in f:
    persona = line.rstrip().split()
    nome = " ".join(persona[0:2])
    altezza = int(persona[2][:-2])

    altezze[nome] = altezza # Associo al nome della persona la sua altezza

for altezza in altezze.values(): # Iterazione su valori
    print(altezza)

for nome in altezze.keys(): # Iterazione su chiavi
    print(nome)

for nome in altezze: # Se non specifico nulla l'iteraizione viene fatta sulle chiavi
    print(nome)

for nome, altezza in altezze.items(): # Iterazione contempoeranea di chiave e valore
    print(f"{nome} {altezza}cm")

altezze.pop("Davide Leva") # Toglie la chiave e il valore corrispondente
altezze.clear() # Pulisce il dizionario

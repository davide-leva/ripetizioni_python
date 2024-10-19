# for i in range(min, max+1):
#   ... (i e' contatore)

# st = "hello world"
# for c in st:
#   ... (c e' un carattere della stringa st, partendo dall'inizio)

# Questo concetto si espande con tutti gli oggetti
# che sono Iterables (iterabili - che si possono scorrere)

# Stampare un carattere alla volta di una stringa
st = "ciao a tutti"
for i in range(0, len(st)):
    print(st[i])

# Con l'approccio pythonesco diventa:
st = "ciao a tutti"
for c in st:
    print(c) # end è il carattere che viene aggiunto dopo l'oggetto da stampare

print()

# Break e continue (sia con for che while)
# break -> interrompre il ciclo
# continue -> salta una singola iterazione

# Esempio FOR

for i in range(0, 10+1):
    if i % 2 == 1:
        continue

    if i == 10:
        print(i)
    else:
        print(i, end=", ")

# Esempio WHILE
# Acquisire una serie di numeri positivi, ne facciamo la somma
# e terminiamo quando viene inserito 0

somma = 0

while True:
    n = int(input("Inserisci numero: "))

    if n == 0:
        break

    somma += n

print(f"La somma e' {somma}")

# While con contatore

i = 0
while i < 10:
    print(i)
    i += 1


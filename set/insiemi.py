import random

insieme = set()

# L'insieme non puo' avere due elementi uguali al suo interno
insieme.add("ciao")
insieme.add("ciao")
print(insieme)

# Creazione con elementi
A = {1, 2, 5, "ciao"}
print(A)

B = {1, 2, 3}
C = {3, 4, 5}

UN = B.union(C) # equivalente a C.union(B)
print('unione', UN)

IN = B.intersection(C) # equivalente a C.intersection(B)
print('intersezione', IN)

# Esempio di controllo di insieme vuoto
A = {1, 2, 3}
B = {"ciao"}
IN = A.intersection(B)

if len(IN) == 0: # len(A) restituisce la sua cardinalita' (il numero di elementi)
    print("L'intersezione è vuota")

A = {1, 4, 6}
B = {4, 8}
D1 = A.difference(B)
D2 = B.difference(A)

print(D1)
print(D2)

# Per avere gli elementi che non sono in comune ovvero
# gli elementi unici in A e unici in B faccio
A = {1, 2, 6, 7}
B = {1, 2, 8, 9}
D1 = A.difference(B) # {6, 7}
D2 = B.difference(A) # {8, 9}
UNICI = D1.union(D2)
X = A.union(B).difference(A.intersection(B))

print(UNICI, X)

# Stampare in un ordine casuale tutti i numeri da 1 a 10
s = set()

while len(s) != 0:
    print(s.pop())

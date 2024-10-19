frase = input("Inserisci frase: ")

vocali = 'aeiouAEIOU'
n_vocali = 0
n_consonanti = 0
n_speciali = 0

for c in frase: # in per scopo iterativo
    if c in vocali: # in per scopo logico di appartenenza
        n_vocali += 1
    elif c.isalpha():
        n_consonanti += 1
    else:
        n_speciali += 1

print(n_vocali, n_consonanti, n_speciali)

print("Ho fatto giusto? ", end="")
if n_speciali + n_consonanti + n_vocali == len(frase):
    print("SI")
else:
    print("NO")


# Scrivere un programma che stampa a terminale un triangolo isoscele di altezza n
# inserita dall'utente in orizzontale

# * n = 3 -> l = 5
# **
# ***
# **
# *

n = int(input("Inserisci altezza: "))

for i in range(2*n-1):
    if i < n:
        for j in range(i+1):
            print("*", end="")
        print()
    else:
        for j in range(2*n-1 - i):
            print("*", end="")
        print()

print("------")

for i in range(2*n-1):
    if i < n:
        print("*"*(i+1))
    else:
        print("*"*(2*n-1 - i))
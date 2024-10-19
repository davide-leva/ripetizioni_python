fattoriale = 1

n = int(input("Inserisci numero: "))

for _ in range(n):
    fattoriale *= n
    n -= 1

print(fattoriale)

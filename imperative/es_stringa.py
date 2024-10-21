# Scrivere un esercizio che una volta acquisite due stringhe indentifichi la maggiore e la minore
# * Stampa quante volte la minore è contenuta nella maggiore
# * Se le lunghezze sono uguali dice se sono uguali o diverse
# * Dice se le due stringhe iniziano entrambe per maiuscola
# * Se finiscono entrambe per maiscuola
# * Se la maggiore termina con la minore
# * Stampa le due stringhe in ordine alfabetico

str1=input("Inserire una stringa di caratteri")
str2=input("Inserire una stinga di caratteri ")

if len(str1) > len(str2):
    s_max = str1
    s_min = str2
else:
    s_max = str2
    s_min = str1

n = s_max.count(s_min)
print(f"La stringa più corta compare {n} volte all'interno di quella più grossa")

if len(str1) == len(str2):
    if str1 == str2:
        print("Le due stringhe sono uguali")
    else:
        print("Le due stringhe non sono uguali")

if str1[0].isupper() and str2[0].isupper():
    print("Le due stringhe iniziano entrambe per maiuscole")
else:
    print("Le due stringhe NON iniziano per maiuscole")

if str1[-1].isupper() and str2[-1].isupper():
    print("Le due stringhe finiscono entrambe per maiuscole")
else:
    print("Le due stringhe NON finiscono per maiuscole")

if s_max.startswith(s_min):
    print("La maggiore inizia con la minore")
else:
    print("La maggiore NON inizia con la minore")

if s_min < s_max:
    print(s_min)
    print(s_max)
else:
    print(s_max)
    print(s_min)

str1 = input("Inserisci stringa: ")
str2 = input("Inserisci stringa: ")

s_max = ""
s_min = ""

if len(str1) > len(str2):
    s_max = str1
    s_min = str2
    n = str1.count(str2)
    print(f"La seconda stringa è contenuta nella prima {n} volte")
elif len(str2) > len(str1):
    s_max = str2
    s_min = str1
    n = str2.count(str1)
    print(f"La prima stringa è contenuta nella seconda {n} volte")
else:
    s_max = str1
    s_min = str2

    if str1 == str2:
        print("Le due stringhe sono uguali")
    else:
        print("Le due stringhe NON sono uguali")

if s_max.endswith(s_min):
    print("La stringa più lunga termina con quella più corta")
else:
    print("La stringa più lunga NON termina con quella più corta")

if str1[0].isupper() and str2[0].isupper():
    print("Le due stringhe iniziano per maiuscola")

if str1[-1].isupper() and str2[-1].isupper():
    print("Le due stringhe finiscono per maiuscola")

if str1 < str2:
    print(str1)
    print(str2)
else:
    print(str2)
    print(str1)
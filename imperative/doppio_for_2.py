# Inserire una stringa da tastiera e trovare la stringa che massimizza il rapporto tra numero di vocali e lunghezza
# della stessa

# ciao a tutti      (iao)/3 = 1
#                   (iao a)/5 < 1

VOCALI = 'aeiouAEIOU'

s = input("Inserisci stringa: ")
len_s = len(s)

max_r = 0
max_v = 0
max_sub = ""


def conta_vocali(s):
    count = 0
    for c in s:
        if c in VOCALI:
            count += 1

    return count


for i in range(0, len_s):
    for j in range(1, len_s+1):
        if i < j:
            sub_s = s[i:j]

            r = conta_vocali(sub_s)/len(sub_s)
            v = conta_vocali(sub_s)
            print(sub_s, r)

            if r > max_r or (r == max_r and v > max_v):
                max_r = r
                max_v = v
                max_sub = sub_s


print("Sottostringa che massimizza il valore:", max_sub)
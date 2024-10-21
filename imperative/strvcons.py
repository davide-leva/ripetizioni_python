VOCALI = "aeiouAEIOU"


def cons_string(str_in):
    str_out = ""

    for c in str_in:
        if c not in VOCALI:
            str_out += c

    return str_out


def crea_string(str1, str2):
    str_cons_1 = cons_string(str1)
    str_cons_2 = cons_string(str2)

    if len(str_cons_1) > len(str_cons_2):
        return str_cons_1 + str_cons_2
    else:
        return str_cons_2 + str_cons_1


def main():
    str_in_1 = input("Inserisci una stringa: ")
    str_in_2 = input("Inserisci una stringa: ")
    strvcons = crea_string(str_in_1, str_in_2)
    print("La stringa diventa", strvcons)


# -- Qui inizia il programma --
if __name__ == '__main__': # Sta roba è una convenzione
    main()

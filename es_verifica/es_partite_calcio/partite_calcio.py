def genera_classifica(lista_squadre, lista_partite):
    lista_perse = []

    f_classifica = open("classfica.txt", "w", encoding="UTF-8")

    for squadra in lista_squadre:
        nome = squadra[1]

        gf = 0
        gs = 0
        p = 0
        n = 0
        v = 0
        pg = 0

        for partita in lista_partite:
            gol_casa = int(partita[3])
            gol_trasferta = int(partita[4])

            # La squadra gioca in casa
            if squadra[0] == partita[1]:
                pg += 1
                gf += gol_casa
                gs += gol_trasferta
                if gol_casa > gol_trasferta:
                    v += 1
                elif gol_casa == gol_trasferta:
                    n += 1
                else:
                    p += 1

            # La squadra gioca in trasferta
            if squadra[0] == partita[2]:
                pg += 1
                gf += gol_trasferta
                gs += gol_trasferta
                if gol_trasferta > gol_casa:
                    v += 1
                elif gol_trasferta == gol_casa:
                    n += 1
                else:
                    p += 1

        diff = gf - gs
        punti = v * 3 + n

        print(f"{nome}: PG {pg} V {v} N {n} P {p} GF {gf} GS {gs} DIFF {diff} PT {punti}", file=f_classifica)
        lista_perse.append([nome, p])

    f_classifica.close()

    return lista_perse


def genera_imbatutti(lista_perse):
    f_imbattute = open("imbattute.txt", "w", encoding="UTF-8")

    n_imbattute = 0

    for squadra in lista_perse:
        nome = squadra[0]
        perse = int(squadra[1])

        if perse == 0:
            n_imbattute += 1
            print(f"{nome}: Imbattute", file=f_imbattute)

    if n_imbattute == 0:
        print("Nessuna squadra è imbattuta", file=f_imbattute)

    f_imbattute.close()


def main():
    lista_squadre = []
    lista_partite = []

    f_squadre = open("squadre.txt", "r", encoding="UTF-8")
    for squadra in f_squadre:
        squadra = squadra.rstrip().split()
        lista_squadre.append(squadra)
    f_squadre.close()

    f_partite = open("partite.txt", "r", encoding="UTF-8")
    for partita in f_partite:
        partita = partita.rstrip().split()
        lista_partite.append(partita)
    f_partite.close()

    lista_perse = genera_classifica(lista_squadre, lista_partite)
    genera_imbatutti(lista_perse)


main()

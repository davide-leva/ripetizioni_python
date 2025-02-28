def combattimento(statistiche, boss):
    if statistiche[1] + statistiche[3] > boss[3] and statistiche[2] + statistiche[3] > boss[2]:
        return True
    else:
        return False


def calcola_statistiche(lista_giocatori, lista_oggetti):
    lista_statistiche = []
    with open("statistiche_giocatori.txt", "w") as file_statistiche:
        for giocatore in lista_giocatori:
            difesa_totale = 0
            attacco_totale = 0
            magia_totale = 0
            for oggetto in lista_oggetti:
                if oggetto[0] in giocatore[2]:
                    difesa_totale += oggetto[2]
                    attacco_totale += oggetto[3]
                    magia_totale += oggetto[4]
            info = [giocatore[1], difesa_totale, attacco_totale, magia_totale]
            lista_statistiche.append(info)
            print(f"Il giocatore {giocatore[1]} ha difesa: {difesa_totale}, attacco: {attacco_totale} e magia: {magia_totale}", file=file_statistiche)
    
    return lista_statistiche


def calcola_reputazione(lista_statistiche, lista_boss):
    lista_reputazioni = []
    with open("reputazioni.txt", "w") as file_reputazioni:
        for statistiche in lista_statistiche:
            numero_boss = 0
            reputazione_totale = 0
            print(f"Il giocatore {statistiche[0]} ha sconfitto ", file=file_reputazioni, end="")
            for boss in lista_boss:
                if combattimento(statistiche, boss):
                    numero_boss += 1
                    reputazione_totale += boss[3]
                    print(f"{boss[1]}, ", file=file_reputazioni, end="")
            
            if numero_boss == 0:
                print("nessun boss", file=file_reputazioni)
            else:
                print(f"ottenendo {reputazione_totale} punti reputazione", file=file_reputazioni)
            info = [statistiche[0], numero_boss, reputazione_totale]
            lista_reputazioni.append(info)
    
    return lista_reputazioni


def miglior_giocatore(lista_reputazioni, stat):
    if stat == "num_boss":
        indice = 1
    else:
        indice = 2
    
    max_valore = 0
    max_giocaotore = ""
    for reputazione in lista_reputazione:
        if reputazione[indice] >= max_valore:
            max_valore = reputazione[indice]
            max_giocaotore = reputazione[0]
    
    return max_giocaotore, max_valore


def main():
    lista_giocatori = []
    with open("giocatori.txt", "r") as file_giocatori:
        for linea in file_giocatori:
            giocatore = linea.strip().split()
            codice_giocatore = giocatore[0]
            nome_giocatore = giocatore[1]
            oggetti = giocatore[2:]
            info = [codice_giocatore, nome_giocatore, oggetti]
            lista_giocatori.append(info)

    lista_oggetti = []
    with open("oggetti.txt", "r") as file_oggetti:
        for linea in file_oggetti:
            oggetto = linea.strip().split()
            codice_oggetto = oggetto[0]
            nome_oggetto = " ".join(oggetto[1:-3])
            difesa = int(oggetto[-3])
            attacco = int(oggetto[-2])
            magia = int(oggetto[-1])
            info = [codice_oggetto, nome_oggetto, difesa, attacco, magia]
            lista_oggetti.append(info)
    
    lista_boss = []
    with open("boss.txt", "r") as file_boss:
        for linea in file_boss:
            boss = linea.strip().split()
            codice_boss = boss[0]
            nome_boss = " ".join(boss[1:-3])
            difesa = int(boss[-3])
            attacco = int(boss[-2])
            reputazione = int(boss[-1])
            info = [codice_boss, nome_boss, difesa, attacco, reputazione]
            lista_boss.append(info)
    
    lista_statische = calcola_statistiche(lista_giocatori, lista_oggetti)
    lista_reputazione = calcola_reputazione(lista_statische, lista_boss)


    print(lista_reputazione)
    print(f"Il giocatore {max_giocaotore} ha sconfitto il maggior numero di boss, ovvero {max_num_boss}")

    max_reputazione = 0
    max_giocaotore = ""
    for reputazione in lista_reputazione:
        if reputazione[2] >= max_reputazione:
            max_reputazione = reputazione[2]
            max_giocaotore = reputazione[0]
    print(f"Il giocatore {max_giocaotore} ha ottenuto la maggior reputazione, ovvero {max_reputazione}")

if __name__ == "__main__":
    main()

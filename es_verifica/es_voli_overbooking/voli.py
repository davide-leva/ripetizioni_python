def genera_report_voli(lista_voli, lista_bigilietti):
    f_report = open("report_voli.txt", "w", encoding="UTF-8")

    for volo in lista_voli:
        codice = volo[0]
        destinazione = volo[1]
        posti = int(volo[2])
        max_bagaglio = int(volo[4])
        tariffa_basic = int(volo[-2])
        tariffa_plus = int(volo[-1])

        num_venduti = 0
        num_checkin = 0
        num_bagagli = 0
        tot_ricavo = 0

        for biglietto in lista_bigilietti:
            checkin = biglietto[-1] == "si"
            bagaglio_ok = int(biglietto[-2]) <= max_bagaglio
            tariffa = biglietto[3]

            if volo[0] == biglietto[1]:
                num_venduti += 1
                if checkin:
                    num_checkin += 1
                if bagaglio_ok:
                    num_bagagli += 1
                if tariffa == 'BASIC':
                    tot_ricavo += tariffa_basic
                elif tariffa == 'PLUS':
                    tot_ricavo += tariffa_plus

        occupazione = num_venduti / posti * 100;
        print(f"{codice} -- {destinazione} -- Venduti {num_venduti} -- Check-in {checkin} -- Occ {occupazione}% "
              f"-- Bagagli OK {num_bagagli} -- Ricavo {tot_ricavo}€")

        f_report.close()
        

def main():
    lista_voli = []
    lista_biglietti = []

    f_voli = open("voli.txt", "r", encoding="UTF-8")
    for volo in f_voli:
        volo = volo.rstrip().split()
        lista_voli.append(volo)
    f_voli.close()

    f_biglietti = open("biglietti.txt", "r", encoding="UTF-8")
    for biglietto in f_biglietti:
        biglietto = biglietto.rstrip().split()
        lista_biglietti.append(biglietto)

    genera_report_voli(lista_voli, lista_biglietti)
def generate_loans(users_list, loans_list):
    sanction_list = []

    user_loans_file = open("prestiti_utenti.txt", "w", encoding="UTF-8")
    for user in users_list:
        total_sanction = 0.0
        print(f"{user[1]} {user[2]}: ", end="", file=user_loans_file)
        for loan in loans_list:
            if user[0] == loan[0]:
                print(f"{loan[1]}, ", end="", file=user_loans_file)
                if loan[4] > loan[3]:
                    total_sanction += (loan[4] - loan[3]) * 0.5
                    print(f"ritardo di {loan[4] - loan[3]} giorni; ", end="", file=user_loans_file)
                else:
                    print("Nessun ritardo; ", end="", file=user_loans_file)
        print(file=user_loans_file)
        if total_sanction > 0:
            sanction_list.append([user[1], user[2], total_sanction])
    user_loans_file.close()

    return sanction_list


def generate_sanctions(sanction_list):
    sanction_file = open("rate_sanzioni.txt", "w", encoding="UTF-8")
    for sanction in sanction_list:
        print(f"{sanction[0]} {sanction[1]}: multa totale {sanction[2]:.2f}€", end="", file=sanction_file)

        if sanction[2] < 5:
            print(f", rata unica di {sanction[2]:.2f}€", file=sanction_file)
        elif sanction[2] <= 10:
            print(f", rata 1: {sanction[2]/2:.2f}€, rata 2: {sanction[2]/2}€", file=sanction_file)
        else:
            print(f", rata 1: {sanction[2]/3:.2f}€, rata 2: {sanction[2]/3:.2f}€, rata 3: {sanction[2]/3:.2f}€", file=sanction_file)
    sanction_file.close()


def main():
    users_list = []
    loans_list = []

    users_file = open("utenti.txt", "r", encoding="UTF-8")
    for line in users_file:
        line = line.rstrip("\n").split()

        user_id = line[0]
        first_name = line[1]
        last_name = line[2]
        age = int(line[3])

        user = [user_id, first_name, last_name, age]
        users_list.append(user)
    users_file.close()

    loans_file = open("prestiti.txt", "r", encoding="UTF-8")
    for line in loans_file:
        line = line.rstrip("\n").split()

        user_id = line[0]
        title = " ".join(line[1:-3])
        date = line[-3]
        expected_day = int(line[-2])
        effective_day = int(line[-1])

        loan = [user_id, title, date, expected_day, effective_day]
        loans_list.append(loan)
    loans_file.close()

    sanction_list = generate_loans(users_list, loans_list)
    generate_sanctions(sanction_list)


main()

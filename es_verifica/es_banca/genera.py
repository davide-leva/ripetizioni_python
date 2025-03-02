import random
import datetime

# Funzione per generare un ID esadecimale di 4 cifre maiuscole
def generate_hex_id():
    return ''.join(random.choices('0123456789ABCDEF', k=4))

# Funzione per generare i clienti
def generate_clients(num_clients=25):
    clients = []
    names = ["Mario", "Luigi", "Giovanna", "Anna", "Paolo", "Laura", "Giuseppe", "Maria", "Luca", "Sara", "Francesca", "Andrea", "Roberto", "Elena", "Simone", "Giovanni", "Teresa", "Antonio", "Chiara", "Marco"]
    surnames = ["Rossi", "Bianchi", "Verdi", "Ferrari", "Russo", "Esposito", "Romano", "Gallo", "Conti", "Marino", "Greco", "Bruno", "Galli", "Costa", "Fontana", "Rizzo", "Moretti", "Barbieri", "Lombardi", "Mancini"]
    types = ["BASIC"] * 4 + ["NEXT"] * 3 + ["PREMIUM"] * 3  # Distribuzione dei tipi di conto
    for i in range(num_clients):
        iban = f"IT{i+1:02d}CL{random.randint(1000000000, 9999999999)}"  # Genera un IBAN univoco
        name = random.choice(names)
        surname = random.choice(surnames)
        balance = round(random.uniform(1000.0, 1000.0), 2)  # Bilancio casuale tra 1000 e 50000
        tipo = random.choice(types)
        punti = random.randint(500, 2800)  # Punti casuali tra 0 e 5000
        clients.append([iban, name, surname, balance, tipo, punti])
    return clients

# Funzione per generare le transazioni
def generate_transactions(client_ibans, num_transactions=500):
    transactions = []
    start_date = datetime.datetime(2023, 1, 1)  # Data di inizio per le transazioni
    for _ in range(num_transactions):
        delta = datetime.timedelta(minutes=random.randint(1, 60 * 3))  # Intervallo casuale tra transazioni
        start_date += delta
        data = start_date.strftime("%d/%m/%Y")  # Formato data
        ora = start_date.strftime("%H:%M:%S")  # Formato ora
        iban = random.choice(client_ibans)  # Scegli un IBAN casuale dalla lista dei clienti
        direzione = random.choices(["DARE", "AVERE"], weights=[70, 30])[0]  # 70% DARE, 30% AVERE
        if direzione == "DARE":
            importo = round(random.uniform(10.0, 5000.0), 2)  # Importo per DARE
        else:
            importo = round(random.uniform(50.0, 2000.0), 2)  # Importo per AVERE
        trans_id = generate_hex_id()  # Genera un ID esadecimale
        transactions.append((trans_id, iban, importo, data, ora, direzione))
    return transactions

# Generazione dei clienti
clients = generate_clients(25)
client_ibans = [c[0] for c in clients]  # Lista degli IBAN dei clienti

# Scrittura del file clienti.txt
with open('clienti.txt', 'w') as f:
    for client in clients:
        f.write(f"{client[0]} {client[1]} {client[2]} {client[3]:.2f} {client[4]} {client[5]}\n")

# Generazione delle transazioni
transactions = generate_transactions(client_ibans, 300)

# Scrittura del file transazioni.txt
with open('transazioni.txt', 'w') as f:
    for t in transactions:
        f.write(f"{t[0]} {t[1]} {t[2]:.2f} {t[3]} {t[4]} {t[5]}\n")


print("File clienti.txt e transazioni.txt generati con successo!")
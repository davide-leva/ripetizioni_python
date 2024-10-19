n_client = int(input("Insert number of client: "))

sale = 0
for i in range(0, n_client):
    groceries = float(input("Insert amount spent in groceries: "))

    if groceries < 10:
        print("No sale")
        continue
    elif 10 < groceries < 60:
        sale = 0.08 * groceries
    elif 60 < groceries < 150:
        sale = 0.1 * groceries
    elif 150 < groceries < 210:
        sale = 0.12 * groceries
    else:
        sale = 0.14 * groceries

    print(f"The sale is {sale}")

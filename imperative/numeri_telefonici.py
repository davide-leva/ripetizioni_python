# Scrivere un programma che accetta una sequenza di numeri telefonici che includa pure il codice internazionale,
# Seleziona i numeri che sono italiani oppure francesi. Quindi resitutire il numeri di numeri tel. italiani e francesi
# e inoltre tra i numeri contare i call center (inizia con 800) e i numeri governativi (finiscono con 9000). La sequenza
# è terminata con lo spazio
# ITA +39, FRA +33

n_ita = 0
n_fra = 0
n_call_center = 0
n_gov = 0

while True:
    num_tel = input("Inserisci numero telefonico: ")

    if num_tel == "":
        break

    if num_tel.startswith('+33'):
        n_fra += 1

    if num_tel.startswith('+39'):
        n_ita += 1

    if num_tel[3:].startswith('800'):
        n_call_center += 1

    if num_tel.endswith('9000'):
        n_gov += 1

print('N ITA', n_ita)
print('N FRA', n_fra)
print('CALL CENTER', n_call_center)
print('N GOV', n_gov)

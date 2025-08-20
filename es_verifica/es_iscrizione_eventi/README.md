# Esercizio: Report e Presenze Clienti ad Eventi

## 🎯 Obiettivo
Lo scopo dell’esercizio è gestire un sistema semplificato di **clienti** e **iscrizioni ad eventi**.  
A partire da due file di input (`clienti.txt` e `iscrizioni.txt`), il programma deve:

1. Calcolare quanto ogni cliente ha speso e a quanti eventi ha partecipato, applicando eventuali sconti in base allo **stato** (NORMALE, MEMBER, VIP).
2. Generare un prospetto delle presenze, elencando gli eventi frequentati da ogni cliente con i relativi costi.

## 🔧 Struttura del programma
Il programma è composto da tre funzioni principali:

### `genera_report(lista_clienti, lista_iscrizioni)`
- Calcola per ogni cliente:
  - Numero di ingressi agli eventi
  - Spesa totale (con eventuali sconti)
- Applica sconti sul totale:
  - **MEMBER** → -10%
  - **VIP** → -20%
- Scrive i risultati nel file `report.txt` in questo formato:

```
Nome Cognome ha speso X.XX€ entrando a N eventi
```

---

### `genera_presenze(lista_clienti, lista_iscrizioni)`
- Elenca per ogni cliente gli eventi a cui ha partecipato, indicando anche il costo di ciascun evento.
- Scrive i risultati nel file `presenze.txt` in questo formato:

```
Nome Cognome: Evento1 Costo1€ Evento2 Costo2€ ...
```

---

### `main()`
- Legge i dati da:
  - `clienti.txt` → informazioni sui clienti
  - `iscrizioni.txt` → informazioni sulle iscrizioni
- Popola due liste (`lista_clienti` e `lista_iscrizioni`)
- Richiama le due funzioni di generazione (`genera_report` e `genera_presenze`)

---

## 📂 File di input

### `clienti.txt`
Formato:  
```
codice_cliente, nome, cognome, stato, residenza
```

Esempio:
```
C001, Matteo, Russo, NORMALE, Palermo
C002, Elena, Romano, VIP, Verona
C003, Marco, Galli, VIP, Napoli
...
```

### `iscrizioni.txt`
Formato:  
```
codice_cliente, nome_evento, costo
```

Esempio:
```
C001, Concerto, 106.62
C002, Musical, 44.71
C003, Festival, 164.82
...
```

---

## 📄 File di output

### `report.txt` (spesa e ingressi)
Esempio:
```
Matteo Russo ha speso 171.94€ entrando a 2 eventi
Elena Romano ha speso 45.71€ entrando a 2 eventi
Marco Galli ha speso 131.86€ entrando a 1 eventi
...
```

### `presenze.txt` (dettaglio eventi)
Esempio:
```
Matteo Russo: Concerto 106.62€ Conferenza 65.32€ 
Elena Romano: Musical 44.71€ Partita 12.43€ 
Marco Galli: Festival 164.82€ 
...
```
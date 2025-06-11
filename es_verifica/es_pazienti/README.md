# Verifica di Informatica

Una clinica medica per gestire i dati dei pazienti e le visite mediche utilizza due file:

- **pazienti.txt**: elenco dei pazienti registrati
- **prestazioni.txt**: interventi o esami effettuati

## Formato dei file

### pazienti.txt
Ogni riga contiene i dati di un paziente:

```
codice_paziente, nome, cognome, età, sesso, assicurazione (si/no), importo_residuo
```
Esempio:
```
PZ001, Mario, Rossi, 45, M, si, -50
PZ002, Anna, Verdi, 34, F, no, 0
PZ003, Luca, Neri, 65, M, si, -80
PZ004, Giulia, Bianchi, 29, F, no, 20
PZ005, Paolo, De Luca, 50, M, si, -10
```

### prestazioni.txt
Ogni riga contiene i dati di una prestazione:

```
codice_paziente, tipo_prestazione, costo
```
Esempio:
```
PZ001, visita_specialistica, 120
PZ002, analisi_laboratorio, 60
PZ003, risonanza, 300
PZ003, visita_specialistica, 120
PZ005, analisi_laboratorio, 60
```

## Struttura del programma

- La funzione `main()` carica i dati dai file e crea:
  - `lista_pazienti`: ogni elemento è una lista con i dati di un paziente
  - `lista_prestazioni`: ogni elemento è una lista con i dati di una prestazione

- Funzione `crea_file_spese_pazienti(lista_pazienti, lista_prestazioni)`:
  - Per ogni paziente, crea una riga con nome, cognome e tutte le prestazioni svolte con costo
  - Salva il risultato in `spese_pazienti.txt`
  - Ogni riga: `nome cognome prestazione: costo ...`
  - Esempio:
    - Mario Rossi visita_specialistica: 120 risonanza: 300
    - Anna Verdi analisi_laboratorio: 60

- Funzione `crea_file_spesa_totale(lista_pazienti, lista_prestazioni)`:
  - Calcola per ogni paziente la spesa totale (prestazioni + importo_residuo)
  - Salva il risultato in `spesa_totale.txt`
  - Ogni riga: `nome cognome: spesa_totale`
  - Esempio:
    - Mario Rossi: 370
    - Anna Verdi: 60
    - Luca Neri: 40

## Attenzione

- Rispettare le consegne sulle funzioni e sulle strutture dati da utilizzare.
- Funzioni diverse e strutture dati diverse da quelle richieste non verranno considerate corrette.

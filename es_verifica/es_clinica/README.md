# Verifica di informatica

Una clinica medica per gestire i dati dei pazienti e le visitiche mediche, utilizza due file:
* **pazienti.txt**: elenco dei pazienti registrati
* **prestazioni.txt**: interventi o esami effettuati

## pazienti.txt
Contiene per ogni paziente
```
codice_paziente, nome, cognome, eta, sesso, assicurazione (si/no), importo_residuo
```

```
PZ001, Mario, Rossi, 45, M, sì, -50
PZ002, Anna, Verdi, 34, F, no, 0
PZ003, Luca, Neri, 65, M, sì, -80
PZ004, Giulia, Bianchi, 29, F, no, 20
PZ005, Paolo, De Luca, 50, M, sì, -10
```

## prestazioni.txt
Contiene per ogni prestazione:
```
codice_paziente, tipo_prestazione, costo
```

```
PZ001, visita_specialistica, 120
PZ002, analisi_laboratorio, 60
PZ001, risonanza, 300
PZ004, ecografia, 90
PZ003, visita_specialistica, 120
PZ005, analisi_laboratorio, 60
```

## Struttura del programma
* **main()**: legge i file _pazienti.txt_ e _prestazioni.txt_ e crea:
  * _lista\_pazienti.txt_: ogni elemento e' una lista con i dati di un paziente
  * _lista\_prestazioni.txt_: ogni elemento e' una lista con i dati di una prestazione

* **crea_file_spese_pazienti(lista_pazienti, lista_prestazioni)**: per ogni paziente, crea una riga con **nome** e **cognome**  e tutte le **prestazioni svolte con costo**, e poi salva i dati nel file _spese\_pazienti.txt_. Ogni riga contiene: **nome** e **cognome** seguito dalle singole prestzioni effettuate con costo. Esempio:
  ```
  Mario rossi visita_specialistica: 120 risonanza: 300
  Anna verdi: analisi_laboratorio: 60
  ```

* **crea_file_spesa_totale(lista_pazienti, lista_prestazioni)**: calcola per ogni paziente la **spesa totale** (prestazioni + importo_residuo) e poi salva i dati in _spesa\_totale.txt_. Ogni riga contiene: **nome** e **cognome**: **spesa_totale**, tenendo conto anche dell'imporo_residuo. Esempio
  ```
  Mario Rossi: 370
  Anna Verdi: 60
  Luca Neri: 40
  ```
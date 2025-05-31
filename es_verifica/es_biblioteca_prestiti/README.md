# Gestione prestiti biblioteca

Una biblioteca gestisce i prestiti dei libri agli utenti. Le informazioni sono salvate in tre file: _libri.txt_, _utenti.txt_ e _prestiti.txt_

### File libri.txt
`codice_libro, titolo, autore, anno`

```
LB001, Il Signore degli Anelli, J.R.R. Tolkien, 1954
LB002, 1984, George Orwell, 1949
LB003, Il Piccolo Principe, Antoine de Saint-Exupéry, 1943
LB004, Harry Potter e la Pietra Filosofale, J.K. Rowling, 1997
LB005, Orgoglio e Pregiudizio, Jane Austen, 1813
```

### File utenti.txt
`codice_utente, nome_cognome`

```
UT001, Mario Rossi
UT002, Lucia Bianchi
UT003, Paolo Verdi
UT004, Anna Neri
UT005, Marco Gallo
```

### File prestiti.txt
`codice_libro, codice_utente, numero_prestiti, anno`

```
LB001, UT001, 2, 2024
LB002, UT002, 1, 2024
LB003, UT001, 1, 2023
LB004, UT003, 3, 2024
LB001, UT002, 1, 2024
LB005, UT004, 2, 2023
LB002, UT005, 1, 2024
LB003, UT003, 2, 2024
```

## Richieste
Scrivere un programma python che:
1. Legge i dati dai file _libri.txt_, _utenti.txt_ e _prestiti.txt_
2. Calcola per ogni utente il **totale libri presi in prestito** e salva i dati in un file _totale_prestiti_utenti.txt_ contenente su ogni riga _codice_utente, totale_prestiti_.
3. Calcola per ogni libro il numero totale di prestiti e salva i dati in un file _totale_prestiti_libri.txt_ contenente su ogni riga _titolo_libro, totale_prestiti_. Le righe devono essere **ordinate per numero di prestiti decrescente**
4. [_BONUS_] Calcola per ogni anno il numero di prestiti effettuati e salva i dati in un file _prestiti_anno.txt_ contenente su ogni riga _anno, totale_prestiti_. Le righe devono essere **ordinate per anno crescente**

## Struttura
Il programma deve avere la seguente struttura:
* funzione _main()_: legge i dati dai file di ingresso e li memorizza in una struttura adeguata, inoltre chiama le seguenti tre funzioni
* funzione _calcola_totale_prestiti_utenti(...)_: che crea il file _totale_prestiti_utenti.txt_
* funzione _calcola_totale_prestiti_libri(...)_: che crea il file _totale_prestiti_libri.txt_
* funzione _calcola_prestiti_per_anno(...)_: che crea il file _prestiti_anno.txt_

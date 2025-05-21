# Verifica di informatica

Una biblioteca gestisce diversi eventi e tiene traccia delle varie iscrizioni che gli utenti effettuano ad ogni evento. Le informazioni sono salvate in due file: _eventi.txt_ e _iscrizioni.txt_

### File eventi.txt
```codice_evento, nome_evento, responsabile, costo_ingresso, max_partecipanti```

```txt
EV001, Lettura fiabe, Marta Neri, 5.00, 50
EV002, Laboratorio Scrittura, Luigi Bianchi, 12.00, 30
EV003, Incontro Autore, Paola Verdi, 8.00, 40
EV004, Proiezione Film, Enrico Gallo, 6.00, 60
EV005, Workshop Poesia, Chiara Mori, 10.00, 20
...
```

### File ingressi.txt
```txt
EV001, UT001, 2, 2024
EV002, UT002, 1, 2024
EV003, UT001, 1, 2023
EV004, UT003, 3, 2024
EV001, UT002, 1, 2024
...
```

## Richieste
Scrivere un programma python che:
1. Legge i dati dai file _eventi.txt_ e _iscrizioni.txt_
2. Calcola per ogni utente il **totale speso** e quindi salva i dati in un file _spesa.txt_ contenente su ogni riga _codice\_utente, spesa\_totale_.
3. Calcola per ogni evento il numero di ingressi effettuati da ogni utente e quindi salva i dati in un file _ingressi.txt_ contente su ogni riga _nome\_evento, totale\_ingressi_. Le righe devono essere **ordinate per numero di ingressi decrescente**
4. [_BONUS_] Calcola per ogni anno il numero di eventi che si sono tenuti e quindi salva i dati in un file _eventi\_anno.txt_ contente su ogni riga _anno, totale\_eventi_. Le righe devono essere **ordinate per anno crescente**

## Struttura
Il programma deve avere la seguente struttura
* funzione _main()_: legge i dati dai due file di ingresso e li memorizza in una struttura adeguata, inoltre chiama le seguenti tre funzioni
* funzione _calcola\_spesa(...)_: che crea il file _spesa.txt_
* funzione _calcola\_ingressi(...)_: che crea il file _ingressi.txt_
* funzione _calcola\_eventi\_per\_anno(...): che crea il file _eventi\_anno.txt_

## Consigli
* Tempo necessario allo svolgimento della simulazione 1h (1h e 30 considerando la funzione _BONUS_)
* Scegli bene la struttura dati che rappresenta i file
* _HINT_: per la funzione bonus puoi creare un dizionario che associa ogni anno ad un insieme dei codici degli eventi che si sono tenuti in quell'anno. Una volta costruito lo si ordina e poi si stampa l'anno (chiave) e la dimesione dell'insieme (valore)
* **BUON LAVORO :)**

## Auto correzione
* funzione main (2 punti totali):
    - lettura file: 0.5 punti
    - scelta stutture: 0.5 punti
    - riempimento con i dati: 0.5 punti
    - chiamata funzioni: 0.5 punti
* prime due funzioni (6 punti totali):
    - stuttura dati adeguate: 0.5 punti,
    - logica di rimpimento: 2 punti
    - stampa su file: 0.5 punti
* ultima funzione: per la lode
* punti base: 2

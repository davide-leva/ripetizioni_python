def read_dict(filename):
    data = dict()
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            obj = line.strip().split(', ')
            data[obj[0]] = obj[1:]
    return data

def read_list(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(line.strip().split(', '))
    return data

def calcola_totale_prestiti_utenti(prestiti, output_file):
    d_utenti = dict()
    for p in prestiti:
        utente = p[1]
        n = int(p[2])
        d_utenti[utente] = d_utenti.get(utente, 0) + n
    with open(output_file, 'w', encoding='utf-8') as f:
        for utente, totale in d_utenti.items():
            f.write(f"{utente}, {totale}\n")

def calcola_totale_prestiti_libri(prestiti, libri, output_file):
    d_libri = dict()
    for p in prestiti:
        libro = p[0]
        n = int(p[2])
        d_libri[libro] = d_libri.get(libro, 0) + n
    # Ordina per numero prestiti decrescente
    d_libri_sorted = sorted(d_libri.items(), key=lambda x: x[1], reverse=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        for libro, totale in d_libri_sorted:
            titolo = libri[libro][0]
            f.write(f"{titolo}, {totale}\n")

def calcola_prestiti_per_anno(prestiti, output_file):
    d_anni = dict()
    for p in prestiti:
        anno = int(p[3])
        n = int(p[2])
        d_anni[anno] = d_anni.get(anno, 0) + n
    d_anni_sorted = sorted(d_anni.items())
    with open(output_file, 'w', encoding='utf-8') as f:
        for anno, totale in d_anni_sorted:
            f.write(f"{anno}, {totale}\n")

def main():
    libri = read_dict('libri.txt')
    utenti = read_dict('utenti.txt')
    prestiti = read_list('prestiti.txt')
    calcola_totale_prestiti_utenti(prestiti, 'totale_prestiti_utenti.txt')
    calcola_totale_prestiti_libri(prestiti, libri, 'totale_prestiti_libri.txt')
    calcola_prestiti_per_anno(prestiti, 'prestiti_anno.txt')

if __name__ == '__main__':
    main()

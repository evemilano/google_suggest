import requests
import json
import time
import os

def get_related_keywords(initial_queries, language, num_cycles):
    base_url = "http://suggestqueries.google.com/complete/search"
    
    # Lista per tracciare le parole chiave correlate
    all_keywords = set(initial_queries)  # Aggiungi subito le query iniziali
    
    # Set per tracciare le query già processate
    processed_queries = set()
    
    # Lista di query da processare
    to_process = initial_queries[:]

    # Ciclo per il numero di iterazioni richieste
    for cycle in range(num_cycles):
        print(f"\nCiclo {cycle + 1}/{num_cycles}")
        new_queries = []

        for query in to_process:
            if query in processed_queries:
                continue

            # Aggiungi la query all'elenco delle query processate
            processed_queries.add(query)

            # Effettua la richiesta HTTP
            response = requests.get(base_url, params={"client": "firefox", "q": query, "hl": language})
            time.sleep(1)  # Pausa di 1 secondo tra le richieste

            if response.status_code == 200:
                try:
                    # Parsing del JSON restituito
                    data = response.json()

                    # Estrai le parole correlate
                    suggestions = data[1]
                    print(f"Query: {query} -> {len(suggestions)} parole correlate trovate")

                    for suggestion in suggestions:
                        if suggestion not in all_keywords:
                            all_keywords.add(suggestion)
                            new_queries.append(suggestion)
                except json.JSONDecodeError:
                    print(f"Errore nel decodificare la risposta JSON per la query: {query}")
            else:
                print(f"Errore nella richiesta HTTP per la query: {query} (status code: {response.status_code})")

        # Aggiorna la lista di query da processare con quelle nuove
        to_process = new_queries

    return list(all_keywords)

if __name__ == "__main__":
    # Parametri di input
    initial_queries = input("Inserisci le query iniziali separate da virgola: ").strip().split(",")
    initial_queries = [query.strip() for query in initial_queries if query.strip()]

    if not initial_queries:
        print("Errore: è necessario inserire almeno una query iniziale.")
        exit(1)

    language = input("Inserisci la lingua (es. it, en): ").strip()
    num_cycles = int(input("Inserisci il numero di cicli: "))

    # Esegui lo script
    related_keywords = get_related_keywords(initial_queries, language, num_cycles)

    # Stampa e salva il risultato
    print("\nParole correlate trovate:")
    for keyword in related_keywords:
        print(keyword)

    # Percorso relativo alla cartella dello script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(script_dir, "related_keywords.txt")

    # Salva in un file
    with open(output_file, "w", encoding="utf-8") as f:
        for keyword in related_keywords:
            f.write(keyword + "\n")

    print(f"\nLe parole correlate sono state salvate in '{output_file}'.")

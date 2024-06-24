import requests
from bs4 import BeautifulSoup

# URL del sito web del challenge
url = "http://infinite.challs.olicyber.it"

# Numero di volte che vogliamo rispondere correttamente
numero_risposte_corrette = 600

# Contatore delle risposte corrette
risposte_corrette = 0

# Fino a quando non abbiamo risposto correttamente il numero desiderato di volte
while risposte_corrette < numero_risposte_corrette:
    # Effettua una richiesta GET per ottenere la pagina web
    response = requests.get(url)
    
    # Utilizza BeautifulSoup per analizzare il contenuto HTML della pagina
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Trova la domanda
    domanda = soup.find('p').text
    
    # Analizza la domanda per ottenere la risposta corretta
    # Questo è solo un esempio generico, la logica dovrebbe essere adattata a seconda della variazione delle domande
    risposta_corretta = domanda.count("r")
    
    # Invia la risposta corretta tramite una richiesta POST
    response = requests.post(url, data={"letter": str(risposta_corretta)})
    
    # Se la richiesta ha avuto successo (status code 200), incrementa il contatore delle risposte corrette
    if response.status_code == 200:
        risposte_corrette += 1
        print(f"Risposta corretta {risposte_corrette}/{numero_risposte_corrette}")
print(response.text)

print("Challenge completato!")
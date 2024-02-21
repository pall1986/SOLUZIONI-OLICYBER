#UTILIZZANDO UN ATTACCO A DIZIONARIO E' POSSIBILE ESTRARRE VELOCEMENTE I FILE
import zipfile

def crack_zip(zip_file, dictionary_file):
    # Apri il file ZIP
    with zipfile.ZipFile(zip_file, 'r') as zf:


        # Leggi le password dal file di dizionario
        with open(dictionary_file, 'r', encoding='latin-1') as f:
            
            passwords = f.readlines()
            for password in passwords:
                password = password.strip()
                try:
                    # Prova ad aprire il file ZIP con la password corrente
                    zf.extractall(pwd=password.encode('utf-8'))
                    print(f"Password trovata: {password}")
                    return True
                except Exception as e:
                    pass
    print("Password non trovata nel dizionario.")
    return False

# Specifica il percorso del file ZIP e del file di dizionario
i=100
while (i!=0):

    zip_file = str(i)+'.zip'
    dictionary_file = 'rockyou.txt'
    i=i-1

    # Esegui la funzione per tentare di decifrare il file ZIP
    crack_zip(zip_file, dictionary_file)

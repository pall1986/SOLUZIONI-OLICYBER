#SOLUZIONE
#Seguendo i flussi TCP del file pcapng si trova che:
# 1-nel primo flusso c'è uno scambio di mail tra alice ed il gabibbo in cui viene inviata una password in chiaro di un file segreto
# 2-controllando i flussi TCP sucessivi si ricava un file 'dati.zip' codificato in base64 il cui contenuto il cui contenuto è riportato nella stringa seguente
#il seguente script ricostruisce il file zip pronto per essere poi aperto con la password precedente.
#Nel file zip si ha un file di testo contenente la flag
import base64

# Testo codificato in base64
encoded_text = """
UEsDBAoAAAAAADulm1QAAAAAAAAAAAAAAAAFABwAZGF0aS9VVAkAA3GOaWJyjmlidXgLAAEE
6AMAAAToAwAAUEsDBAoACQAAAMikm1Rtav/dPwAAADMAAAANABwAZGF0aS9mbGFnLnR4dFVU
CQADl41pYpeNaWJ1eAsAAQToAwAABOgDAADqjURVPEQmTgYftinWcYp1R87NwCw+inMGmSJx
Ndf3SFn9rf7VTQXPUfa4qogymeZk/HP9so/1hEOXvUosP7NQSwcIbWr/3T8AAAAzAAAAUEsB
Ah4DCgAAAAAAO6WbVAAAAAAAAAAAAAAAAAUAGAAAAAAAAAAQAP1BAAAAAGRhdGkvVVQFAANx
jmlidXgLAAEE6AMAAAToAwAAUEsBAh4DCgAJAAAAyKSbVG1q/90/AAAAMwAAAA0AGAAAAAAA
AQAAALSBPwAAAGRhdGkvZmxhZy50eHRVVAUAA5eNaWJ1eAsAAQToAwAABOgDAABQSwUGAAAA
AAIAAgCeAAAA1QAAAAAA
"""

# Decodifica il testo base64
decoded_bytes = base64.b64decode(encoded_text)

# Scrivi il contenuto decodificato in un file ZIP
with open("dati.zip", "wb") as zip_file:
    zip_file.write(decoded_bytes)

print("File ZIP estratto correttamente!")
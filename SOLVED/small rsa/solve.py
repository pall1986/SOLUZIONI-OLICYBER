import gmpy2
##Hai ragione, la fattorizzazione potrebbe non sempre essere la soluzione appropriata, soprattutto quando il problema non richiede esplicitamente la decifrazione del messaggio cifrato. Se conosci eee, NNN, e il testo cifrato (ctctct) e hai bisogno di recuperare il testo in chiaro, in questo caso particolare è possibile utilizzare il valore di eee basso (come e\=3e = 3e\=3)
## per eseguire un attacco di testo in chiaro noto come "attacco di decrittazione a radice cubica".
# Valori dati
e_value = 3
N_value = 121188535871798118811428322495136173485838157702837603009744079502828661170574654643712519826693731103670617468427120197687519224611728159372629028899279680740201176466228593180097000630667826923128885153190352359299571456927587933797154384731664367396394374086703053646510220882981791309024543386831488440013
ct = 56274920108133183710879347789095782313165243853788407193317419375243717146801757114129876005705242550492379484281774120724787040219649340446091878053221949541

# Calcola la radice cubica del ciphertext
ciphertext = gmpy2.mpz(ct)
plaintext = gmpy2.iroot(ciphertext, e_value)[0]

# Converte il risultato in una stringa
plaintext_str = gmpy2.digits(plaintext, 16)

# Converti la stringa esadecimale in ASCII
plaintext_ascii = bytearray.fromhex(plaintext_str).decode()

print(f"Testo in chiaro esadecimale: {plaintext_str}")
print(f"Testo in chiaro ASCII: {plaintext_ascii}")
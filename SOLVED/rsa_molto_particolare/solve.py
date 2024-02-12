from Crypto.Util.number import getPrime, inverse, long_to_bytes, bytes_to_long
from sympy import isprime
def gcd_extended(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = gcd_extended(b % a, a)
        return (gcd, y - (b // a) * x, x)

def mod_inverse(e, phi):
    gcd, x, y = gcd_extended(e, phi)
    if gcd != 1:
        raise ValueError("e non è invertibile modulo phi")
    else:
        return x % phi

# Inserisci i valori di e e phi


# Calcola d

N = 22714782753220015042573603265764327669650408033887636001879315184259375362820403603936005525717891771936636443451884119703671427781729492224095091855683005507053963590222220410804649184763035006811331809382943132022500027644637621163477965898393682291084319795270435040869951140803612012610686322537800900791300826066574059761090027917447672155092101024934115081690160104897792167626579027888190943470746383568651182247114083165294856136382262206643466869528191984416012578579746005217713198188905067819779002232496897304974008305258471888110945562966313488702125793402335565466499907920044056450331308275860705662078
e = 65537
flag_enc = '388244a02eb9e2c2c06bcbc932422e0d181156ea4e08710b6987aad4f16e55e137b45ed9776b6baaffad78006db8131526e0c941b759e4493f38a697caba8d1a8e81300baa86d7b0a63b542e661b3bda502f6c09bf5636dbf567c21a3f3b10dcf9054ed4c485755df1d6d2f4a05814281eea0f4cb43d4e623a92c62473e2a2315e29e46ac31ff37e2a8feddba8f6d11a31aa7941d7edef3087582e43f2faa83a0555a598c1248568d8a268d993c8b47e8cc7c76d9ce95df1933d6b32fa331c1fcb154ebd65681945c958d8f0f10c015a478cc03fa4e31c1b5a4c55dc3da7b9c9ee5e0f24481b81a75af306dc9b766913c234f03673e9dc1cf35eb7f338d12e1f'
flag_enc=bytes.fromhex(flag_enc)
#print(flag_enc)
c=bytes_to_long(flag_enc)
print(c)

#N termina con  8!!!! Quindi, se N è il risultato del prodotto di due numeri primi, uno dei due deve essere pari
# e l'unico numero primo pari è 2
#Controlliamo se N/2 è primo
print(isprime(N//2))# True quindi N/2 è primo e l'altro numero primo è 2

p=2
q=N//2
phi_n=(q-1)*(p-1)
#Calcoliamo d
d = mod_inverse(e, phi_n)
#print("Il valore di d è:", d)
#Calcoliamo m
m= pow(c, d, N)

print("Il valore di m è:", m)
#Calcoliamo flag
print("La flag è: ",long_to_bytes(m))






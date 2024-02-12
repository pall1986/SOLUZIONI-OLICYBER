alfabeto_cifrato = [chr(ord('a') + i) for i in range(26)]
flag_cifrata='fmcj{yo_ackyzb_ihruvcvjam}'
flag_cifrata_divisa=list(flag_cifrata)
flag='f'
len_alfabeto_cifrato=len(alfabeto_cifrato)
distanza=0
i=0
while i<(len(flag_cifrata_divisa)):
	if flag_cifrata_divisa[i] in alfabeto_cifrato:
		#print((i-distanza))
		if (i-distanza)>=0:
			if (i)==0:
				pass
			else:
				#print(flag_cifrata.index(flag_cifrata[i])-distanza)
				flag=flag+alfabeto_cifrato[alfabeto_cifrato.index(flag_cifrata[i])-distanza]
		else:
			flag=flag+alfabeto_cifrato[len_alfabeto_cifrato-(distanza-alfabeto_cifrato.index(flag_cifrata[i]))]
		#print(distanza)
		

	else:
		flag=flag+flag_cifrata_divisa[i]
	i=i+1
	distanza=distanza+1

	print(flag)


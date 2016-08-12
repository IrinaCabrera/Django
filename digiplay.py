print ('\n-----------------------\n|Bienvenido a DigiPLAY|\n-----------------------')
print ('*Este juego te mostrara la suma de 4 digitos que tienes que adivinar*\n\nIngresa los numeros que creas correctos uno por uno*\nTienes 3 intentos.')
control=1
while control ==1:
	from random import randrange
	a=randrange(9)
	b=randrange(9)
	c=randrange(9)
	d=randrange(9)
	e=a+b+c+d
	print ('\nlos digitos que los componen suman',e,'ingresalos uno por uno')
	intentos=3
	while intentos >= 1:
		aa=int(input("\ningrese el primer numero:"))
		bb=int(input("ingrese el segundo numero:"))
		cc=int(input("ingrese el tercer numero:"))
		dd=int(input("ingrese el cuarto numero:"))
		
		if a==aa:
			print ('\nPrimer numero Correcto')
		else:
			print ('\nPrimer numero Incorrecto')
		
		if b==bb:
			print ('Segundo numero Correcto')
		else:
			print ('Segundo numero Incorrecto')
		
		if c==cc:
			print ('Tercer numero Correcto')
		else:
			print ('Tercer numero Incorrecto')
		
		if d==dd:
			print ('Cuarto numero Correcto')
		else:
			print ('Cuarto numero Incorrecto')
		intentos=intentos-1
		if intentos >=1:
			print ('\nLe quedan',intentos,'intentos')
		if intentos==0:
			print ('\nNo posee mas intentos, suerte la proxima vez')
			print ('\n-----------\n|GAME OVER|\n-----------')
			break
		

	control= int(input('desea continuar jugando?\n1)si\n2)no'))
	if control==2:
		print ('>> DigiPLAY se ha cerrado <<<')


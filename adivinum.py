control=1
while control==1:
	print ('--------------------------\n|Bienvenido a AdiviNumero|\n--------------------------\n*usted tendra 5 intentos para adivinar un numero del 1 al 100*')
	pista=int(input('\ndesea una pista? este mensaje no se volvera a mostrar y descontara un intento\n1)si\n2)no'))
	from random import randrange
	x=randrange(100)
	intentos=5
	if pista == 1:
		if x > 50:
			print ('\nel numero es mayor a 50')
			intentos=intentos-1
			print ('\nle quedan',intentos,'intentos')

		else:
			print ('\nel numero es menor a 50')
			intentos=intentos-1
			print ('\nle quedan',intentos,'intentos')

	while intentos >= 1:
		numingresado=int(input('\ningrese el numero que crea que es '))
		if numingresado < x:
			print ('el numero ingresado es menor al numero por adivinar.')
			intentos=intentos-1
			print ('le quedan',intentos,'intentos')
		if numingresado > x:
			print ('el numero ingresado es mayor al numero por adivinar.')
			intentos=intentos-1
			print ('le quedan',intentos,'intentos')
		if numingresado == x:
			print ('\nFELICIDADES! HA GANADO EL JUEGO!, debe de ser un genio')
			break
		if intentos == 0:
			print ('\n-----------\n|GAME OVER|\n-----------')


	control=int(input('\ndesea volver a jugar?\n1)si\n2)no'))
	if control==2:
		print ('>>> AdiviNumero se ha cerrado <<<')
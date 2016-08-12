print ('\n----------------------------------\n|Bienvenido al Camino del Gigante|\n----------------------------------')
print ('*Este juego consiste en hacer llegar al gigante a su caverna*\n\nTira el dado para que el pueda avanzar y llegar a destino\nTiene 3 intentos.')
control=1

while control==1:
	import random
	pasos=random.randint(1,18)
	print ('\nEl GIGANTE debe CAMINAR',pasos,'PASOS para LLEGAR a su CAVERNA')
	
	intentos=3
	while intentos >=1:
		import random 
		dado=random.randint(1,6)
		numero=int(input('\ningrese "1" para tirar el dado'))
		
		if numero == 1:
			print ('el numero que le toco fue',dado,)
			pasos=pasos-dado
			if pasos < 0:
				print ('el gigante dio mas pasos de los que debia, cayo por el precipicio')
				print ('\n-----------\n|GAME OVER|\n-----------')

			if pasos == 0:
				print ('\nFELICIDADES! EL GIGANTE HA LLEGADO A SU HOGAR SANO Y SALVO!')
				break
			print ('Ahora al gigante le quedan',pasos,'por caminar para llegar a destino')
			intentos=intentos-1
			print ('le quedan',intentos,'intentos')
			
			if intentos==0:
				print ('se ha quedado sin intentos y el gigante no llego a su destino')
				print ('\n-----------\n|GAME OVER|\n-----------')
				break
			


			

	control= int(input('desea continuar jugando?\n1)si\n2)no'))
	if control==2:
		print ('>> Camino Del Gigante se ha cerrado <<<')
	
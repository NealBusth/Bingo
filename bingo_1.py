import random

def randomLetra(rango_maximo):
	num = random.randrange(0, rango_maximo)
	return letras[num]


"""En este metodo le sumo un 1 a los numeros finales del random
porque solo toma en cuenta hasta el numero anterior ha este"""
def randomNumero(letra, rango_maximo):
	
	validacion_numero = False
	longitud_lista = len(lista_numeros)
	rango = 0

	if letra == "B":
		#mientras no se valida que el numero random es unico
		while validacion_numero == False:
			#Generar numero random
			num = random.randrange(1,16)
			#Si la lista de numeros no contiene nada
			if longitud_lista == 0:
				#Numero es unico y no se necesita validar
				validacion_numero = True
				lista_numeros.append(num)
				lista_numeros_letra_b.append(num)

				rango = rango_maximo
			#de lo contrario la lista contiene datos
			else:
				#Si el numero generado no se encuentra en la lista de numeros ya mostrados
				if num not in lista_numeros:
					#Validar y salir
					lista_numeros.append(num)
					lista_numeros_letra_b.append(num)
					validacion_numero = True

					rango = rango_maximo
					if len(lista_numeros_letra_b) == 15:
						#Si la lista de numeros de la letra b esta llena (15 numeros) remover de las letras disponibles
						letras.remove(letra)
						rango = rango_maximo - 1

	elif letra == "I":
		#mientras no se valida que el numero random es unico
		while validacion_numero == False:
			#Generar numero random
			num = random.randrange(16,31)
			#Si la lista de numeros no contiene nada
			if longitud_lista == 0:
				#Numero es unico y no se necesita validar
				validacion_numero = True
				lista_numeros.append(num)
				lista_numeros_letra_i.append(num)
				rango = rango_maximo
			#de lo contrario la lista contiene datos
			else:
				#Si el numero generado no se encuentra en la lista de numeros ya mostrados
				if num not in lista_numeros:
					#Validar y salir
					lista_numeros.append(num)
					lista_numeros_letra_i.append(num)
					validacion_numero = True
					
					rango = rango_maximo

					if len(lista_numeros_letra_i) == 15:
						#Si la lista de numeros de la letra b esta llena (15 numeros) remover de las letras disponibles
						letras.remove(letra)
						rango = rango_maximo - 1

	elif letra == "N":
		#mientras no se valida que el numero random es unico
		while validacion_numero == False:
			#Generar numero random
			num = random.randrange(31,46)
			#Si la lista de numeros no contiene nada
			if longitud_lista == 0:
				#Numero es unico y no se necesita validar
				validacion_numero = True
				lista_numeros.append(num)
				lista_numeros_letra_n.append(num)
				rango = rango_maximo
			#de lo contrario la lista contiene datos
			else:
				#Si el numero generado no se encuentra en la lista de numeros ya mostrados
				if num not in lista_numeros:
					#Validar y salir
					lista_numeros.append(num)
					lista_numeros_letra_n.append(num)
					validacion_numero = True
					
					rango = rango_maximo

					if len(lista_numeros_letra_n) == 15:
						#Si la lista de numeros de la letra b esta llena (15 numeros) remover de las letras disponibles
						letras.remove(letra)
						rango = rango_maximo - 1

	elif letra == "G":
		#mientras no se valida que el numero random es unico
		while validacion_numero == False:
			#Generar numero random
			num = random.randrange(46,61)
			#Si la lista de numeros no contiene nada
			if longitud_lista == 0:
				#Numero es unico y no se necesita validar
				validacion_numero = True
				lista_numeros.append(num)
				lista_numeros_letra_g.append(num)
				rango = rango_maximo
			#de lo contrario la lista contiene datos
			else:
				#Si el numero generado no se encuentra en la lista de numeros ya mostrados
				if num not in lista_numeros:
					#Validar y salir
					lista_numeros.append(num)
					lista_numeros_letra_g.append(num)
					validacion_numero = True
					
					rango = rango_maximo

					if len(lista_numeros_letra_g) == 15:
						#Si la lista de numeros de la letra b esta llena (15 numeros) remover de las letras disponibles
						letras.remove(letra)
						rango = rango_maximo - 1

	else:
		#mientras no se valida que el numero random es unico
		while validacion_numero == False:
			#Generar numero random
			num = random.randrange(61,76)
			#Si la lista de numeros no contiene nada
			if longitud_lista == 0:
				#Numero es unico y no se necesita validar
				validacion_numero = True
				lista_numeros.append(num)
				lista_numeros_letra_o.append(num)
				rango = rango_maximo
			#de lo contrario la lista contiene datos
			else:
				#Si el numero generado no se encuentra en la lista de numeros ya mostrados
				if num not in lista_numeros:
					#Validar y salir
					lista_numeros.append(num)
					lista_numeros_letra_o.append(num)
					validacion_numero = True
					
					rango = rango_maximo

					if len(lista_numeros_letra_o) == 15:
						#Si la lista de numeros de la letra b esta llena (15 numeros) remover de las letras disponibles
						letras.remove(letra)
						rango = rango_maximo - 1

	
	return num, rango


letras = ["B","I","N","G","O"]
lista_numeros = []
continuar = 1

#--------------
lista_numeros_letra_b = []
lista_numeros_letra_i = []
lista_numeros_letra_n = []
lista_numeros_letra_g = []
lista_numeros_letra_o = []

while continuar == 1:
	#Presentacion
	print("Bienvenido al juego de Bingo")
	nada = input("Presionar <ENTER> para continuar: ")
	rango_maximo_letras = 5

	#mientras presionar enter
	while nada == "":

		letra = randomLetra(rango_maximo_letras)
		numero, rango_reducido = randomNumero(letra, rango_maximo_letras)

		rango_maximo_letras = rango_reducido

		if rango_maximo_letras == 0:
			print("")
			print(" => " + letra + " - " + str(numero))
			print("")
			print(" -------------------------------------")
			print(" -------------------------------------")
			print("")
			print(" Ya no hay mas numeros, fin del Juego.")
			nada = "asd"
			continuar = 0
		else:
			print("")
			print(" => " + letra + " - " + str(numero))
			print("")
			nada = input(" <ENTER> para continuar,<S> para ver lista y cualquier letra para salir: ")

		if nada == "s":
			print("")
			print(" Lista de N° : " + str(lista_numeros))
			print("")
			nada = input(" <ENTER> para continuar y cualquier letra para salir: ")


	continuar = 0
	print(" Has salido del juego, espero que alguien haya ganado. :p ")

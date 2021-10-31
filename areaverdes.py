import random
print("le ofrezco estas tres bellezas de areas verdes")
print("""
	0)parque Don Benito
	1)volcan sanguijuela
	2)Finca Doña Elena
	""")





def generador_numero_aleatorio(valor_inicial, valor_final):
	'''
	E: un rango de numeros enteros positivos 
	S: numero aleatorio en un rango de numero
	R: solo un numero del rango
	'''
	numero_aleatorio = int(random.random() * valor_final) 
	return numero_aleatorio
	
res = generador_numero_aleatorio(1,3)
print(res)


def lista(numero_elegido):
	'''
	E: una lista con las areas y las personas
	S:el nombre de la área elegida y las personas de esa área 
	R: Crea tres unicas áreas
	'''
	lista_relacion = [["área 1", ["Don Pepe", "Rosaura"]], ["área 2", ["Felipe","Don Castor"]], ["area 3", ["Lola", "Sinai","Antonieta"]]]
	print("¿Cuál área verde desea visitar?")
	numero_elegido = int(input())
	if(numero_elegido == 1):
		print("parque Don Benito") 
	elif(numero_elegido == 0):
		print("volcan sanguijuela") 	
	elif(numero_elegido == 2):
		print("Finca Doña Elena") 
	elif(numero_elegido == 3):
		False	
	for i in range(len(lista_relacion[numero_elegido][1])):
		print(str(i + 1) + "- " + lista_relacion[numero_elegido][1][i])
	print("¿Con cuál persona desea hablar?")
	persona_elegido = int(input()) 
	for i in range(len(lista_relacion[numero_elegido][1])):
		print(str(i + 1) + "- " + lista_relacion[numero_elegido][1][i])
res = lista(0)
print(res)


#No funcionan
primer_nombre_areas_verdes = {"parque", "volcan", "finca"}
segundo_nombre_areas_verdes = {"Don Benito", "sanguijuela","Doña Elena"}

def generacion_areas_verdes():
	numero_areas_verdes = 0
	numero_valido = False
	print("Ingrese la cantidad de zonas que desea crear:")
	
	while(numero_valido == False):
		numero_areas_verdes = int(input())
		if(numero_areas_verdes > 0):
			numero_valido = True
		else:
			print("El número ingresado no es válido, favor ingresar otro.")

	lista_areas_verdes = creacion_areas_verdes(numero_areas_verdes)
	return lista_areas_verdes
	
res = generacion_areas_verdes()
print(res)

def creacion_areas_verdes(numero_areas_verdes):
	lista_areas_verdes = []
	for i in range(numero_areas_verdes):
		nombre_area_verde = generador_numero_aleatorio(0, len(primer_nombre_areas_verdes)) + " " + generador_numero_aleatorio(0, len(segundo_nombre_areas_verdes))
		lista_areas_verdes.append(nombre_area_verde)
	return lista_areas_verdes
	
res = creacion_areas_verdes()
print(res)
	
	

def indiceEspejo(arr, inicio=1):
    # Caso base: si el array tiene un solo elemento
    if len(arr) == 1:
        if arr[0] == inicio:
            return arr[0]
        return "No existe indice espejo"

    # Dividir el array en dos mitades
    medio = len(arr) // 2

    # Verificar el índice espejo en el elemento medio
    if arr[medio] == inicio + medio:
        return arr[medio]

    # Decidir en cuál mitad continuar
    if arr[medio] < inicio + medio:
        # Buscar en la mitad derecha
        return indiceEspejo(arr[medio + 1:], inicio + medio + 1)
    else:
        # Buscar en la mitad izquierda
        return indiceEspejo(arr[:medio], inicio)

# Ejemplo de uso
print(indiceEspejo([-4, -1, 2, 4, 7]))




def IzquierdaDominante(arr):
	if len(arr) <= 2:
		return sum(arr)
			
	medio = len(arr) // 2
	mitad_izq = arr[:medio]
	mitad_der = arr[medio:]
		
	suma_izq = IzquierdaDominante(mitad_izq)
	suma_der = IzquierdaDominante(mitad_der)
	
	if suma_izq > suma_der:
		return suma_izq + suma_der
	return -1

def esMasALaIzquierda(arr):
	res = IzquierdaDominante(arr)
	if res != -1:
		return "Es mas a la izquierda"
	return "No es mas a la izquierda"

print(esMasALaIzquierda([8, 6, 7, 4, 5, 1, 3, 2]))



# Puede ser que este ejercicio solo sea comparar la resta de los elems de la mitad de ambos arrays
# Con sus siguientes y anteriores?
# A chequear, pero en principio vamos a hacer eso

def minDif (a, b):

    res_primero = abs(a[0] - b[0])
    res_ultimo = abs(a[len(a) - 1] - b[len(b) - 1])
    
    medio = len(a) // 2
    res_medio =  abs(a[medio] - b[medio])
    res_medio_sig = abs(a[medio + 1] - b[medio + 1])
    res_medio_ant = abs(a[medio - 1] - b[medio - 1])

    print("res_primero:", res_primero)
    print("res_ultimo:", res_ultimo)
    print("res_medio:", res_medio)
    print("res_medio_sig:", res_medio_sig)
    print("res_medio_ant:", res_medio_ant)

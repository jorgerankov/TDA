""" 27. SumaSelectiva
a)  Uso la idea de ordenar de mayor a menor para luego obtener los k
    primeros elementos (que resultan ser los mayores)"""

def sumaSelectiva(conjunto, k):
    conjunto.sort(reverse=True)
    mayor_subconjunto = []
    i = 0
    total = 0
    for i in range(k):
        total += conjunto[i]
        mayor_subconjunto.append(conjunto[i])
    

    print("El mayor subconjunto es:",mayor_subconjunto, "y el total es:",total)



""" 28. SumaGolosa
a)   Propongo ordenar la lista de forma ascendente   => Sumo el primer elemento con el siguiente 
=> Esa suma la acumulo en un contador de costo  => Sumo el proximo elemento y agrego el total al costo
=> Al tener la lista ordenada, logro obtener siempre el menor costo posible """

def sumaGolosa(conjunto):
    conjunto.sort()

    total_suma = conjunto[0]
    costo = 0
    i = 1

    while i < len(conjunto):
        total_suma += conjunto[i]
        costo += total_suma
        i+=1
    print("Suma total de la lista:",total_suma)
    print("Costo total:",costo)
    return 0

print(sumaGolosa([1,2,5]),"\n")
print(sumaSelectiva([1,2,-5,40,50,10,30,3], 3),"\n")



""" 29. Deadlines """

def deadlines(tareas):
    tareas.sort()
    max_tareas = []

    tiempo_actual = 0

    for i in range(0, len(tareas)):
            if tiempo_actual + 1 <= tareas[i]:
                max_tareas.append(tareas[i])
                tiempo_actual+=1
    return len(max_tareas)

print("La maxima cantidad de tareas que puedo hacer son", deadlines([2,1,3,2]))



""" 30. Ruta Eficiente """

def rutaEficiente(estaciones, c, m):
    min_estaciones = [0]
    nafta = c
    recorrido_hasta_mardel = 0
    i = 0

    while (i+1) < len(estaciones):
        if nafta > estaciones[i]:                           # Si me queda nafta para seguir:
            nafta -= estaciones[i]                          # Skippeo la estacion (gasto nafta)
            i+=1                                            # Avanzo a la siguiente estacion
        elif nafta == estaciones[i]:
            nafta = c                                       # Restauro nafta (como es == llegar hasta ahi deja nafta en 0)
            min_estaciones.append(i)                        # Agrego la estacion a la lista de minimos
            i+=1                                             # Avanzo a la siguiente estacion
        elif nafta < estaciones[i+1]:
            nafta = c                                       # Restauro nafta (como es < no llego hasta ahi sin cargar nafta antes)
            min_estaciones.append(i)                        # Agrego la estacion a la lista de minimos
            i+=1                                            # Avanzo a la siguiente estacion
    
    print("Conjunto de estaciones minimas que recorrer:",min_estaciones, "Cantidad minima de estaciones:",len(minimo_estaciones))
    return 0



""" 33. MaxMex """
def maxMex(conjunto):
    conjunto.sort()
    total_mex = 0
    vistos = set()

    for i in range(len(conjunto)):
        vistos.add(conjunto[i])
        # Calcula el mex del subconjunto {b_1, ..., b_i}
        mex = 0
        while mex in vistos:
            mex += 1
        total_mex += mex
    return total_mex




""" 35. ParejasdeBaile
a) Si recorro las listas de forma creciente, puedo comparar el abs entre ambos elementos, si es == 0 o == 1,
avanzo en ambas listas. Al ser creciente, si me paso de == 0 o == 1, se que los demas elementos que le sigan
a una lista seran de mayores abs() que 0 o 1, asi que paso al siguiente elemento de una de las listas y la otra
la dejo estatica.
Comparo los elems en la posicion i y j para saber cual de las 2 listas avanzar. Si i < j, avanzo la lista[i] para 
buscar un elemento mayor y comparar nuevamente con lista[j] y ver si se cumple lo pedido. Sino, avanzo la lista[j]

b) """

def parejasDeBaile(multi_a, multi_b):
    i, j = 0, 0
    max_cant = 0
    while i < len(multi_a) and j < len(multi_b):
        if abs(multi_a[i] - multi_b[j]) == 1 or abs(multi_a[i] - multi_b[j]) == 0:
            max_cant += 1
            i += 1
            j += 1
        elif multi_a[i] < multi_b[j]:
            i += 1
        else:
            j += 1
    return max_cant





""" Hacer ejercicios 31, 32 y 34 """






print("===== Tests maxMex =====")
print("MaxMex para la lista [0, 1, 2]:", maxMex([0, 1, 2]))
print("MaxMex para la lista [0, 1, 3]:", maxMex([0, 1, 3]))
print("MaxMex para la lista [3, 0, 1]:", maxMex([3, 0, 1]))
print("MaxMex para la lista [1, 2, 3]:", maxMex([1, 2, 3]))
print("")

print("===== Tests ParejasDeBaile =====")
print(parejasDeBaile([1, 2, 4, 6], [1, 5, 5, 7, 9]))
print(parejasDeBaile([1, 1, 1, 1, 1], [1, 2, 3]),"\n")






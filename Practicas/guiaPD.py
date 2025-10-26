# 9. KingArmy
def kingArmy(n, memo=None):
    memo = {}

    # Casos base (segun ejercito)
    if n <= 1:
        return 1

    # Si ya calculamos este valor, lo devolvemos
    if n in memo:
        return memo[n]

    # Calcular recursivamente y guardar en memo
    memo[n] = kingArmy(n - 1, memo) + kingArmy(n - 2, memo)
    return memo[n]


# 10. Vacations
def vacations(n, dias_gim, dias_comp):
    memo = {}

    def dp(dia, ultima_actividad):
        if dia > n:
            return 0

        if (dia, ultima_actividad) in memo:
            return memo[(dia, ultima_actividad)]

        opciones = []

        # Opción 0: Descansar (siempre posible)
        opciones.append(1 + dp(dia + 1, 0))

        # Opción 1: Gimnasio (si disponible y no repetimos)
        if dia in dias_gim and ultima_actividad != 1:
            opciones.append(dp(dia + 1, 1))

        # Opción 2: Competencia (si disponible y no repetimos)
        if dia in dias_comp and ultima_actividad != 2:
            opciones.append(dp(dia + 1, 2))

        resultado = min(opciones)
        memo[(dia, ultima_actividad)] = resultado
        return resultado

    return dp(1, 0)


# 12. OptiPago
# a, b, c) OptiPago con recursividad
def cc(B, c):
    if c == 0:
        return []
    for b in B:
        if b <= c:
            return [b] + cc(B, c - b)
    return []


# Otra forma con while
def cambio(lista_valores, c):
    i = 0
    lista_total_monedas = []

    while i < len(lista_valores):
        if lista_valores[i] <= c:
            lista_total_monedas.append(lista_valores[i])
            c -= lista_valores[i]
        else:
            i += 1
    return lista_total_monedas


# d, e, f) OptiPago con memoizacion
def optiPago(s, denominaciones, memo={}):
    if s in memo.keys():
        return memo[s]

    # caso base
    if s == 0:
        return 0

    pruebas = []

    for i in range(0, len(denominaciones)):
        if denominaciones[i] <= s:
            pruebas.append(1 + optiPago(s - denominaciones[i], denominaciones, memo))

    mejor = min(pruebas)

    memo[s] = mejor
    return mejor


vuelto = 69
denominaciones = [50, 25, 10, 5, 1]

cantidad = optiPago(vuelto, denominaciones, {})


# 13. AstroTrade
def astroTrade(precios):
    if len(precios) <= 1:
        return 0

    n = len(precios)
    # Ajustamos para que los índices vayan de 1 a n
    p = [0] + precios  # índice 0 no se usa, precios van de 1 a n

    # memo[dia][asteroides] = máxima ganancia
    memo = {}

    def mgn(ast, dia):
        # Caso base: no quedan días
        if dia == 0:
            return 0

        if (ast, dia) in memo:
            return memo[(ast, dia)]

        # Opciones
        res = mgn(ast, dia - 1)  # No hacer nada
        res = max(res, mgn(ast - 1, dia - 1) - p[dia])  # Comprar
        res = max(res, mgn(ast + 1, dia - 1) + p[dia])  # Vender

        memo[(ast, dia)] = res
        return res

    # Llamamos con 0 asteroides al final del día n
    return mgn(0, n)


# 14. Fire
def fire():
    return 0


# 15. CortesEconomicos
def cortesEconomicos(varilla, cortes):
    listaCortes = [0] + sorted(cortes) + [varilla]
    n = len(listaCortes)
    memo = {}

    def costo(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if (j - i) <= 1:
            return 0

        min_costo = float("inf")

        for k in range(i + 1, j):
            costo_actual = listaCortes[j] - listaCortes[i] + costo(i, k) + costo(k, j)
            min_costo = min(min_costo, costo_actual)

        memo[(i, j)] = min_costo
        return min_costo

    return costo(0, n - 1)


"""16. TravesiaVital  
a) Pensar la idea de un algoritmo de backtracking (no hace falta escribirlo).
    Arranco desde el primer valor (matriz[0][0]) y comparo cual es el menor valor entre la suma de matriz[0][0]
    con su valor a la derecha y con su valor hacia abajo => Me quedo con el que me de el menor valor entre ambos
    y sigo comparando con el valor actual que me queda (nuevamente con su derecho y con su elem de abajo).
    
    Finalmente, llego al menor valor posible => Lo transformo a absoluto y le sumo 1 para llegar al menor valor que puedo
    encontrar sin llegar a un elemento menor a 1
"""


# d)
def travesiaVital(matriz):
    filas = len(matriz)  # total de filas de matriz
    columnas = len(matriz[0])  # total de columnas de matriz
    dp = [
        [float("inf")] * columnas for _ in range(filas)
    ]  # Diccionario de longitud matriz lleno de "inf" (p/ luego calcular el menor)
    dp[0][0] = max(1, 1 - matriz[0][0])
    for i in range(filas):
        for j in range(columnas):
            if i > 0:
                dp[i][j] = min(dp[i][j], max(1, dp[i - 1][j] - matriz[i][j]))
            if j > 0:
                dp[i][j] = min(dp[i][j], max(1, dp[i][j - 1] - matriz[i][j]))
    return dp[filas - 1][columnas - 1] + 1


def pilaCauta(pesos, soportes):

    memo = {}
    n = len(pesos)

    def apilar(ultimo, peso_arriba):
        if ultimo == n:
            return 0

        if (ultimo, peso_arriba) in memo:
            return memo[(ultimo, peso_arriba)]

        mejor = 0

        for i in range(ultimo + 1, n):
            if soportes[i] >= peso_arriba:
                mejor = max(mejor, 1 + apilar(ultimo + 1, peso_arriba + pesos[ultimo]))
        memo[(ultimo, peso_arriba)] = mejor
        return mejor

    return apilar(0, 0)


print("Test pilaCauta")
print(pilaCauta([19, 7, 5, 6, 1], [15, 13, 7, 8, 2]))


def operacionesSeqRec(v, w):
    import operator

    operaciones = {"+": operator.add, "x": operator.mul, "↑": pow}

    res = v[0]

    if len(w) != len(v) - 1:
        return 0

    for i in range(1, len(v)):
        res = operaciones[w[i - 1]](res, v[i])
    return res


# print("===== Test operacionesSeqRec =====")
# print(operacionesSeqRec([3, 1, 5, 2, 1]["+", "x", "↑", "x"]))


""" 19. DadosSuma """


# b)
def dadosSuma(n, k, s, min=1):
    if n == 0:
        return [[]] if s == 0 else []

    formas = []

    for i in range(min, k + 1):
        if s >= i:
            for resto in dadosSuma(n - 1, k, s - i, i):
                formas.append([i] + resto)
    return formas


# c) Demostrar que f y g poseen la propiedad de superposición de subproblemas
#   => Para poder lograr obtener los valores que deben obtener los dados para determinado s, debemos recorrer esos
#       mismos valores como mucho k veces, generando que la recursividad de buscar y encontrar el mismo resultado
#       reiteradas veces cree dicha superposición de subproblemas. No guardamos el valor parcial si ya lo buscamos y encontramos
#       al menos una vez, sino que vamos en busca de el (o de otro valor) nuevamente

print("dadosSuma")
print(dadosSuma(3, 4, 6))


""" Hacer ejercicios 11, 14, 17 a 21, 25 """

print("")

print("===== Tests kingArmy =====")
print(kingArmy(5))
print(kingArmy(7))  # Debería imprimir 13
print(kingArmy(10))  # Debería imprimir 55
print("")

print("===== Tests vacations =====")
print("días de descanso:", vacations(4, [2, 3], [1, 2]))
print("")

print("===== Tests OptiPago (recursivo) =====")
print(cc([50, 25, 10, 5, 1], 69))
print(cc([50, 25, 10, 5, 1], 10))
print(cc([50, 25, 10, 5, 1], 5))
print("")

print("===== Tests AstroTrade =====")
print(astroTrade([3, 2, 5, 6]))  # Esperado: 6
print(astroTrade([3, 6, 10]))  # Esperado: 7
print(astroTrade([1, 2, 3, 4, 5]))  # Precio siempre creciente
print(astroTrade([5, 4, 3, 2, 1]))  # Precio siempre decreciente
print(astroTrade([10]))  # Un solo día
print(astroTrade([3, 7]))  # Dos días
print("")

print("===== Tests CortesEconomicos =====")
print(cortesEconomicos(10, [2, 4, 7]))  # Output: 20

print("===== Test TravesiaVital =====")
print(travesiaVital([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))

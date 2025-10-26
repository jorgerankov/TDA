# 3. MaxiSubconjunto

def maxiSubconjunto(matriz, k):
    n = len(matriz)
    mejor_suma = -1
    mejor_conjunto = []

    def bt(res, start):
        if (len(res) == k):
            suma = 0
            for i in range(k):
                for j in range(i+1, k):
                    suma += matriz[res[i][res[j]]]
                    suma += matriz[res[j][res[i]]]
            if suma > mejor_suma:
                mejor_suma = suma
                mejor_conjunto = res[:]
            return
        for l in range(start, n):
            res.append(l)
            bt (res, l+1)
            res.pop()
    bt([],0)
    return mejor_conjunto, mejor_suma



# 5. Palabras en cadena

def palabrasEnCadena(cadena):
    dicc={"TDA", "es", "la", "mejor", "materia", "del", "DC"}
    
    if cadena == "":
        return True
    
    for i in range(1, len(cadena)+1):
        primera = cadena[:i]
        if palabra(primera, dicc):
            if palabrasEnCadena(cadena[i:]):
                return True
    return False

def palabra(palabra, dicc):
    return palabra in dicc


diccVocal = {'a','e','i','o','u'}
alfabeto = 'abcdefghijklmnopqrstuvwxyz'

def sonTresVocales(cadena):
    for i in range(len(cadena) - 2):
        if all(c in diccVocal for c in cadena[i:i+3]):
            return True
    return False

def sonTresCons(cadena):
    for i in range(len(cadena) - 2):
        if all(c not in diccVocal for c in cadena[i:i+3]):
            return True
    return False

def contieneE(cadena):
    return 'e' in cadena



# 7. Dobra
def dobra(cadena):
    if '_' not in cadena:
        # Caso base: la cadena está completa, verificamos las condiciones
        if not contieneE(cadena):
            return False
        if sonTresVocales(cadena):
            return False
        if sonTresCons(cadena):
            return False
        return True
    else:
        idx = cadena.index('_')
        for letra in alfabeto:
            nueva = cadena[:idx] + letra + cadena[idx+1:]
            if dobra(nueva):
                return True
        return False

    

# 8. Cadenas de Adicion
def cadenasDeAdicion(cadena, n, mejor=None):
    # Caso base: si llegamos a n
    if cadena[-1] == n:
        if mejor is None or len(cadena) < len(mejor):
            return list(cadena)
        else:
            return mejor

    # Si nos pasamos, no seguimos
    if cadena[-1] > n:
        return mejor

    # Poda: si ya es más largo que el mejor, no sigo
    if mejor is not None and len(cadena) >= len(mejor):
        return mejor

    # Probar todas las sumas posibles
    for i in range(len(cadena)):
        for j in range(i, len(cadena)):
            nuevo = cadena[i] + cadena[j]                                   # Sumo los 2 ultimos elems de la cadena
            if nuevo > cadena[-1] and nuevo <= n and nuevo not in cadena:   # Si cumple que nuevo es mayor que actual,
                                                                            # nuevo no se pasa de n y la suma no existe en cadena:    
                nueva_cadena = list(cadena) + [nuevo]                       # Agrego el nuevo valor a cadena
                
                res = cadenasDeAdicion(nueva_cadena, n, mejor)              # Llamo a la funcion nuevamente
                                                                            # Comparo mejor actual con la nueva cadena
          
                if res is not None:                                         # Si mi nuevo resultado != None:
                    if mejor is None or len(res) < len(mejor):              # Si mi nuevo res es mas corto que mi mejor actual:
                        mejor = res                                         # Actualizo el mejor
    return mejor




""" Hacer ejercicios 4, 6 """






















print("===== Tests Cadenas de Adicion =====")
print(cadenasDeAdicion([1, 2],15))


print("===== Tests Dobra =====")
print("'e' existe en 'ab_cde_f'?:", 'e' in "ab_cde_f")
print("ab_cde_f:",dobra("ab_cde_f"))
print("aa_abcd_e:",dobra("aa_abcd_e"))
print("fd_ad_dd_e:",dobra("fd_ad_dd_e"))
print("eeeeee:",dobra("eeeeee"))
print("")


print("===== Tests Palabras en cadena =====")
print(palabrasEnCadena("TDAeslamejormateriadelDC"))
print("")


"""  
  print("===== Tests minDif =====")
  print(minDif([1, 2, 3, 4], [6, 4, 2, 1]))
  print("")
  print(minDif([0, 20, 35, 80, 130, 150, 190], [200, 190, 175, 120, 90, 7, 0]))
  
""" 
""" 
Ej Garland

Estado      -> I
            -> Par_Ult
            -> C_par -> Total_Ceros - Cantidad_pares = Cantidad_impares
            ->  

Opciones:
    Valor fijo  -> (i, pares, P) -> (i+1, pares, paridad de a_i)
    Valor 0     -> Coloco par   -> (i+1, pares+1, True) # pares+1 porque coloco un par mas
                -> Coloco impar -> 


"""



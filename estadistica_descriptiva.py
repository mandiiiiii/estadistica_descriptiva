def calcular_media(datos):
    suma = 0
    for dato in datos:
        suma += dato
    media = suma / len(datos)
    return media

def calcular_mediana(datos):
    datos_ordenados = sorted(datos)
    n = len(datos)
    if n % 2 == 0:
        # Si la cantidad de datos es par, la mediana es el promedio de los dos valores centrales
        indice1 = n // 2
        indice2 = indice1 - 1
        mediana = (datos_ordenados[indice1] + datos_ordenados[indice2]) / 2
    else:
        # Si la cantidad de datos es impar, la mediana es el valor central
        indice_central = n // 2
        mediana = datos_ordenados[indice_central]
    return mediana
    
def calcular_moda(datos):
    # Crear un diccionario para contar la frecuencia de cada valor
    frecuencias = {}
    for dato in datos:
        if dato in frecuencias:
            frecuencias[dato] += 1
        else:
            frecuencias[dato] = 1

    # Encontrar el valor (o valores) con la mayor frecuencia
    moda = None
    moda_frecuencia = 0

    for valor, frecuencia in frecuencias.items():
        if frecuencia > moda_frecuencia:
            moda = valor
            moda_frecuencia = frecuencia
        elif frecuencia == moda_frecuencia:
            # Si hay empate, se pueden tener múltiples modas
            moda = (moda , valor)

    return moda

def calcular_rango(datos):
    rango = max(datos) - min(datos)
    return rango

def calcular_varianza(datos):
    media = calcular_media(datos)
    suma_cuadrados_diferencias = 0
    for dato in datos:
        suma_cuadrados_diferencias += (dato - media) ** 2
    varianza = suma_cuadrados_diferencias / len(datos)
    return varianza

def calcular_desviacion_estandar(datos):
    varianza = calcular_varianza(datos)
    desviacion_estandar = varianza ** 0.5
    return desviacion_estandar

def calcular_rango_intercuartilico(datos):
    datos_ordenados = sorted(datos)
    n = len(datos)
    q1_index = int(0.25 * n)
    q3_index = int(0.75 * n)
    
    q1 = datos_ordenados[q1_index]
    q3 = datos_ordenados[q3_index]
    
    rango_intercuartilico = q3 - q1
    return rango_intercuartilico

def calcular_bines_frecuencia_absoluta(datos, num_bines):
    min_valor = min(datos)
    max_valor = max(datos)
    
    # Calcular el ancho del bin
    amplitud_bin = (max_valor - min_valor) / num_bines
    
    # Inicializar los límites de los bines
    limites_bines = [min_valor + i * amplitud_bin for i in range(num_bines + 1)]
    
    # Inicializar las frecuencias de los bines
    frecuencias_bines = [0] * num_bines
    
    # Contar las frecuencias absolutas de cada bin
    for dato in datos:
        for i in range(num_bines):
            if limites_bines[i] <= dato < limites_bines[i + 1]:
                frecuencias_bines[i] += 1
                break
    
    # Crear una lista de tuplas (límite inferior, límite superior, frecuencia)
    bines_frecuencia_absoluta = [
        (limites_bines[i], limites_bines[i + 1], frecuencias_bines[i])
        for i in range(num_bines)
    ]
    
    return bines_frecuencia_absoluta

def calcular_bines_sturges(datos):
    n = len(datos)
    num_bines = int(1 + 3.322 * log10(n))
    return num_bines

def calcular_bines_scott(datos):
    desviacion_estandar = calcular_desviacion_estandar(datos)
    rango = max(datos) - min(datos)
    amplitud_bin = 3.5 * desviacion_estandar / (len(datos) ** (1/3))
    num_bines = int(rango / amplitud_bin)
    return num_bines

def calcular_bines_fd(datos):
    rango_intercuartilico = calcular_rango_intercuartilico(datos)
    amplitud_bin = 2 * rango_intercuartilico / (len(datos) ** (1/3))
    num_bines = int(rango_intercuartilico / amplitud_bin)
    return num_bines

def calcular_cuartiles(datos):
    datos_ordenados = sorted(datos)
    n = len(datos)
    
    q1_index = int(0.25 * n)
    q2_index = int(0.5 * n)
    q3_index = int(0.75 * n)
    
    q1 = datos_ordenados[q1_index]
    q2 = datos_ordenados[q2_index]
    q3 = datos_ordenados[q3_index]
    
    return q1, q2, q3

def calcular_percentil(datos, percentil):
    datos_ordenados = sorted(datos)
    n = len(datos)
    
    # Calcular la posición del percentil en el conjunto ordenado
    posicion_percentil = (percentil / 100) * (n + 1)
    
    # Si la posición es un número entero, el percentil es el valor en esa posición
    if posicion_percentil.is_integer():
        percentil = datos_ordenados[int(posicion_percentil) - 1]
    else:
        # Si la posición no es entera, interpolar entre los valores cercanos
        posicion_superior = int(posicion_percentil)
        posicion_inferior = int(posicion_percentil - 1)
        valor_superior = datos_ordenados[posicion_superior - 1]
        valor_inferior = datos_ordenados[posicion_inferior - 1]
        fraccion_parte_decimal = posicion_percentil - posicion_inferior
        percentil = valor_inferior + fraccion_parte_decimal * (valor_superior - valor_inferior)
    
    return percentil 






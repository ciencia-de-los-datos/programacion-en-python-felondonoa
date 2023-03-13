"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv
from csv import reader
from collections import defaultdict
from datetime import datetime

#Lectura de datos
def lecturaDatos():
    data_list = []
    with open("data.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        for lista in csv_reader:
            data_list.append(lista)

    return (data_list)

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    datos = lecturaDatos()
    sum_colum2 = 0
    for lista in datos:
        sum_colum2 += int(lista[1])
    return sum_colum2


def pregunta_02():
    """
    Retorne la cantidad de listas por cada lista de la primera columna como la lista
    de tuplas (lista, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    datos = lecturaDatos()

    conteo_registros = {}
    for lista in datos:
        registro = lista[0]
        if registro in conteo_registros:
            conteo_registros[registro] += 1
        else:
            conteo_registros[registro] = 1

    lista_tuplas = list(conteo_registros.items())
    lista_tuplas_ordenadas = sorted(lista_tuplas)

    return lista_tuplas_ordenadas


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada registro de la primera columna como una lista
    de tuplas (registro, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    datos = lecturaDatos()

    suma_colum2 = {}
    for lista in datos:
        registro = lista[0]
        columna2 = int(lista[1])
        if registro in suma_colum2:
            suma_colum2[registro] += columna2
        else:
            suma_colum2[registro] = columna2

    lista_tuplas = list(suma_colum2.items())
    lista_tuplas_ordenadas = sorted(lista_tuplas)

    return lista_tuplas_ordenadas


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    
    datos = lecturaDatos()
    conteo_mes = {}

    # Itera sobre los datos y cuenta los registros por mes
    for lista in datos:
        fecha_str = lista[2]
        fecha_obj = datetime.datetime.strptime(fecha_str, '%Y-%m-%d')

    mes_str = '{:02d}'.format(fecha_obj.month)

    if mes_str in conteo_mes:
        conteo_mes[mes_str] += 1
    else:
        conteo_mes[mes_str] = 1

    lista_tuplas_ordenadas = sorted(conteo_mes.items())
    """
    datos = lecturaDatos()

    conteo_mes = defaultdict(int)

    for lista in datos:
        fecha_str = lista[2]  # obtener la fecha como una cadena
        mes_str = fecha_str[5:7]  # extraer el mes como una cadena
        conteo_mes[mes_str] += 1  # incrementar el contador para ese mes

    lista_tuplas_ordenadas = sorted(conteo_mes.items())

    return lista_tuplas_ordenadas


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    registro de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    datos = lecturaDatos()

    grupos = {}

    for lista in datos:
        columna1, columna2 = lista[0], int(lista[1])
        if columna1 in grupos:
            grupos[columna1].append(columna2)
        else:
            grupos[columna1] = [columna2]

    lista_tuplas = []

    for columna1, columna2_list in grupos.items():
        lista_tuplas.append((columna1, max(columna2_list), min(columna2_list)))

    lista_tuplas_ordenadas = sorted(lista_tuplas)

    return lista_tuplas_ordenadas


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres listas corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    datos = lecturaDatos()

    valores_min = defaultdict(lambda: float("inf"))
    valores_max = defaultdict(lambda: float("-inf"))

    for lista in datos:
        valores = lista[4].split(",")
        for valor in valores:
            key, val = valor.split(":")
            val = int(val)
            valores_min[key] = min(valores_min[key], val)
            valores_max[key] = max(valores_max[key], val)

    lista_tuplas_ordenadas = [(key, valores_min[key], valores_max[key])
            for key in sorted(valores_min.keys())]

    return lista_tuplas_ordenadas


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las listas asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    
    datos = lecturaDatos()

    grupos = {}

    for lista in datos:
        valor_col2 = int(lista[1])
        if valor_col2 not in grupos:
            grupos[valor_col2] = []
        grupos[valor_col2].append(lista[0])

    lista_tuplas = []
    for valor_col2, listas in grupos.items():
        lista_tuplas.append((valor_col2, listas))
    
    lista_tuplas_ordenadas = sorted(lista_tuplas)

    return lista_tuplas_ordenadas


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las listas
    (ordenadas y sin repetir lista) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """

    datos = lecturaDatos()

    grupos = {}
    for lista in datos:
        if lista[1] not in grupos:
            grupos[lista[1]] = set()
        grupos[lista[1]].add(lista[0])

    lista_tuplas = []
    for k, v in grupos.items():
        lista_tuplas.append((int(k), sorted(list(v))))

    lista_tuplas_ordenadas = sorted(lista_tuplas)

    return lista_tuplas_ordenadas


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de listas en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """

    datos = lecturaDatos()
    conteo_claves = defaultdict(int)

    for lista in datos:
        for key_value in lista[4].split(','):
            key = key_value.split(':')[0]
            conteo_claves[key] += 1

    conteo_claves = dict(sorted(conteo_claves.items()))

    return conteo_claves


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la lista de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    
    datos = lecturaDatos()
    lista_tuplas = []

    for lista in datos:
        col1 = lista[0]
        conteo_col4 = len(lista[3].split(","))
        conteo_col5 = len(lista[4].split(","))
        lista_tuplas.append((col1, conteo_col4, conteo_col5))

    return lista_tuplas



def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada lista de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    datos = lecturaDatos()

    diccionario = defaultdict(int)

    for lista in datos:
        col2 = int(lista[1])
        col4 = lista[3].split(',')
        for elemento in col4:
            diccionario[elemento] += col2

    diccionario = dict(sorted(diccionario.items()))
    
    return diccionario



def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """

    datos = lecturaDatos()

    diccionario = {}

    for lista in datos:
        clave = lista[0]
        valor = sum(int(item.split(':')[1]) for item in lista[4].split(','))
        diccionario[clave] = diccionario.get(clave, 0) + valor

    diccionario_ordenado = dict(sorted(diccionario.items(), key=lambda x: x[0]))

    return diccionario_ordenado

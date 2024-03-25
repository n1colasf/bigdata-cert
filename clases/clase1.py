def clase1():
    print("--- CLASE 1 ------------------------------------------------------------")
    '''
    COMENTARIOS Y VARIABLES
    '''
    print("Hola Mundo")  # Esto es un comentario

    x = 10
    print(x)
    x = "Diez"
    print(x)

    '''
    DATOS COMPLEJOS
    '''
    # Listas (arrays indexados)
    lista_vacia = []
    lista = ["abc", 4, 3.14]
    print(lista[0])
    print(lista[1])
    print(lista[2])
    print(lista[-1])

    # agregar elementos a la lista
    lista.append("nuevo")
    lista.append(True)
    print(lista)

    # eliminar elementos de la lista
    lista.pop(1)
    lista.remove(True)
    print(lista)

    lista[0] = "xyz"
    print(lista[0:2])  # sin incluir el último elemento
    print(lista[:2])

    # lista anidada
    lista_anidada = [lista, [True, "dos", 3]]
    print(lista_anidada)
    print(lista_anidada[1][0])  # True

    # Tuplas (arrays no indexados)
    tupla = ("abc", 4, 3.14)
    print(tupla[0])
    print(tupla[-1])
    # tupla[0] = "xyz"  # error

    # Diccionarios (arrays asociativos)
    diccionario = {"clave": "valor", "nombre": "Juan", "edad": 25}
    print(diccionario["nombre"])
    print(diccionario["edad"])

    diccionario["nuevo_valor"] = "Nuevo"

    print(diccionario.keys())
    print(diccionario.values())
    print(diccionario.items())

    nuevo_diccionario = diccionario.copy()
    print(nuevo_diccionario)
    diccionario.clear()
    print(diccionario)

    # Conjuntos
    conjunto1 = set(["a","b","a"])
    print(conjunto1)
    conjunto2 = set(["a","c","d","e"])
    conjunto_inmutable = frozenset(["a","b","c"])
    print(conjunto_inmutable)

    print(conjunto2)
    print(conjunto1 & conjunto2)
    print(conjunto1 | conjunto2)

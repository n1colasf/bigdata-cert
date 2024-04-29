def clase3():
    print("--- CLASE 3 ------------------------------------------------------------")
    print("--- 07-03-24 -----------------------------------------------------------")
    '''
    ESTRUCTURAS DE CONTROL
    '''
    # if
    bool = True
    if bool:
        print("Es verdadero")
    else:
        print("Es falso")

    # if anidado
    x = 10
    if x > 5:
        print("Es mayor a 5")
        if x > 7:
            print("Es mayor a 7")
        else:
            print("Es menor o igual a 7")
    else:
        print("Es menor o igual a 5")

    # if con operadores lógicos
    x = 10
    y = 20
    if x > 5 and y > 15:
        print("x es mayor a 5 y y es mayor a 15")
    elif x > 5 or y > 15:
        print("x es mayor a 5 o y es mayor a 15")
    else:
        print("ninguna de las anteriores")

    if 1:  # 1
        print("Es verdadero")

    # for
    for i in range(5):
        print(i)
    else:
        print("Terminó el for")
    print("----")
    for i in range(2, 5):
        print(i)
    print("----")
    for i in range(0, 10, 2):
        print(i)
    print("----")
    lista = ["uno", "dos", "tres"]
    for i in lista:
        print(i)
    print("----")
    for i in range(len(lista)):
        print(lista[i])
    print("----")

    # while
    i = 0
    while i < 5:
        print(i)
        i += 1
    else:
        print("Terminó el while")

    '''
    CONTROL DE BUCLES
    '''
    print("----")
    # break
    for i in range(5):
        if i == 3:
            break
        print(i)
    else:
        print("Terminó el for")
    print("----")
    for i in 'break':
        print(i)
        if i == 'a':
            break
    print("----")

    # continue
    for i in range(5):
        if i == 3:
            continue
        print(i)
    else:
        print("Terminó el for")
    print("----")
    i = 0
    while i < 5:
        i += 1
        if i == 4:
            continue
        print(i)
    print("----")
    '''
    FUNCIONES
    '''

    # función simple
    def saludar():
        print("Hola")

    saludar()
    print("----")

    # función con parámetros
    def saludar_a(nombre):
        print("Hola", nombre)

    saludar_a("Juan")
    print("----")

    # función con retorno
    def sumar(a, b):
        return a + b

    print(sumar(2, 3))
    print("----")

    # función con parámetros por defecto
    def sumar(a, b=1):
        return a + b

    print(sumar(2))
    print("----")

    # función con parámetros variables
    def sumar(*args):
        suma = 0
        for arg in args:
            suma += arg
        return suma

    print(sumar(2, 3, 4))
    print("----")

    # función con parámetros variables
    def sumar(**kwargs):
        suma = 0
        for key in kwargs:
            suma += kwargs[key]
        return suma

    print(sumar(a=2, b=3, c=40))
    print("----")

    # operadores de identidad
    x = 10
    y = 10
    print(x is y)
    print(x is not y)
    print("----")

    # operadores de pertenencia
    lista = [1, 2, 3]
    print(1 in lista)
    print(4 not in lista)
    print("in" in "Python")
    print("----")

    # operadores de comparación
    print(2 == 2)
    print(2 != 2)
    print(2 > 2)
    print(2 >= 2)
    print(2 < 2)
    print(2 <= 2)
    print("----")

    # variables locales y globales
    x = 10

    def funcion():
        x = 20
        print(x)

    funcion()
    print(x)
    print("----")

    y = 10

    def funcion():
        global y
        y = 20
        print(y)

    funcion()
    print(y)
    print("----")

    # formateo de cadenas
    nombre = "Juan"
    edad = 25
    print(nombre, "tiene", edad, "años")
    print(f"Me llamo {nombre} y tengo {edad} años")
    print("Me llamo {} y tengo {} años".format(nombre, edad))
    print("Me llamo {0} y tengo {1} años".format(nombre, edad))
    print("Me llamo {nombre} y tengo {edad} años".format(nombre="Juan", edad=25))

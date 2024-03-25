import os

def clase4():
    print("--- CLASE 4 ------------------------------------------------------------")
    '''
    FUNCION INPUT
    '''
    nombre = input("Ingrese su nombre: ")
    print("Hola", nombre)

    '''
    MANEJO DE ARCHIVOS
    '''
    # Get the absolute path of the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the file
    file_path = os.path.join(script_dir, "../auxiliares/archivo.txt")

    # Use the absolute file path in the open function
    archivo = open(file_path, "w+")

    archivo.write("Hola Mundo!")
    archivo.close()

    # leer archivo
    archivo = open(file_path, "r")
    f_contenido = archivo.read()
    print(f_contenido)
    archivo.close()

    # agregar a archivo
    archivo = open(file_path, "a")
    f_contenido = "\r\n" + "Adios Mundo!"
    print(f_contenido)
    archivo.write(f_contenido)
    f_contenido = "\r\n" + "Agregando una linea."
    archivo.write(f_contenido)
    print(f_contenido)
    archivo.close()

    # leer archivo de a una linea
    archivo = open(file_path, "r")
    f_linea1 = archivo.readline()
    print(f_linea1)
    f_linea2 = archivo.readline()
    print(f_linea2)
    archivo.close()

    # leer archivo de a una linea
    archivo = open(file_path, "r")
    for linea in archivo:
        print(linea)
    archivo.close()

    # usando el with
    with open(file_path, "w") as archivo:
        archivo.write("Hola Mundo!")

    with open(file_path, "r") as archivo:
        f_contenido = archivo.read()
        print(f_contenido)

    '''
    CLASES
    '''
    class UnaClase:
        x = 5

    o = UnaClase()
    print(o.x)
    del o  # elimina el objeto

    class Persona:
        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad

        def saludar(self):  # self es una referencia al objeto, para poder acceder a sus atributos
            print("Hola, mi nombre es", self.nombre, "y tengo", self.edad, "años.")

    p = Persona("Juan", 25)
    p.saludar()

    p2 = Persona("Ana", 30)
    p2.saludar()

    # Variables

    class Auto:
        ruedas = 4
        puertas = 5

        def __init__(self, marca, modelo):
            self.marca = marca
            self.modelo = modelo

    a = Auto("Ford", "Fiesta")
    print(f"Marca: {a.marca}, Modelo: {a.modelo}, Ruedas: {a.ruedas}, Puertas: {a.puertas}")

    a2 = Auto("Chevrolet", "Corsa")
    print(f"Marca: {a2.marca}, Modelo: {a2.modelo}, Ruedas: {a2.ruedas}, Puertas: {a2.puertas}")

    # Encapsulamiento
    class Persona:
        def __init__(self, nombre, edad):
            self._nombre = nombre
            self.__edad = edad

    p = Persona("Juan", 26)
    print(p._nombre)  # Juan
    # print(p.__edad)  # error (no se puede acceder directamente)

    # Herencia simple
    class Vehiculo:
        def __init__(self, marca, modelo):
            self.marca = marca
            self.modelo = modelo

        def presentar(self):
            print(f"Marca: {self.marca}, Modelo: {self.modelo}")

        def laMarca(self):
            print(f"La Marca es: {self.marca}")

    class Auto(Vehiculo):
        def __init__(self, marca, modelo, puertas):
            super().__init__(marca, modelo)  # llama al constructor de la clase padre para herencia
            self.puertas = puertas

        def presentar(self):
            super().presentar()
            print(f"Puertas: {self.puertas}")

    a = Auto("Ford", "Fiesta", 5)
    a.presentar()
    a.laMarca()

    # herencia multiple
    class A:
        def a(self):
            print("A")

    class B:
        def b(self):
            print("B")

    class C(A, B):
        def c(self):
            print("C")

    c = C()
    c.a()
    c.b()
    c.c()

    '''
    MANEJO DE EXCEPCIONES
    '''
    try:
        x = 1 / 0
    except ZeroDivisionError as e:
        print("Error: División por cero")
    except:
        print("Error")
    else:
        print("Sin errores")
    finally:
        print("Finalizado")


    while True:
        try:
            x = int(input("Ingrese un número: "))
        except ValueError:
            print("No es un número")
        else:
            print("Calculando 50/",x, "Resultado= ", 50 / x)
        finally:
            print("Finalizado")
            break

    x = -1
    if x < 0:
        pass
        # raise Exception("Número negativo")  # lanza una excepción

    # Excepciones personalizadas
    class MiError(Exception):
        def __init__(self, mensaje):
            super().__init__(mensaje)

    # raise MiError("Error personalizado")















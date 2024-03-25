from clases import clase1, clase3, clase4, clase6, clase7
from practicos import clase2, practico2, clase5

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

'''
Las clases se pueden importar de otros archivos
'''

print("Clases -----------------------------------------------------")
clase1.clase1()  # Comentarios, variables, listas, tuplas, diccionarios
clase3.clase3()  # Estrucutras de control, funciones, operadores
clase4.clase4()  # Archivos, clases y excepciones
try:
    clase6.clase6()  # Base relacional postgres
except:
    print("No se puede ejecutar clase 6 - Iniciar docker con postgres")
try:
    clase7.clase7()  # Base no relacional cassandra
except:
    print("No se puede ejecutar clase 7 - Iniciar docker con Cassandra")

print("Practicos -----------------------------------------------------")
clase2.practico1()
practico2.clase3()
clase5.practico3()

print("Ejercicios -----------------------------------------------------")
print("Sin ejercicios por el momento")

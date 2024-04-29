import pandas as pd


def clase13_b():
    print("--- CLASE 13: Pandas ----------------------------------------------------")
    print("--- 08-04-24 ------------------------------------------------------------")

    # Crear un diccionario con los datos
    data = {
        'Nombre': ['Juan', 'Ana', 'Pedro', 'Marta'],
        'Edad': [25, 30, 35, 40],
        'Sexo': ['M', 'F', 'M', 'F'],
        'Ciudad': ['Montevideo', 'Punta del Este', 'Maldonado', 'La Pedrera']
    }

    # Crear un DataFrame
    df = pd.DataFrame(data)

    # Imprimir el DataFrame
    print(df)

    # Leer CSV de un archivo
    df = pd.read_csv('auxiliares/datasets/datos_barrios.csv')
    print("Imprimir el CSV con los datos de los barrios")
    print(df)

    # Imprimir la columna de los nombres
    columna = df['BARRIO']
    print(columna.values)

    # Estadísticas descripitivas
    print(df.describe())

    # Ordenar por valores de una columna
    print(df.sort_values('COMUNA'))

    # Limpieza de datos
    df.dropna()  # elimina filas con valores nulos
    df.fillna(0)  # reemplaza valores nulos por 0
    print(df.duplicated())  # muestra las filas duplicadas
    df.drop_duplicates(inplace=True)  # elimina filas duplicadas

    # Crear un nuevo DataFrame
    nuevo_df = pd.DataFrame({
        'Fecha': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04'],
        'Temperatura': ['25', '28', '30', '27'],
        'Humedad': [70, 75, 80, 78]
    })

    # Convertir la columna de fecha a datetime
    nuevo_df['Fecha'] = pd.to_datetime(nuevo_df['Fecha'])

    # Convertir la columna de temperatura a numérica
    nuevo_df['Temperatura'] = pd.to_numeric(nuevo_df['Temperatura'])

    # Imprimir el nuevo DataFrame
    print(nuevo_df)

    # Indexar por etiqueta
    print(nuevo_df['Fecha'])

    # Indexar por posición
    print(nuevo_df.iloc[0])

    # Concatenar DataFrames
    concat_df = pd.concat([df, nuevo_df])
    print("Concatenar DataFrames")
    print(concat_df)

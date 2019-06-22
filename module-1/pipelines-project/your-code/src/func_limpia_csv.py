import pandas as pd
import matplotlib.pyplot as plt

# Escoger las columnas que quieres borrar del df
def elegir_columnas_borrar():
    respuesta = input('Introduce el nombre las columnas que quieres borrar separadas por una coma:')
    respuesta = respuesta.split(',')
    respuesta = [x.strip() for x in respuesta]
    return respuesta

# Borrar columnas seleccionadas anteriormente
def delete_columns(df,lista):
    data = df.drop(lista, axis=1)
    return data

# Eliminar filas que no contengan un item
def delete_rows(df,column,item):    
    df = df.loc[df[column] != item]
    return df

# Borrar un item del nombre de cualquiera de las columnas
def delete_letter_from_column(df,letra):
    df.columns = df.columns.str.replace(letra,'')
    return df

#Filtar por un valor específico de una columna
def filter_item(df,columna,item): 
    df = df[df[columna] == item]
    return df

# Agrupar por columna haciendo la media
def groupby_item_and_mean(df,columna):
    df.groupby([columna]).mean()
    return df

# Crea una columna que suma la producción de todos los años
def total_años(df):
    col_list = list(df)
    df['total_años'] = df[col_list].sum(axis= 1)
    return df

# Crea un top 'num' de la columna que introduzcas
def top_num(df,num,column):
    df = df.nlargest(num, [column])
    return df

# Resetea el index de un dataframe
def reset_index(df):
    df = df.reset_index()
    return df

# Crear una gráfica de barras 
def grafico_barras(df,ejex, ejey):
    grafico = df.plot(kind='bar', x = ejex, y = ejey)
    return grafico
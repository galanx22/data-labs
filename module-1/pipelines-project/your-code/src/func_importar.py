import pandas as pd

def import_csv(file_name):
    data = pd.read_csv('../input/' + file_name +'.csv', encoding = 'ISO-8859-1')
    return data

def export_to_csv(df,archivo):
    df.to_csv(archivo + '.csv')
    return print('El archivo ' + archivo + ' se ha importado correctamente')


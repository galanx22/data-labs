def import_csv(df):
    data = df.read_csv(df +'.csv', encoding = 'ISO-8859-1')
    return data

def export_to_csv(df,nombre_archivo):
    df.to_csv(nombre_archivo + '.csv')
    return print('El archivo ' + nombre_archivo + ' se ha importado correctamente')


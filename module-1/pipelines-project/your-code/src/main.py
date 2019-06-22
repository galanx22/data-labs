from func_importar import *
from func_limpia_csv import *

if __name__ == "__main__":
    df = import_csv('FAO')
    #Area Abbreviation, Area Code, Item Code, Element Code
    columnas_borrar= elegir_columnas_borrar()

    df = delete_columns(df,columnas_borrar)

    df = delete_rows(df,'Element','Feed')

    df = delete_letter_from_column(df,'Y')

    Spain = filter_item(df,'Area','Spain')

    Spain = groupby_item_and_mean(Spain,'Item')

    #latitude,longitude
    columnas_borrar2 = elegir_columnas_borrar()

    Spain = delete_columns(Spain,columnas_borrar2)

    Spain= total_años(Spain)

    Spain_top10 = top_num(Spain,10,'total_años')

    Spain_top10 = reset_index(Spain_top10)

    print(grafico_barras(Spain_top10,'Item','total_años'))

    export_to_csv(Spain_top10,'Spain')

   #################################################

    Vegetables = filter_item(df,'Item','Vegetables')
    Vegetables = groupby_item_and_mean(Vegetables,'Area')
    columnas_borrar3 = elegir_columnas_borrar()
    #latitude,longitude
    Vegetables = delete_columns(Vegetables,columnas_borrar3)
    Vegetables = total_años(Vegetables)
    Vegetables = reset_index(Vegetables)
    Vegetables = top_num(Vegetables,15,'total_años')
    print(grafico_barras(Vegetables,'Area','total_años'))
    export_to_csv(Vegetables, 'Vegetables_top15')
    
    
    




from utils.db import engine, db_to_plaintext
from datetime import datetime

#timestamp de prefijo
prefix_key = str(round(datetime.timestamp(datetime.now())))

header = ['id',
        'nombre_algoritmo',
        'parametros',
        'inicio',
        'fin',
        'estado']

print(db_to_plaintext(engine=engine,
                          sep='|',
                          prefix_key=prefix_key,
                          keys_idx = [0],
                          header=[],
                          tabla = 'datos_ejecucion',
                          path_append_txt='./db/plaintext_db/mh_ejecucion.txt'))

print('Todo ok -  tabla 1')


header = ['id',
'id_ejecucion',
'fitness',
'inicio',
'fin',
'mejor_solucion']

print(db_to_plaintext(engine=engine,
                          sep='|',
                          header=[],
                          keys_idx = [0,1],
                          prefix_key=prefix_key,
                          tabla = 'resultado_ejecucion',
                          path_append_txt='./db/plaintext_db/mh_ejecucion_resultado.txt'))

# print('Todo ok -  tabla 2')

header = ['id',
'id_ejecucion',
'numero_iteracion',
'fitness_mejor',
'fitness_promedio',
'fitness_mejor_iteracion',
'parametros_iteracion',
'inicio',
'fin',
'datos_internos']

print(db_to_plaintext(engine=engine,
                          sep='|',
                          header=[],
                          prefix_key=prefix_key,
                          keys_idx = [0,1],
                          tabla='datos_iteracion',
                          path_append_txt='./db/plaintext_db/mh_ejecucion_iteracion.txt'
                          ))
print('Todo ok -  tabla 3')

from utils.db import engine, plaintext_to_db

print(plaintext_to_db(engine = engine, 
                      sep = '|', 
                      path_txt = 'db/plaintext_db/mh_ejecucion.txt', 
                      table='mh_ejecucion', 
                      header=True))

print(plaintext_to_db(engine = engine, 
                      sep = '|', 
                      path_txt = 'db/plaintext_db/mh_ejecucion_resultado.txt', 
                      table='mh_ejecucion_resultado', 
                      header=True))

print(plaintext_to_db(engine = engine, 
                      sep = '|', 
                      path_txt = 'db/plaintext_db/mh_ejecucion_iteracion.txt', 
                      table='mh_ejecucion_iteracion', 
                      header=True))
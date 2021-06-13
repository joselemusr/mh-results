import os
import sqlalchemy as db
from sqlalchemy.sql import text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData

from dotenv import load_dotenv
load_dotenv()

DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_NAME = os.environ['DB_NAME']
DB_HOST = os.environ['DB_HOST']
DB_PORT = os.environ['DB_PORT']

engine = db.create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

def drop_table(table_name, engine=engine):
    Base = declarative_base()
    metadata = MetaData()
    metadata.reflect(bind=engine)
    table = metadata.tables[table_name]
    if table is not None:
        Base.metadata.drop_all(engine, [table], checkfirst=True)
        
        
def drop_everything(engine):

    from sqlalchemy.engine.reflection import Inspector
    from sqlalchemy.schema import (
        DropConstraint,
        DropTable,
        MetaData,
        Table,
        ForeignKeyConstraint,
    )

    con = engine.connect()
    trans = con.begin()
    inspector = Inspector(engine)


    meta = MetaData()
    tables = []
    all_fkeys = []

    for table_name in inspector.get_table_names():
        fkeys = []

        for fkey in inspector.get_foreign_keys(table_name):
            if not fkey["name"]:
                continue

            fkeys.append(ForeignKeyConstraint((), (), name=fkey["name"]))

        tables.append(Table(table_name, meta, *fkeys))
        all_fkeys.extend(fkeys)

    for fkey in all_fkeys:
        con.execute(DropConstraint(fkey))

    for table in tables:
        con.execute(DropTable(table))

    trans.commit()
    
    
"""
Genera un archivo plano a partir de una tabla sql

@param keys_idx: lista de posiciones a las que deben agregarse un prefijo.
"""   
def db_to_plaintext(engine, sep, prefix_key, keys_idx, path_append_txt, tabla,header=[]):
    
    try: 
        file_object = open(path_append_txt, 'a')
    except: 
        return f'Error al abrir archivo {path_append_txt}'
    
    with engine.connect() as con:

        query = f'SELECT * FROM {tabla}'
        rs = con.execute(query)
        
        if len(header)>0:
            file_object.write(sep.join(header)+'\n')
        
        n = 1
        for row in rs:
            row = list(dict(row).values())
            # agregamos prefijo a las posiciones que correspondan
            for idx in keys_idx:
                row[idx] = prefix_key+'-'+str(row[idx])
                
            row_str = ['NULL' if str(c) == 'None' else str(c) for c in row]
            file_object.write(sep.join(row_str)+"\n")
            
            if n%1000==0:
                print(f'Llevo {n} filas')
                
            n +=1
    
    return True
            
"""
Poblar una tabla en la db a partir de un archivo plano

@param engine: objeto sqlalchemy
@param sep: char de separacion de columnas
@param path_txt: path de ubicacion de plaintext
@param table: tabla de destino 
@param header: True, si tiene encabezado, False si no
"""

def plaintext_to_db(engine, sep, path_txt, table, header=True):

    try: 
        file_object = open(path_txt, 'r')
    except: 
        return f'Error al abrir archivo {path_txt}'
    
    i=0
    for line in file_object:
        i+=1
        if i == 1 & header:
            continue
                
        columns = line.split(sep)
        columns[len(columns)-1] = columns[len(columns)-1].replace("\n","")
        
        query_insert =f"INSERT INTO {table} VALUES ("
        j = 0
        for col in columns:
            if col != 'None':
                query_insert += f"'{col}'"
            else:
                query_insert += f"NULL"

            if j < len(columns)-1:
                query_insert += ","
            j+=1
            
        query_insert += ")"
        
        engine.execute(query_insert)
        if i%1000==0:
            print(f'Llevo {i} filas')
                
    return True
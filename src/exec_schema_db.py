from utils.db import engine, drop_table, drop_everything
from classes.Model import Ejecucion, EjecucionIteracion, EjecucionResultado, Base

from sqlalchemy import inspect


if __name__ == '__main__':
    
    print("="*25,"GENERANDO SCHEMA DB","="*25)
    
    """
    Si queremos borrar alguna tabla en particular o todo, se implementaron
    drop_table(): recibe tabla
    drop_everything(): recibe engine
    
    ## ejemplo: 
    # drop_table('tabla')
    # drop_everything(engine)
    # exit()
    
    """
    drop_everything(engine)
    try:
        
        Base.metadata.create_all(engine, checkfirst=True)
        
        print("Todo Ok")
        
        inspector = inspect(engine)
        table_names = inspector.get_table_names()
        for table_name in table_names:
            print("-"*40)
            print(table_name)
            print("-"*40)
            column_items = inspector.get_columns(table_name)
            for col in column_items:
                # assert len(c) == len(column_items[0])
               print(f'{col["name"]} \t {col["type"]}')
            print("-"*40)
            
        print("="*50)
    except:
        print('Error al generar schema db')
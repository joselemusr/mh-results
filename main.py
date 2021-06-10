import src.utils.db
from src.utils.dicts import options_action, options_server

if __name__ == '__main__':
    """
    Simple menu    
    """

    print("="*(30))
    print('OPCIONES')
    print("="*(30))

    for option,key in options_action.items():
        print(f'[{key}] {option}')
    print("="*(30))
    
    menu_action = True
    while menu_action:
        read_option_plot = input('Selecciona opcion [#]:')
        
        if read_option_plot in list(options_action.values()):
            menu_action = False
            
    print("="*(30))
    print('SERVIDOR')
    print("="*(30))

    for option,key in options_server.items():
        print(f'[{key}] {option}')
    print("="*(30))
    
    menu_server = True
    while menu_server:
        read_option_server = input('Selecciona opcion [#]:')
        
        if read_option_server in list(options_action.values()):
            menu_server = False
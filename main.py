import src.utils.db
from src.utils.dicts import options_action

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
            menu = False
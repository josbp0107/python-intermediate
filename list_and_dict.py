def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Jose", "lastname": "Ballesteros"}

    super_list = [
        {"firstname": "Jose", "lastname": "Ballesteros"},
        {"firstname": "David", "lastname": "Ballesteros"},
        {"firstname": "Carlos", "lastname": "Ballesteros"},
        {"firstname": "Juan", "lastname": "Ballesteros"}
    ]
    
    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-3,2,4,6],
        "floating_nums": [4.5,2.2,1.0,4.56]
    }

    # Primero recorre la lista
    for person in super_list:
        for key, value in person.items(): # Luego recorre por llave y valor del diccionario
            print(f'{key} : {value}')

    # Recorre las llaves y valores al mismo tiempo en un ciclo
    for key, value in super_dict.items():
        print(f'{key} - {value}')

if __name__ == '__main__':
    run()
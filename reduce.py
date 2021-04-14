# Siempre que se vaya a utilizar la funcion reduce, es imprescindible importar el
# modulo de functools
from functools import reduce


def run():

     my_list= [2,2,2,2,2]
    # a obtendrá el valor de la primera posición, mientras que b obtendra el segundo.
    # Cuando se realice la primera operación, es decir, my_list[0] * my_list[1]
    # el resultado se guardará en a y b tendra el valor de la siguiente posicion, es decir,
    # my_list[2], y asi sucesivamente hasta llegar a la ultima posición.
     all_multiplied = reduce(lambda a,b: a*b, my_list)
     print(all_multiplied)    

if __name__ == '__main__':
    run()
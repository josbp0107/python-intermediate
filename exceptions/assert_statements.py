def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = input('Ingresa un número: ')
    # assert tiene dos estados: verdadero ó falso, donde si arroja True ejecutará las siguientes
    # lineas de codigo, y si arroja falso, imprimira un error como esta descrito abajo
    # isnumeric simplemente devuelve TRUE si la variable es un numero y FALSE si no lo es  
    assert num.isnumeric(), "Debes ingresar un número"
    print(divisors(int(num)))
    print("Termino el programa")

if __name__ == '__main__':
    run()
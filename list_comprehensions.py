def run():
    # for i in range(100):
    #     i += 1
    #     print (i**2)
    
    # list_comprehensions = [i**2 for i in range(1, 101) if i % 3 != 0]
    # print (list_comprehensions)
    
    list = [i for i in range(1, 100000) if i%4==0 and i%6==0 and i%9==0]
    print (list)

    # Se coloca el 36, ya que es el minimo comun multiplo de 4,6 y 9
    # 4 6 9 | 2
    # 2 3 9 | 2
    # 1 3 3 | 3
    # 1 1 3 | 3
    # 1 1 1 | 1
    # M.C.M = 2 * 2 * 3 * 3 * 1 = 36 
    list_with_minimum_multiply =[i for i in range(1, 100000) if i%36==0]
    print(list_with_minimum_multiply)    

if __name__ == '__main__':
    run()
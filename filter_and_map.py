my_list = [1,2,3,4,5]

def comprehension():
    squares = [i**2 for i in my_list]
    print(squares)

def function_filter():
    squares = list(filter(lambda x:x**2, my_list))
    print(squares)

def funcition_map():
    squares = list(map(lambda x: x**2, my_list))
    print(squares)

if __name__ == '__main__':
    comprehension()
    function_filter()
    funcition_map()


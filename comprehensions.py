from math import sqrt

from functools import reduce

MY_LIST = [1,4,5,7,9,13,19,21]

def list_comprehension():
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    print("squares", squares)

def dict_comprehension():
    my_dict = {i: sqrt(i) for i in range(1,1001)}
    print("my_dict", my_dict)

def ho_filter():
    
    list_filter = list(filter(lambda x: x % 2 != 0, MY_LIST))
    print("list_filter", list_filter)

def ho_map():
    list_map = list(map(lambda x: x**2, MY_LIST))
    print("list_map", list_map)

def ho_reduce():
    all_multiplied = reduce(lambda a, b: a*b, MY_LIST)
    print("all_multiplied", all_multiplied)

if __name__ == '__main__':
    # list_comprehension()
    # dict_comprehension()
    # ho_filter()
    # ho_map()
    ho_reduce()
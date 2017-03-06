from support import *

def sum_square_diff(n=100):
    natural_list=list(range (1,n+1))
    squared_list=[]
    for i in natural_list:
        squared_list.append(i**2)

    num_1=add_list(squared_list)
    num_2=(add_list(natural_list))**2

    return num_2-num_1
print(sum_square_diff())

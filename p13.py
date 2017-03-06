from support import *

def get_file():
    nums=[]
    with open("100_nums.txt",'r') as in_file:
        for line in in_file:
            nums.append(int(line))
    return nums
            
print(add_list(get_file()))

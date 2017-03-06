from support import *

def sum_of_divisor(n):
    if n==0:
        return -1
    return sum(factors_of(n))-n

the_list= list(range(1,10000))
print(the_list[0])
def amicable_nums(n=10000):
    amicable_list=[]
    for i in range(1,n):
        num_2=sum_of_divisor(i)
        if (i==sum_of_divisor(num_2)) and (i!=num_2):
            amicable_list.append(i)
    
    return amicable_list

        
    

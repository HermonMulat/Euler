from support import *
from itertools import *
def sum_of_divisor(n):
    if n==0:
        return -1
    return sum(factors_of(n))-n

def deficiency(n1):
    if sum_of_divisor(n1)> n1:
        return -1
    if sum_of_divisor(n1)< n1:
        return 1
    return 0
def abund(max_n=10801*2):
    abund=[12]
    
    num=12
    while max_n>(max(abund)):
        if deficiency(num)==-1:
            abund.append(num)
        
        num += 1

    return list(sorted(set(abund)))

def n_sums_of_list(a_list,n2):
    a=list(combinations_with_replacement(a_list,n2))
    sums_of_list=map(sum,a)

    return list(sorted(set(sums_of_list)))

def non_abund_sum_2(n3,a):
    lesser=[1]
    for i in a:
        if i<(n3//2)+2:
            lesser.append(i)
    for i in lesser:
        if (deficiency(i) == -1) and (deficiency(n3-i)==-1):
            return False
    return True

def non_abund_sum(n4):
    
    for i in range((n4//2)+2):
        if (deficiency(i) == (-1)) and (deficiency(n4-i)==(-1)):
            print(i)
            return False
    return True
        
all_num=list(range(20162))
a=abund()
b=n_sums_of_list(a,2)
for i in b:
    if i in all_num:
        all_num.remove(i)
print(sum(all_num))   
        
    

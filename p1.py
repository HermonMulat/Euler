from support import *

def multiples_of_3_5 (n=1000):
    mult_5=5
    mult_3=3
    a_list=[]
    while not((mult_3 > n)):
        a_list.append(mult_3)
        
        if (not(mult_5 in a_list)) and (mult_5<n):
            a_list.append(mult_5)

        mult_3 +=3
        mult_5 +=5

    return list(set(a_list))
    

print (add_list(multiples_of_3_5(1000)))

from support import *

def triangle_num(n):
    tri_num=[]
    for i in range(1,n+1):
        tri_num.append(int((i*(i+1))/2))

    return tri_num
def nth_tri_num(n):
    return int((n*(n+1))/2)
def highly_div_tri_num(n=500):
    i=1
    while len(factors_of(nth_tri_num(i)))<n:
        i=i+1
    return nth_tri_num(i)
    

from support import *
prime_set=[2,3]
def nth_prime(n):
    count=1
    i=3
    while (count!=n):
        if (is_prime(i)):
            prime_set.append(i)
            count +=1
        i +=2

    return prime_set


'''       
def nth_prime_2(n):
    num=3
    count=2
    signal=True
    for i in prime_set:
        if num

    return i-2
'''

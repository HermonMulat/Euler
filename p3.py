from support import *
NUM=600851475143

def prime_factor(n=NUM):
    factor_list = factors_of(n)
    prime_factor =[]

    for i in factor_list:
        if is_prime(i):
            prime_factor.append(i)
    return prime_factor

        




    

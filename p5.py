from support import *
def merge_dict(a,b):
    for i in b:

        if (not(i in a)) or (a[i]<b[i]):
            a[i]=(b[i])

    return a
                
def multiply_out(a):
    product=1
    for i in a:
        product*=(i**a[i])
    return product

def least_multi(n=20):
    all_prime={}
    for i in range (1,n+1):
        a=prime_factorize(i)
        all_prime=merge_dict(all_prime,a)

    return all_prime

print(multiply_out(least_multi()))






def fact(n):
    product=1
    for i in range (1,n+1):
        product*=i
    return product
def comb(n,m):
    return (fact(n)/(fact(m)*fact(n-m)))

print(comb(40,20))

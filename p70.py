import sys
import math
def sieve(n):
    """
    Sieve of Eratosthenes to determine prime factors less than sqrt(n)
    """
    sqrt_n = int(math.sqrt(n)) + 1
    mark = [True for i in range(sqrt_n+1)]
    p=2
    primes = []
    while(p*p <= n ):
        if (mark[p] == True):
            primes.append(p)
            for i in range(2*p,sqrt_n+1,p):
                mark[i] = False
        p +=1

    return primes

def split(n,primes):
    """
    Return 3 integers p,q,phi(p) shuch that pq=n and gcd(p,q) = 1.
    Computing phi(p) is easy since p is made of only a single prime.
    """
    if n==1:
        return 1,1,1
    p = 1
    i = 1
    for i in primes:
        if n%i == 0: # prime i divides n
            while(n%i == 0):
                n /= i
                p *= i
            break
    return p,n,(p - p/i)

def arePerms(a,b):
    return sorted(list(str(a))) == sorted(list(str(b)))

def phi(n):
    """
    Compute Euler's Totient Function upto n.
    """
    primes = sieve(n)
    phis = [i-1 for i in range(n+1)]
    phis[1] = 1

    ans = 2
    min_ratio = 2

    for i in range(2,n+1):
        p,q,k = split(i,primes)
        if q == 1 and p!=1:
            phis[i] = k
        else:
            phis[i] = phis[p]*phis[q]

        ratio = (i*1.0)/phis[i]
        if arePerms(i,phis[i]):
            if ratio < min_ratio:
                min_ratio = ratio
                ans = i
    return ans

def main():
    n = int(sys.argv[1])
    ans = phi(10**n)
    print ans

if __name__ == '__main__':
    import time
    s = time.time()
    main()
    print "Total time taken:", time.time() - s, "seconds"

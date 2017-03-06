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

def phi(n):
    """
    Compute Euler's Totient Function upto n.
    Returns the i which produces max ratio i/phi(i)
    """
    primes = sieve(n)
    phis = [1 for i in range(10)]

    phis[1] = 1
    maxratio = 0
    n_byPhi = 0
    for i in range(10,n+1):
        p,q,k = split(i,primes)
        if p==1:
            phis.append(q-1)
        else:
            phis.append(k*phis[q])

        ratio = phis[i]/(i*1.0)
        if ratio < maxratio:
            maxratio = ratio
            n_byPhi = i
            break

    return n_byPhi

def main():
    n = float(sys.argv[1])
    max_ratio = phi(int(10**n))
    print max_ratio

if __name__ == '__main__':
    import time
    s = time.time()
    main()
    print "Total time taken:", time.time() - s, "seconds"

import sys

def sieve(n):
    mark = [True for i in xrange(n+1)]
    p=2
    while(p*p <= n ):
        if (mark[p] == True):
            for i in xrange(2*p,n+1,p):
                mark[i] = False
        p +=1

    primes = []
    for i in xrange(2,len(mark)):
        if mark[i]:
            primes.append(i)
    return mark, primes

def rad(n, primes, mark):
    if mark[n]:
        return n
    prime_factors = []
    i = 0
    while n != 1:
        p = primes[i]
        if n % p == 0:
            prime_factors.append(p)
        while n%p == 0:
            n /= p
        i += 1
    return reduce(lambda x,y: x*y, prime_factors)

def main():
    limit = 100000
    index = 10000
    mark,primes = sieve(limit)
    print sorted([(rad(i, primes, mark), i) for i in xrange(limit+1)])[index]

if __name__ == '__main__':
    main()

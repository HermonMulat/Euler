import sys
import math
import time

prime_gens = [1]

def get_sqr_free(n):
    sq_fr_mark = [True for i in xrange(n+1)]
    p=2
    while(p*p <= n ):
        if (sq_fr_mark[p]):
            for i in xrange(p*p,n+1,p*p):
                sq_fr_mark[i] = False
        p +=1
    square_free = []
    for i in range(2,len(sq_fr_mark)):
        if sq_fr_mark[i]:
            square_free.append(i)
    return square_free

def sieve2(n):
    """
    Sieve of Eratosthenes to determine prime factors less than n
    """
    s = time.time()
    prime_mark = [True for i in xrange(n+1)]
    p=2
    while(p*p <= n ):
        if (prime_mark[p]):
            for i in xrange(2*p,n+1,p):
                prime_mark[i] = False
        p +=1
    print "Finished sieving",time.time()-s,"seconds"
    primes = []
    for i in range(2,len(prime_mark)):
        if prime_mark[i]:
            primes.append(i)
    print "Extracted primes",time.time()-s,"seconds"
    return prime_mark,primes

def check(n,prime_check,square_free):
    sqrt_n = int(math.sqrt(n))

    for i in square_free:
        if i>sqrt_n:
            break
        if (n%i == 0 and not prime_check[i+ n/i]):
            return False

    return True

def main():
    m = int(sys.argv[1])
    n = 10**m
    prime_check,primes = sieve2(n+1)
    print "Got all my primes"
    square_free = get_sqr_free(int(math.sqrt(n))+1)
    total = 1 # because 1 + 1/1 is a prime
    for p in primes:
        val = p-1
        if ( p%4 == 3 and prime_check[2+val/2] and check(val,prime_check,square_free)):
            total += val
            prime_gens.append(val)
    print total

if __name__ == '__main__':
    s = time.time()
    main()
    print "Total time taken:", time.time()-s,"seconds"

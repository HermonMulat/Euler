import sys,time
def sieve2(n):
    """
    Sieve of Eratosthenes to determine prime factors less than n
    """
    mark = [True for i in xrange(n+1)]
    p=2
    while(p*p <= n ):
        if (mark[p] == True):
            for i in xrange(2*p,n+1,p):
                mark[i] = False
        p +=1

    primes = []
    for i in range(2,len(mark)):
        if mark[i]:
            primes.append(i)

    return mark,primes

def sieve(n):
    """
    Sieve of Eratosthenes to determine prime factors less than n
    """
    mark = [True for i in xrange(n+1)]
    p=2
    while(p*p <= n ):
        if (mark[p] == True):
            for i in xrange(2*p,n+1,p):
                mark[i] = False
        p +=1

    return mark

def is_pan(n):
    n = int("".join(str(n).split().sort()))
    return n == int("".join([i for i in range(1,len(str(n))+1)]))


def main():
    s = time.time()
    n = 10**(int(sys.argv[1]))
    mark,p = sieve2(n)
    print len(p), "primes less than", n
    print "Total time taken :", time.time()-s,"seconds"

if __name__ == '__main__':
    main()

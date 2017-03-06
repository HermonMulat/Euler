import sys
import math

def sieve(n):
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

def resiliant(a,b,primes):
    limit = (a*1.0)/b
    resiliance = 1
    for i in range(len(primes)):
        resiliance *= (1-1.0/primes[i])
        if resiliance < limit:
            return primes[:i+1],resiliance

def solution(a,b,primes):

    primes_to_use,resiliance = resiliant(a,b,primes)
    num = reduce((lambda x, y: x * y),primes_to_use)
    num = num*1.0
    limit = a/b
    while(True):
        act_resiliance = resiliance*(num/(num - 1))
        if act_resiliance < limit:
            return int(num)
        num += num


def main():
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    primes = sieve(1000)
    print solution(a,b,primes)


if __name__ == '__main__':
    import time
    s = time.time()
    main()
    print "Total time taken:", time.time() - s, "seconds"

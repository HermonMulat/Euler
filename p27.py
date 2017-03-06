import math
import bisect
import sys
def sieve(n):

    mark = [True for i in range(n+1)]
    p=2

    while(p*p <= n ):
        if (mark[p] == True):
            for i in range(2*p,n+1,p):
                mark[i] = False
        p +=1

    primes = []
    for i in range(2,n):
        if mark[i]:
            primes.append(i)

    return primes

# Global I dont want to keep passing primes
primes = sieve(int(sys.argv[1])**2)


def isPrime(r):
    if r<0:
        return False
    if r<len(primes):
        index = bisect.bisect_left(primes,r)
        if index <= len(primes)-1:
            return primes[index] == r
        return False
    # not proud of the next case
    else:
        for i in range(2,int(math.sqrt(r))+1):
            if i%r == 0:
                return False
        return True


def check_length(a,b):
    n = 0
    r = b
    while(isPrime(r)):
        n+=1
        r = n*n + (a*n) + b
    return n

def quadratic_pairs(n):
    max_length = 0
    max_pair = (0,0)
    index = bisect.bisect_left(primes,n)
    for b in primes[:index]:
        for a in range(1,n+1):
            index1 = bisect.bisect_left(primes,a+b+1)
            index2 = bisect.bisect_left(primes,b-a+1)
            len1 = 0
            len2 = 0
            if index1 < len(primes) and primes[index1] == (a+b+1):
                len1 = check_length(a,b)
            if index2 < len(primes) and primes[index2] == (b-a+1):
                len2 = check_length(-1*a,b)
            if max_length < max(len1,len2):
                if len1 > len2:
                    max_length = len1
                    max_pair = (a,b)
                else:
                    max_length = len2
                    max_pair = (-1*a,b)

    return max_pair


def main():
    n = int(sys.argv[1])
    a = quadratic_pairs(n)
    print a,""

if __name__ == '__main__':
    main()

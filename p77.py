import sys
import bisect # for binary search
def sieve(n):
    """
    Sieve of Eratosthenes to determine prime factors less than sqrt(n)
    """
    mark = [True for i in range(n+1)]
    p=2
    while(p*p <= n ):
        if (mark[p] == True):
            for i in range(2*p,n+1,p):
                mark[i] = False
        p +=1

    primes = []
    for i in range(2,len(mark)):
        if mark[i]:
            primes.append(i)

    return primes

def countSums(n,nums_to_use):
    look_up = [[1]*(n+1) for i in range(len(nums_to_use))]
    # initialize representation with just nums_to_use[0]
    for i in range(n+1):
        look_up[0][i] = 0 if (i%nums_to_use[0] != 0) else 1

    for i in range(1,len(look_up)):
        for j in range(1,n+1):
            if j - nums_to_use[i] < 0:
                look_up[i][j] = look_up[i-1][j]
            else:
                look_up[i][j] = look_up[i-1][j] + look_up[i][j-nums_to_use[i]]
    return look_up


def main():
    n = 100
    primes = sieve(n)
    table =  countSums(n,primes)
    index = bisect.bisect_right(table[-1],5000)
    print index
    print table[-1][index]


if __name__ == '__main__':
    main()

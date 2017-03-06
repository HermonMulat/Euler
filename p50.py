import sys,time
def sieve(n):
    mark = [True for i in xrange(n+1)]
    p=2
    while(p*p <= n ):
        if (mark[p] == True):
            for i in xrange(2*p,n+1,p):
                mark[i] = False
        p +=1

    primes = []
    prefix = [0]
    for i in xrange(2,len(mark)):
        if mark[i]:
            primes.append(i)
            prefix.append(prefix[-1]+i)

    return prefix[1:],mark

def main():
    n =10**int(sys.argv[1])

    num_of_primes_used = 0
    result = 0
    prefix,mark = sieve(n)

    for i in xrange(len(prefix)-1,-1,-1):
        for j in xrange(i-1-num_of_primes_used,0,-1):
            if prefix[i] -prefix[j] > n:
                break
            else:
                if mark[prefix[i]-prefix[j]]:
                    if num_of_primes_used < (i-j):
                        num_of_primes_used = i-j
                        result = prefix[i]-prefix[j]
    print result


if __name__ == '__main__':
    start = time.time()
    main()
    print "Total time taken:", time.time() - start, "seconds"

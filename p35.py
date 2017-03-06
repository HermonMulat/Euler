import bisect,sys
def sieve(n):
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
def is_in(a,item):
    item = int(item)
    index = bisect.bisect_left(a,item)
    return index<len(a) and a[index]==item

def rot(s):
    cycles = [True]
    cycles += [s for i in s]
    for i in range(2,len(cycles)):
        last = cycles[i-1][-1]
        if last in "24680":
            cycles[0]=False
            return cycles
        rest = cycles[i-1][:-1]
        cycles[i] = last + rest
    return cycles

def main():
    n = int(sys.argv[1])
    primes = sieve(10**n)
    count = 0
    for p in primes:
        cycles = rot(str(p))
        loc_count = 0
        if cycles[0]:
            for j in cycles[1:]:
                if is_in(primes,j):
                    loc_count +=1
                else:
                    break
            if loc_count == len(cycles)-1:
                count +=1
    print count

if __name__ == '__main__':
    import time
    s = time.time()
    main()
    print "\nTotal time:",time.time()-s,"seconds"

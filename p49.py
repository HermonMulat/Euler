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
        if mark[i] and len(str(i)) == 4:
            primes.append(i)

    return primes

def determine_perms(a):
    perm = []
    for i in range(len(a)):
        digits = "".join(sorted(list(str(a[i]))))
        perm_inSet = []
        for j in range(i,len(a)):
            d = "".join(sorted(list(str(a[j]))))
            if d == digits:
                perm_inSet.append(a[j])
        if len(perm_inSet) > 2:
            perm.append(perm_inSet)
    return perm

def filter_arithm(some_list):
    arithm = []
    for i in some_list:
        if ((i[1] - i[0]) == (i[2]-i[1])):
            arithm.append(i)
    return arithm



def main():
    import sys
    n = int(sys.argv[1])
    p = sieve(10**n)
    perms = determine_perms(p)
    arith_perm = filter_arithm(perms)
    for i in arith_perm:
        print "".join([str(j) for j in i])



if __name__ == '__main__':
    import time
    start = time.time()
    main()
    print "Total time taken:", time.time() - start, "seconds"

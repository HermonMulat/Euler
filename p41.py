import sys,time
def sieve(n):
    mark = [True for i in range(n+1)]
    p=2
    while(p*p <= n ):
        if (mark[p] == True):
            for i in range(2*p,n+1,p):
                mark[i] = False
        p +=1

    return mark

def all_perm(astr):
    if len(astr) == 1:
        return [astr]
    a = all_perm(astr[:-1])
    last = astr[-1]
    final = []
    for i in a:
        for j in range(len(i)+1):
            final.append(i[:j]+last+i[j:])

    return final
def main():
    n = int(sys.argv[1])
    prime_mark = sieve(n)
    valid_perms = all_perm("1234")
    valid_perms += all_perm("1234567")

    max_prime = 0
    for i in valid_perms:
        if prime_mark[int(i)]:
            if max_prime < int(i):
                max_prime = int(i)

    print max_prime

if __name__ == '__main__':
    start = time.time()
    main()
    print "Total time taken:",time.time() - start, "seconds"

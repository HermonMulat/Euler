import sys,math,time
from sieve import sieve2
from support import divisors_half
from operator import mul

def combine(a,b_list):
    final = []
    for i in b_list:
        final.append([a]+i)
    return final

def all_facts(n,p_m):
    if p_m[n]:
        return [[n]]
    divisors = divisors_half(n)
    final = [[n]]
    for d in divisors:
        final += combine(d,all_facts(n/d,p_m))
    return final

# DP approch
def all_facts_upton(n,p_m):
    factors = [ [[i]] for i in xrange(n+1)]
    for i in xrange(2,n+1):
        divisors = divisors_half(i)
        final = [[i]]
        for d in divisors:
            final += combine(d,factors[i/d])
        factors[i] = final
    return factors


def main():
    n = int(sys.argv[1])
    max_val = 2*n
    p_m,primes = sieve2(max_val)

    min_ps = [2*i for i in xrange(n+1)]
    all_facts_list = all_facts_upton(max_val,p_m)
    for i in xrange(2,max_val+1):
        facts = all_facts_list[i]
        for j in facts:
            ones =  i - sum(j)
            k = ones + len(j)
            if ones >= 0 and k<=n and min_ps[k]>i:
                min_ps[k] = i
    print sum(set(min_ps[2:]))

if __name__ == '__main__':
    start = time.time()
    main()
    print "Total time taken:",time.time()-start,"seconds"

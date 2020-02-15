import sys
from itertools import permutations, combinations

def sieve2(n):
    mark = [True for i in xrange(n+1)]
    mark[0], mark[1] = False, False
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

MARK, PRIMES = sieve2(10**6)
def is_prime(n):
    if n < len(MARK):
        return MARK[n]
    for p in PRIMES:
        if n % p == 0:
            return False
        if p*p > n:
            return True
    return True

def uniq_partition(n):
    if n == 0:
        return set([tuple([])])
    if n == 1:
        return set([tuple([1])])
    ans = set()
    for i in xrange(1,n+1):
        for part in uniq_partition(n-i):
            ans.add(tuple(sorted(list(part)+[i])))
    return ans

def generate_prime_set(digits, partition):
    if len(partition) == 0:
        return [tuple()]

    ans = set()
    for comb in combinations(digits,partition[0]):
        curr = set(comb)
        rest = [k for k in digits if k not in curr]
        for p in permutations(curr):
            num = int("".join(p))
            if is_prime(num):
                prime_covers = generate_prime_set(rest, partition[1:])
                for cover in prime_covers:
                    pandigital_set = tuple(sorted([num]+list(cover)))
                    ans.add(pandigital_set)
    return ans

def main():
    length = 9
    digits = map(str, range(1, length+1))
    partitions = uniq_partition(length)
    total = 0
    for partition in partitions:
        total += len(generate_prime_set(digits, partition))
    print total

if __name__ == '__main__':
    main()

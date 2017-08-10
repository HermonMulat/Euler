import sys, time, math
from sieve import sieve2

def bisect(n,p):
    count = 0
    while n%p == 0:
        count += 1
        n /= p
    return count,n

def num_divisors(n,primes):
    # start with the assumption that any number, n has atleast 2 factors, 1 & n
    divisor_count = [2 for i in xrange(n+1)]
    divisor_count[1] = 1 # 1 is a special case

    consec_prime_count = 0
    for i in xrange(3,n+1):
        sqrt_i = int(math.sqrt(i))
        for p in primes:
            if p > sqrt_i:
                break
            if i%p == 0:
                count,m = bisect(i,p)
                divisor_count[i] = (divisor_count[m])*(count+1)
                break
        consec_prime_count += (divisor_count[i]==divisor_count[i-1])

    return consec_prime_count

def main():
    n = 10**(int(sys.argv[1]))
    sqrt_n = int(math.sqrt(n))+1
    p_m,primes = sieve2(sqrt_n+1)

    print num_divisors(n,primes)

if __name__ == '__main__':
    s  = time.time()
    main()
    print "Total time taken:", time.time()-s, "seconds"

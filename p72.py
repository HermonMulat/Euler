from support import sieve
import sys,time

def split(n,primes):
    """
    Return 3 integers p,q,phi(p) shuch that pq=n and gcd(p,q) = 1.
    Computing phi(p) is easy since p is made of only a single prime.
    """
    if n==1:
        return 1,1,1
    p = 1
    i = 1
    for i in primes:
        if n%i == 0: # prime i divides n
            while(n%i == 0):
                n /= i
                p *= i
            break
    return int(p),int(n),int(p - p/i)

def phi(n):
    primes = sieve(n)[0]
    phis = [i-1 for i in range(n+1)]
    phis[1] = 1
    phi_sums = [0,0]

    for i in range(2,n+1):
        p,q,k = split(i,primes)
        if q == 1 and p!=1:
            phis[i] = k
        else:
            phis[i] = phis[p]*phis[q]

        phi_sums.append(phi_sums[i-1]+phis[i])

    return phi_sums[-1]

def main():
    print (phi(eval(sys.argv[1])))

if __name__ == '__main__':
    start = time.time()
    main()
    print ("Total time taken:",time.time()-start,"seconds")

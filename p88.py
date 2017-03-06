import sys,math,time
from support import sieve

def factorize_all(num,primes):
    all_facts = {1:{}}
    for n in range(2,num+1):
        ori_n = n
        flag = False
        for p in primes:
            count = 0
            while n%p == 0:
                flag = True
                n = n//p
                count +=1
            if flag:
                break

        factors = all_facts[n].copy()
        factors[p] = count
        all_facts[ori_n] = factors

    return all_facts

def express(n,k,fact):
     pass

def main():
    n = int(sys.argv[1])
    primes = sieve(2*n + 1)
    prime_fact = factorize_all(2*n,primes)
    min_k = ([(i,2*i) for i in range(2,n+1)])
    



if __name__ == '__main__':
    start = time.time()
    main()
    print("Total time taken:",time.time()-start,"seconds")

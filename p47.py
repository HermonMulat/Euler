import time,sys
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

primes = sieve(10000)
def f(num):
    prime_fact = [0 for i in primes]
    count = 0
    for i in range(len(primes)):
        if num % primes[i] == 0:
            count +=1
            while (num % primes[i] == 0):
                num /= primes[i]
                prime_fact[i] += 1
                if num == 1:
                    return count
def main():
    i = 2
    while(True):
        if f(i) == 4 and f(i+1) == 4 and f(i+2)==4 and f(i+3)==4:
            print i
            break
        i +=1

if __name__ == '__main__':
    start = time.time()
    main()
    print "Total time taken:",time.time() - start, "seconds"

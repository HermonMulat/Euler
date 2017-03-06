import sys,time,math
from support import sieve

prime_test = sieve(10**eval(sys.argv[1]))
prime_nums = []
for i in range(2,len(prime_test)):
    if prime_test[i]:
        prime_nums.append(i)

def d1(n):
    if n%2 == 0:
        return n**2 + 1
    return n**2
def d2(n):
    return n**2 - (n-1)

def is_prime(num):
    if num<len(prime_test):
        return prime_test[num]

    for i in prime_nums:
        if i>math.sqrt(num):
            break
        if num%i == 0:
            prime_test[num] = False
            return False

    prime_test[num]=True
    prime_nums.append(num)
    return True

def main():
    primes = 8
    size = 7
    while(primes/(2*size-1) > 0.1):
        size += 1
        a,b = (d1(size),d2(size))
        if is_prime(a):
            primes += 1
        if is_prime(b):
            primes += 1

    print(size)

if __name__ == '__main__':
    start = time.time()
    main()
    print ("Total time taken:",time.time() - start,"seconds")

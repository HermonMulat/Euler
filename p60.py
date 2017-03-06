import sys,time,math
from support import sieve

prime_test = sieve(10**4)
def is_prime(n):

    try:
        return prime_test[n]
    except:
        sqrt_n = int(math.sqrt(n))

        for j in range(2,sqrt_n+1):
            if n%j == 0:
                return False
        prime_test[n] = True
        return True

def check_condition(chain,num):
    n = str(num)
    for i in chain:
        a = int(n+str(i))
        b = int(str(i)+n)
        if not (is_prime(a)) or not(is_prime(b)):
            return False
    return True

def extend_chain(chain, complete_set,chain_length):
    if len(chain) == chain_length:
        return True

    for i in complete_set:
        if check_condition(chain,i):
            chain.append(i)
            if extend_chain(chain,complete_set,chain_length):
                return True
            else:
                del chain[-1] # backtrack

    return False

def main():
    prime_list = []
    for i in prime_test:
        if prime_test[i] and i>=2:
            prime_list.append(i)
    chain_length = int(sys.argv[1])
    chain = []
    extend_chain(chain,prime_list,chain_length)
    print (chain)
    print (sum(chain))

if __name__ == '__main__':
    start = time.time()
    main()
    print("Total time taken:",time.time()-start,"seconds")

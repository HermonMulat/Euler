import sys,time
from math import factorial

fact = [factorial(i) for i in range(10)]
length_map = {}
def chain(num,limit=60):
    n = num
    chain_set = set([])
    length = 0
    while True:
        if num not in chain_set:
            chain_set.add(num)
            length += 1
            digit_fact = [fact[int(i)] for i in str(num)]
            num = sum(digit_fact)
            if num in length_map:
                length += length_map[num]
                break
        else:
            break
    length_map[n] = length
    return length == limit

def main():
    count = 0
    n = eval(sys.argv[1])
    for i in range(10**n):
        if chain(i):
            count += 1
    print (count)
if __name__ == '__main__':
    start = time.time()
    main()
    print ("Total time taken:",time.time()-start,"seconds")

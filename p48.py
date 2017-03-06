
def pow_mod(a,b,n):
    """
    a^b mod n
    """
    a = int(a)
    b = int(b)
    n = int(n)

    b = bin(b)[2:]
    pow_list = []
    num = a
    for i in reversed(b):
        if int(i) == 1:
            pow_list.append(num)
        num = (num**2) % n

    total = 1
    for term in pow_list:
        total = (term*total) % n
    return total


def main():
    import sys
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    total = 0
    for i in range(1,n+1):
        total = (total + pow_mod(i,i,m)) % m
    print total

if __name__ == '__main__':
    import time
    start = time.time()
    main()
    print "Total time taken:", time.time() - start, "seconds"

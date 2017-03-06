import math,sys,time
from support import gcd

def sqrt_frac(n):
    flor = int(math.sqrt(n))
    if flor*flor == n:
        return [flor]
    continued_cycle = [flor]
    a,b,c = 1,1,-1*flor
    a,b,c = (b*b*n) - (c*c),a*b,(a*c*-1)
    d = gcd(b,c)
    e = gcd(a,d)
    a,b,c = a//e, b//e, c//e

    flor  = int((b*math.sqrt(n) + c)/a)
    a,b,c = a,b,c-(a*flor)
    continued_cycle.append(flor)
    original = (a,b,c)
    while True:
        a,b,c = (b*b*n) - (c*c),a*b,(a*c*-1)
        d = gcd(b,c)
        e = gcd(a,d)
        a,b,c = a//e, b//e, c//e

        flor  = int((b*math.sqrt(n) + c)//a)
        a,b,c = a,b,c-(a*flor)
        if (a,b,c) == original:
            break
        continued_cycle.append(flor)


    return continued_cycle

def main():
    n = int(sys.argv[1])
    odd_count = 0
    for i in range(1,n+1):
        cycle_length = len(sqrt_frac(i))-1
        if cycle_length % 2 == 1:
            odd_count +=1
    print (odd_count)

if __name__ == '__main__':
    start = time.time()
    main()
    print ("Total time taken:",time.time()-start,"seconds")

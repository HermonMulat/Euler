import time,sys
from fractions import gcd

def main():
    n = int(sys.argv[1])
    count = 0
    for x in range(1,n+1):
        for y in range(x,n+1):
            g = gcd(x,y)
            count += 2*min(y*g/x, (n-x)*g/y)
    print count + n*n*3

if __name__ == '__main__':
    s = time.time()
    main()
    print "Total time taken:", time.time() - s, "second"

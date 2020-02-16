import sys

def sieve(n, limit):
    mark = [True for i in xrange(n+1)]
    p=2
    while(p*p <= n ):
        if (mark[p] == True):
            for i in xrange(2*p,n+1,p):
                mark[i] = False
        p +=1

    nth = 1
    for pn in xrange(2,len(mark)):
        if mark[pn]:
            if  nth%2 != 0 and 2*nth*pn >= limit:
                return nth
            nth += 1
    # prime bound of 300,000 is enough for solution
    return "Go higher, try higher prime limit"


def main():
    # looking for n such that 2.n.Pn > 10^10
    # n should be odd otherwise (Pn+1)^n + (Pn-1)^n = 2 % Pn^2
    print sieve(int(sys.argv[1]), 10**10)

if __name__ == '__main__':
    main()

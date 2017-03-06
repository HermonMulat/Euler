import math
import sys
def choose(n,r):
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

def countDigitsFact(n,r):
    n = int(n)
    r = int(r)
    digits = 0.0
    a = 1
    for i in range(n,n-r,-1):
        digits += math.log(i,10)
        if (a<=r):
            digits -= math.log(a,10)
    for j in range(a,r+1):
        digits -= math.log(j,10)
    return digits
def countAboveMill(n):
    r = n/2
    count = 0
    while(countDigitsFact(n,r)>6):
        r -=1
        count += 1
    if n%2 == 0:
        return 2*count - 1
    return 2*count

def main():

    count = 0
    for i in range(23,int(sys.argv[1])+1):# no need to check till 23
        d = countDigitsFact(i,i/2) # max combination value
        if d > 6: # means a good candidate
            count += countAboveMill(i)

    print count
    print "time taken", time.time() - start_time, "seconds"



if __name__ == '__main__':
    main()

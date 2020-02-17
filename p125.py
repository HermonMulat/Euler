import sys,math
from itertools import chain

def generate_palindrom(length):
    half = (length+1)/2
    for i in xrange(10**(half-1), 10**half):
        yield int(str(i) + "".join(reversed(str(i/(10**(length%2))))))

def main():
    max_len = int(sys.argv[1])
    # the only 1 digit paliondrom that can be represented as sum of squares
    palindromic_sq_sums = [5]
    for m in chain(*map(generate_palindrom, range(2, max_len+1))):
        k,f_k = 1, 1
        while f_k < m:
            a,b,c = k+1, k*(k+1), f_k-m
            n = (math.sqrt(b*b-4*a*c)-b) / (2*a)
            if int(n) == n:
                palindromic_sq_sums.append(m)
                break
            k +=1
            f_k += (k**2)

    print sum(palindromic_sq_sums)

if __name__ == '__main__':
    main()

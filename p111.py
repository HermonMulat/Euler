import sys,math
from itertools import combinations

def is_prime(n):
    if n <= 2:
        return n == 2
    for i in xrange(2,int(math.sqrt(n))+2):
        if n%i == 0:
            return False
    return True

def possible_nums(digits, length):
    if length == 1:
        return list(digits)
    ans = []
    for i in possible_nums(digits, length-1):
        for d in digits:
            ans.append(i+d)
    return ans

def primes_with_runs(d,length):
    rest_digits = [str(i) for i in xrange(10) if i!=d]
    count, total, max = 0, 0, 0
    is_zero = (d==0)
    no_replace = int(str(d)*length)
    if is_prime(no_replace):
        count += 1
        total += no_replace
        max = length
    for k in xrange(1+is_zero,length):
        # k is the number of digits to replace with randos
        if count > 0:
            max = length-k+1-is_zero
            break
        possible_replacements = possible_nums(rest_digits,k)
        for choice in combinations(range(is_zero,length),k-is_zero):
            if is_zero:
                choice = [0]+list(choice)
            for replacement in possible_replacements:
                val = [str(d)]*length
                for index,c in enumerate(choice):
                    if replacement[0] == "0" and c == 0:
                        continue
                    val[c] = replacement[index]
                num = int("".join(val))
                if is_prime(num):
                    count += 1
                    total += num
    print "{}\t{}\t{}\t{}\t{}".format(d,length,max,count, total)
    return total

def main():
    total = 0
    length = int(sys.argv[1])
    print "D\tLen\tMax\tCount\ttotal"
    print "---------------------------------------------"
    for i in xrange(10):
        total += primes_with_runs(i,length)
    print "---------------------------------------------"
    print "\t\t\t\t{}".format(total)

if __name__ == '__main__':
    main()

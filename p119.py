import sys

def main():
    power_bound = int(sys.argv[1]) # power_bound of 48 is enough to find solu
    limit = 2**power_bound
    digit_pow_sum = set()

    for p in xrange(2,power_bound+1):
        base = 2
        num = base**p
        while num < limit:
            if num > 9 and base == sum([int(i) for i in str(num)]):
                digit_pow_sum.add(num)
            base += 1
            num = base**p

    if len(digit_pow_sum) == 30:
        print sorted(digit_pow_sum)[29]
    else:
        print "Increase power bound and try again :("

if __name__ == '__main__':
    main()

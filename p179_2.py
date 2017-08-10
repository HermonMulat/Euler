def num_divisors2(n):
    divisor_count = [1 for i in xrange(n+1)]
    count = 0
    for i in xrange(2,n+1):
        for j in xrange(i,n+1,i):
            divisor_count[j] += 1
        count += (divisor_count[i]==divisor_count[i-1])
    return count

def main():
    n = 10**(int(sys.argv[1]))
    print num_divisors2(n)

if __name__ == '__main__':
    s  = time.time()
    main()
    print "Total time taken:", time.time()-s, "seconds"

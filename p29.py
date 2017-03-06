import sys,time

def stupid_bruteforce(n):
    nums = set([])
    for i in range(2,n+1):
        for j in range(2,n+1):
            nums.add(i**j)
    print len(nums)

if __name__ == '__main__':
    start = time.time()
    stupid_bruteforce(int(sys.argv[1]))
    print "Total time taken:",time.time() - start, "seconds"

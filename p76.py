import sys

def countSums(n):
    # space complexity O(n)
    nums_to_use = range(1,n)
    prev = [1]*(n+1)
    for i in range(1,len(nums_to_use)):
        curr = [1]*(n+1)
        for j in range(2,n+1):
            if j - nums_to_use[i] < 0:
                curr[j] = (prev[j])
            else:
                curr[j] = (prev[j] + curr[j-nums_to_use[i]])
            if i>= j  and (((curr[j]+1) % 1000000) == 0):
                return [j]

        prev = curr
    return curr


def main():
    n = eval(sys.argv[1])
    ans =  countSums(n)
    print ans[-1]


if __name__ == '__main__':
    import time
    start = time.time()
    main()
    print "Total time taken:",time.time() - start, "seconds"

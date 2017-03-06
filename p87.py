from support import sieve
import sys,math,time,bisect
def main():
    n = eval(sys.argv[1])
    sqrt_n = int(math.sqrt(n))
    p1 = sieve(sqrt_n)
    p2 = p1[:bisect.bisect_left(p1,int(math.pow(n,1/3)))]
    p3 = p1[:bisect.bisect_left(p1,int(math.sqrt(sqrt_n)))]

    num_set = set([])
    for i in p1:
        for j in p2:
            for k in p3:
                num = i**2 + j**3 + k**4
                if  num < n:
                    num_set.add(num)
    print (len(num_set))

if __name__ == '__main__':
    start = time.time()
    main()
    print ("Total time taken:",time.time()-start,"seconds")

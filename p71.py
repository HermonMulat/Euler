from support import gcd
import sys,time

def main():
    nums = 0
    deno = 1
    max_v = 0
    flag = False
    n = int(sys.argv[1])

    for i in range(2,n+1):
        j = int((i*3)/7)
        while (gcd(j,i)!=1):
            j = j-1

        if nums*i < j*deno and (j,i)!=(3,7):
            nums = j
            deno = i
            max_v = j/i


    print (nums,deno,sep="/")

if __name__ == '__main__':
    start = time.time()
    main()
    print ("Total time taken:",time.time()-start,"seconds")

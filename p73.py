from support import gcd
import sys,time

def main():
    ans = 0
    n = eval(sys.argv[1])

    for i in range(2,n+1):
        j = (i/2)
        j = int(j) if int(j)<j else int(j)-1
        while (j > i/3):
            if gcd(j,i)==1:
                ans +=1
            j = j-1

    print (ans)

if __name__ == '__main__':
    start = time.time()
    main()
    print ("Total time taken:",time.time()-start,"seconds")

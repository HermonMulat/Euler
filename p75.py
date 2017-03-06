import sys,time
from support import gcd

def main():
    n =  eval(sys.argv[1])

    tri_pere_count = [0 for i in range(n+1)]
    for u in range(1,865): # solved for u by setting v=1 and p 1.5 mil
        for v in range(1,u):
            if (u+v)%2==1 and gcd(u,v) == 1:
                a = 2*u*v
                b = u*u - v*v
                c = u*u + v*v
                p = a + b + c
                ori_p = p
                while(p<=n):
                    tri_pere_count[p]+=1
                    p += ori_p
    print (tri_pere_count.count(1))

if __name__ == '__main__':
    start = time.time()
    main()
    print ("Total time taken:",time.time()-start,"seconds")

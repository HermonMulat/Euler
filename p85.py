import sys,time,math

def grids(n,m):
    return int((n*n + n)*(m*m +m))//4

def main():
    limit = int(sys.argv[1])
    n = 100
    ans = (n,1)
    diff = abs(limit - grids(n,1))
    for i in range(1,n+1):
        for j in range(1,i+1):
            g = grids(i,j)
            if diff > abs(limit - g):
                diff = abs(limit - g)
                ans = (i,j)

    print ("Dimensions:",ans,"\nArea:",ans[0]*ans[1],"\nNumber of rectangles:",grids(*ans))


if __name__ == '__main__':
    start = time.time()
    main()
    print ("Total time taken:",time.time()-start,"seconds")

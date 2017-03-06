import sys,time,math
def main():
    count = 0
    i=0
    while count < int(sys.argv[1]):
        i+=1
        for j in range(2,2*i+1):
                # the amount of calc used to get this solution ... 
                # LETS JUST SAY ITS A LOT
                sol = math.sqrt(i*i + j*j)
                if sol == int(sol):
                    if i >= j:
                        count += j//2
                    else:
                        count += i - (j+1)//2  +1

    print (i,"=>",count)

if __name__ == '__main__':
    start = time.time()
    main()
    print ("Total time taken:",time.time()-start,"seconds")

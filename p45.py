import math,sys,time

def main():
    i = 144
    while True:
        num = i*(2*i-1)
        k = (1+ math.sqrt(24*num+1))/6
        if k == int(k):
            print i,num
            return
        i +=1


if __name__ == '__main__':
    start = time.time()
    main()
    print "Total time taken:",time.time() - start, "seconds"

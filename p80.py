'''
Don't want to implement sqrt function
'''

import decimal
import math,sys,time


def main():
    decimal.getcontext().prec = 102
    total = 0
    for i in range(int(sys.argv[1])+1):
        if int(math.sqrt(i))**2 != i:
            b = "".join(str(decimal.Decimal(i).sqrt()).split("."))
            #print (b,len(b))
            total += sum([int(i) for i in b[:100]])
    print (total)

if __name__ == '__main__':
    start = time.time()
    main()
    print ("Total time taken:",time.time()-start,"seconds")

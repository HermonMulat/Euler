from fraction import Fraction
import time,sys
def continued_frac(seq):
    cur_frac = Fraction(1,0)
    for i in reversed(seq):
        cur_frac = cur_frac.inverse()+i

    return cur_frac

def main():
    e_seq = [2]
    for i in range(1,eval(sys.argv[1])+1):
        e_seq+=[1,2*i,1]

    e = continued_frac(e_seq)
    print (sum(map(int,list(str(int(e.num))))))


if __name__ == '__main__':
    start = time.time()
    main()
    print ("Total time taken:",time.time() - start,"seconds")

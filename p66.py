import math,sys,time
from support import gcd
def sqrt_frac(n):
    flor = int(math.sqrt(n))
    if flor*flor == n:
        return [flor]
    continued_cycle = [flor]
    a,b,c = 1,1,-1*flor
    a,b,c = (b*b*n) - (c*c),a*b,(a*c*-1)
    d = gcd(b,c)
    e = gcd(a,d)
    a,b,c = a//e, b//e, c//e

    flor  = int((b*math.sqrt(n) + c)/a)
    a,b,c = a,b,c-(a*flor)
    continued_cycle.append(flor)
    original = (a,b,c)
    while True:
        a,b,c = (b*b*n) - (c*c),a*b,(a*c*-1)
        d = gcd(b,c)
        e = gcd(a,d)
        a,b,c = a//e, b//e, c//e

        flor  = int((b*math.sqrt(n) + c)//a)
        a,b,c = a,b,c-(a*flor)
        if (a,b,c) == original:
            break
        continued_cycle.append(flor)

    return continued_cycle

def main():
    n = int(sys.argv[1])
    max_sol = 0
    max_D = 0
    for d in range(2,n+1):

        cont_cyc = sqrt_frac(d)
        cycle_length = len(cont_cyc)-1

        if len(cont_cyc) == 1:
            continue
        n_i = cont_cyc[0]
        prev_n_i = 1

        d_i = 1
        prev_d_i = 0

        i = 0
        while(n_i*n_i - d*d_i*d_i !=1):
            i += 1
            a = cont_cyc[i%cycle_length if i%cycle_length else cycle_length]

            temp1 = n_i
            temp2 = d_i

            n_i = a*n_i + prev_n_i
            d_i = a*d_i + prev_d_i

            prev_n_i = temp1
            prev_d_i = temp2

            g = gcd(n_i,d_i)
            n_i //= g
            d_i //= g

        if max_sol < n_i:
            max_sol = n_i
            max_D = d



    print (max_D)
if __name__ == '__main__':
    start = time.time()
    main()
    print ("Total time taken:",time.time()-start,"seconds")

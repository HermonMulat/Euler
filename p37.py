import sys,time
digit_count = 6 #int(sys.argv[1])
def mid_digits(n,a_str):
    if n<1:
        return [""]
    if n==1:
        return list(a_str)
    a = mid_digits(n-1,a_str)
    ans = []
    for i in a:
        for j in a_str:
            ans.append(i+j)
    return ans

def possible_nums(n,ends="2357",mid="123579"):
    values = mid_digits(n-2,mid)
    final_list = []
    for i in values:
        for j in ends:
            a = j+i
            for k in ends:
                final_list.append(a+k)
    return final_list

def sieve(n):
    mark = [True for i in range(n+1)]
    p=2
    while(p*p <= n ):
        if (mark[p] == True):
            for i in range(2*p,n+1,p):
                mark[i] = False
        p +=1

    return mark

prime_table = sieve(10**digit_count)
def check(num):
    num = str(num)
    if not prime_table[int(num)]:
        return False
    for i in range(1,len(num)):
        if prime_table[int(num[:i])] and prime_table[int(num[-1*i:])]:
            continue
        else:
            return False
    return True

def main():

    poss_list  = [possible_nums(i) for i in range(2,digit_count+1)]
    poss = []
    for i in poss_list:
        poss +=i
    final = []
    for i in poss:
        if check(i):
            final.append(int(i))
        if len(final)==11:
            break
    print sum(final)
    print final

if __name__ == '__main__':
    s = time.time()
    main()
    print "\nTotal time:",time.time()-s,"seconds"

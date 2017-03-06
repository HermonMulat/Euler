import sys,time

def is_pali(n):
    if len(n) <= 1:
        return True
    return n[0]==n[-1] and is_pali(n[1:-1])

def main():
    ans  = []
    n = eval(sys.argv[1])
    for i in range(10**n):
        if is_pali(str(i)) and is_pali(bin(i)[2:]):
            ans.append(i)

    print sum(ans)

if __name__ == '__main__':
    s = time.time()
    main()
    print "\nTotal time:",time.time()-s,"seconds"

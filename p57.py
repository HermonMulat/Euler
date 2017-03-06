import sys,time

def main():
    n = eval(sys.argv[1])
    count = 0
    nume = 1
    deno = 1
    for i in range(10**n):
        nume = 2*deno + nume
        deno = nume - deno
        if len(str(nume))>len(str(deno)):
            count +=1
    print(count)

if __name__ == '__main__':
    s= time.time()
    main()
    print ("Total time taken:",time.time() - s,"seconds")

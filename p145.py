import time,sys

def check(n):
    if n%10 == 0:
        return False
    n2 = str(n)[::-1]
    res = n+int(n2)
    for i in str(res):
        if int(i)%2 == 0:
            return False
    return True

def main():
    n = 10**(int(sys.argv[1]))
    count  = 0
    for i in range(n):
        count += check(i)

    print (count)


if __name__ == '__main__':
    s = time.time()
    main()
    print ("Total time taken:", time.time()-s,"seconds")

def main():

    a = 1
    b = 1
    n = 3
    c = 0
    while(True):
        c = a+b
        if sorted(list(str(c%(10**9)))) == list("123456789"):
            if sorted(list(str(c)[:9])) == list("123456789"):
                break
        temp = a
        a = b
        b = c
        n +=1
    print n
if __name__ == '__main__':
    import time
    s = time.time()
    main()
    print "Time take:",time.time()-s,"seconds"

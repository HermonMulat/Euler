def process(n):
    digits = sorted(list(str(n)))

    for i in range(2,7):
        num = i*n
        d = sorted(list(str(num)))
        if d != digits:
            return False
    return True

def main():
    i=1
    while (True):
        i+=1
        if int(str(i)[0]) == 1 and process(i):
            break;
    print i

if __name__ == '__main__':
    import time
    s = time.time()
    main()
    print "\nTotal time:",time.time()-s,"seconds"

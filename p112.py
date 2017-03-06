def bouncy(n):
    n2 = list(str(n))
    return not (n2 == sorted(n2,reverse=True) or n2 == sorted(n2))


def main():
    m = 19602
    n = 21780

    while( (m*100)/n != 99):
        n+=1
        if (bouncy(n)):
            m+=1
    print n

if __name__ == '__main__':
    main()

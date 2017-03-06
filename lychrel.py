def reverse(n):
    n = str(n)
    n = n[::-1]
    return int(n)

def pali(r):
    if len(r) == 0:
        return True
    return r[0]==r[-1] and pali(r[1:-1])

def reverse_add(n):
    count = 1
    n = n + reverse(n)
    while ((not pali(str(n))) and count<=50):
        count +=1
        n = n + reverse(n)

    return count < 50

def main():
    c = 0
    for i in range(10000):
        if not reverse_add(i):
            c +=1
    print c


if __name__ == '__main__':
    main()

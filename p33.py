import sys,time

def digitCancle(a,b):
    a = int(a)
    b = int(b)
    digits_a = [int(i) for i in str(a)]
    digits_b = [int(j) for j in str(b)]
    for i in range(len(digits_a)):
        for j in range(len(digits_b)):
            if ((digits_b[(j+1) % 2] == digits_a[(i+1) % 2]) and
                (a*digits_b[j] == b*digits_a[i])):
                return True
    return False

def perms(n,digits = "123456789"):
    if n == 1:
        return [int(i) for i in list(digits)]

    a = perms(n-1,digits)
    final = []
    for i in range(len(a)):
        for j in digits:
            final.append(int(str(a[i])+j))
    return final



def main():
    n = int(sys.argv[1])
    pairs =  perms(n)
    wanted = []
    for n in pairs:
        for d in pairs:
            if d>n and digitCancle(n,d):
                wanted.append([n,d])

    num = 1
    deno = 1
    for i in wanted:
        num *= i[0]
        deno *=i[1]
    print num,"/",deno


if __name__ == '__main__':
    s = time.time()
    main()
    print "Total Time Taken:", time.time() - s,"seconds"

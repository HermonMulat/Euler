import sys, time

def make_lookup(n):
    table = [1 for i in range(n+1)]

    for i in range(1,n+1):
        table[i] = table[i-1]*i
    return table

def digit_fact(num,table):
    d = [table[int(i)] for i in str(num)]
    return sum(d) == num


def main():
    ans = []
    table  = make_lookup(9)
    for i in range(10,table[9]):
        if digit_fact(i,table):
            ans.append(i)
    print sum(ans)

if __name__ == '__main__':
    s = time.time()
    main()
    print "Total time taken:", time.time() - s,"seconds"

import sys
def reversePrefix(a):
    sub = 0
    t = sum(a)
    ans = []
    for i in a:
        ans.append(t-sub)
        sub += i
    return ans
def prefix(a):
    ans =[a[0]]

    for i in range(1,len(a)):
        ans.append(a[i]+ans[i-1])
    return ans


def inc(n):
    table = [[1,1,1,1,1,1,1,1,1] for i in range(n)]

    for i in range(1,n):
        table[i] = prefix(table[i-1])

    return table

def main():
    a = dec(int(sys.argv[1]))
    for i in a:
        print i, " ==> ",sum(i)

if __name__ == '__main__':
    main()

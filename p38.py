import sys, time
def multiplied(n):
    range_r = {2:4,4:2,3:3}
    rr = range_r[len(str(n))]
    cated = []
    for i in range(1,rr+1):
        cated.append(str(n*i))
    cated = "".join(cated)
    if len(cated)!=9:
        return 0
    if sorted(list(cated)) == list("123456789"):
        return int(cated)
    return 0


def main():
    final_list = []
    for i in range(10,10**4):
        a =  multiplied(i)
        if a!=0:
            final_list.append(a)
    print max(final_list)

if __name__ == '__main__':
    s = time.time()
    main()
    print "Total Time Taken:", time.time() - s,"seconds"

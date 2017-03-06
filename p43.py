import sys,time

def all_perm(astr):
    if len(astr) == 1:
        return [astr]
    a = all_perm(astr[:-1])
    last = astr[-1]
    final = []
    for i in a:
        for j in range(len(i)+1):
            final.append(i[:j]+last+i[j:])
    return final

def check_property(str_n):
    if str_n[0]=="0":
        return False
    divis_map = dict((j,i) for i,j in zip("2,3,5,7,11,13,17".split(","),range(1,8)))
    for i in range(1,8):
        num = int(str_n[i:i+3])
        if num % int(divis_map[i]) !=0:
            return False
    return True

def main():
    all10pans = all_perm("0123456789")
    final = []
    for i in all10pans:
        if check_property(i):
            final.append(int(i))

    print sum(final)

if __name__ == '__main__':
    start = time.time()
    main()
    print "Total time taken:",time.time() - start, "seconds"

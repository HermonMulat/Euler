import sys,time

def all_perms(a_str):
    if len(a_str) <= 1:
        return [a_str]

    final_piece = a_str[-1]
    lesser_perm = all_perms(a_str[:-1])
    new_perm = []
    for i in range(len(a_str)):
        for perm in lesser_perm:
            new_perm.append(perm[:i]+final_piece+perm[i:])
    return new_perm

def isPanIdentity(ordering):
    rs = 4 # result size is always 4
    digits_left = 9-rs
    for ms in range(digits_left/2 + 1 ,digits_left):
        result = int(ordering[:rs])
        a = int(ordering[rs:rs+ms])
        b = int(ordering[rs+ms:])
        if result == a*b:
            return result
    return 0

def main():
    perms_of_9 = all_perms("123456789")

    final_list = set([])
    for i in perms_of_9:
        r = isPanIdentity(i)
        if r !=0:
            final_list.add(r)

    print "Final answer:",sum(final_list)


if __name__ == '__main__':
    s = time.time()
    main()
    print "Total time take:",time.time() - s,"seconds"

from sieve import *
import sys, time

def check(num_str):
    """
    I am hoping the answer is not one where there are say 4 repeating digits
    but we need to replace only 3 of them - that would complicate things.
    """
    n = list(num_str)
    return n.count('0') == 3 or n.count('1') == 3 or n.count('2') == 3

def count_prime_replacement(num_str,p_m):
    rs = []
    for reps in '012':
        if num_str.count(reps) == 3:
            rs.append(reps)

    for r in rs:
        count = 1
        poss_replacemnt = {"0":"123456789", "1":"23456789","2":"3456789"}
        for i in poss_replacemnt[r]:
            count += p_m[int(num_str.replace(r, i))]
        if count == 8:
            return True

    return False

def main():
    n = 10**(int(sys.argv[1]))
    p_m, p = sieve2(n)
    for i in p:
        num_str = str(i)
        if check(num_str):
            if count_prime_replacement(num_str,p_m):
                print num_str
                return



if __name__ == '__main__':
    s = time.time()
    main()
    print "Total time taken:", time.time() - s, "seconds"

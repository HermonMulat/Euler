import sys

def main():
    total = 0
    for a in xrange(3,1001):
        mod_vals = set()
        curr_mod, max_mod = 2*a, 2*a
        while curr_mod not in mod_vals:
            if curr_mod > max_mod:
                max_mod = curr_mod
            mod_vals.add(curr_mod)
            curr_mod = (2*a+curr_mod) % (a*a)
        total += max_mod
    print total

if __name__ == '__main__':
    main()

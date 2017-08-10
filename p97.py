import sys, time

def main():
    # if i didn't have python's pow i would have had to write it, which
    # would be binary modular exponentiation.
    print  (28433*pow(2,7830457,10**10)+1) % (10**10)

if __name__ == '__main__':
    s  = time.time()
    main()
    print "Total time taken:", time.time()-s, "seconds"

import sys, math

def all_paths(limit, min_chain_length = {1:0}, chain = [1]):
    if chain[-1] > limit:
        return
    # important to reverse chain here because more values get explored fast
    # when adding higher number first
    for i in reversed(chain):
        nxt = chain[-1]+i
        if nxt in min_chain_length and min_chain_length[nxt] < len(chain):
            # ignoring already longer chains. not a very good solution,
            # kinda lucky actually. This should be explored
            continue
        else:
            min_chain_length[nxt] = len(chain)
        all_paths(limit, min_chain_length, chain+[nxt])

def main():
    limit = int(sys.argv[1])
    mults_required = {1:0}
    all_paths(limit, mults_required)
    print sum([mults_required[i] for i in xrange(1,limit+1)])

if __name__ == '__main__':
    main()

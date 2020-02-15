import sys
from itertools import combinations

def main():
    n = int(sys.argv[1])
    half = (n/2) + 1
    f = lambda x: 1 if x==1 else x*f(x-1)
    denom = f(n+1)
    denom_per_round = range(2,n+2)
    numerator = 0
    for choice in combinations(range(n),half):
        last_play = max(choice)
        choice = set(choice)
        num_per_choice = 1
        for index,d in enumerate(denom_per_round):
            if index in choice:
                num_per_choice *= 1
            elif index > last_play:
                num_per_choice *= d
            else:
                num_per_choice *= (d-1)
        numerator += num_per_choice
    print "Probabilty of win: {}/{}".format(numerator, denom)
    print int(denom/numerator)

if __name__ == '__main__':
    main()

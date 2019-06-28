import sys
from itertools import combinations

def can_rep(set1, set2):
    def extend(p, s):
        if p[0] in s: s.add(p[1])
        elif p[1] in s: s.add(p[0])
    extend([6,9], set1)
    extend([6,9], set2)
    dependency_pair = [(0,1),(0,4),(0,9),(1,6),(2,5),(3,6),(6,4),(8,1)]
    for x,y in dependency_pair:
        if not((x in set1 and y in set2) or (x in set2 and y in set1)):
            return False
    return True

def main():
    possible_choice = {}
    for p in combinations(range(10),6):
        possible_choice[tuple(sorted(p))] = set(p)

    keys = possible_choice.keys()
    count = 0
    for i in xrange(len(keys)):
        for j in xrange(i+1,len(keys)):
            count += can_rep(possible_choice[keys[i]], possible_choice[keys[j]])
    print count


if __name__ == '__main__':
    main()

import sys
from itertools import combinations

def main():
    # miss + single and double bulls
    move, doubles = {"miss": 0, "S25": 25, "D25": 50}, ["D25"]
    for i in xrange(1,21):
        # single, double and triple moves
        move["S{}".format(i)] = i
        move["D{}".format(i)] = 2*i
        move["T{}".format(i)] = 3*i
        doubles.append("D{}".format(i))
    limit, total = 100,0
    for d in doubles:
        for m1,m2 in combinations(move.keys(), 2):
            total += (limit > move[d] + move[m1] + move[m2])
    # Combinations don't have the repeats... won't include moves like S1-S1-D2
    for d in doubles:
        for m in move:
            total += (limit > move[m]*2+move[d])

    print total

if __name__ == '__main__':
  main()

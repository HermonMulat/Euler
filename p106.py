import sys
from itertools import combinations
from termcolor import colored

def mustCheck(n):
  all_subs = []
  for i in xrange(1,n):
    all_subs += list(combinations(range(n),i))

  count = 0
  for i in xrange(len(all_subs)):
    for j in xrange(i+1, len(all_subs)):
      s1, s2 = all_subs[i], all_subs[j]
      if len(s1) == len(s2) and len(s1) != 1 and len(set(s1) & set(s2)) == 0:
        if not all(map(lambda x: x[0] < x[1], zip(s1, s2))):
          count += 1
  return count

def main():
  ans = colored(mustCheck(int(sys.argv[1])), "green")
  print ("For a set of size {}, we must check only {} disjoint pairs"
          .format(sys.argv[1], ans))

if __name__ == '__main__':
  main()


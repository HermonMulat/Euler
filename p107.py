import sys
from termcolor import colored

def main():
  edges = []
  n = 0
  total = 0
  for r,line in enumerate(sys.stdin):
    n += 1
    for c,v in enumerate(line.strip().split(",")):
      if v != "-":
        v = int(v)
        total += v
        edges.append((v,r,c))
  total /= 2

  S = [i for i in xrange(n)]
  def find(a):
    while S[a] != a:
      a, S[a] = S[a], S[S[a]]
    return a

  def union(a, b):
    pa,pb = find(a), find(b)
    if pa == pb:
      return
    S[pa] = pb

  edges.sort()
  for w,u,v in edges:
    if find(u) != find(v):
      total -= w
      union(u,v)
  print ("Maximum saving by removing redundant edges is {}"
          .format(colored(total, 'green')))

if __name__ == '__main__':
  main()

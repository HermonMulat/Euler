import sys
from math import sqrt
from itertools import product

def sieve(n):
    mark = [True for i in xrange(n+1)]
    p=2
    while(p*p <= n ):
        if (mark[p] == True):
            for i in xrange(2*p,n+1,p):
                mark[i] = False
        p +=1

    primes = []
    for i in range(2,len(mark)):
        if mark[i]:
            primes.append(i)

    return primes

def properDivSum(n, primeFact):
  if n < 2:
    return 0
  toList = lambda x: [(i, x[i]) for i in x]
  primeFact = toList(primeFact)
  multiplicity = map(lambda x:range(x[1]+1), primeFact)
  divSum = 0
  for pows in product(*multiplicity):
    div = 1
    for i,p in enumerate(pows):
      div *= primeFact[i][0]**p
    if div != n:
      divSum += div
  return divSum

def primeFacts(n):
  primes = sieve(int(sqrt(n))+1)
  allFacts = [{},{}, {2:1}]
  for i in xrange(3, n+1):
    sqrt_i = int(sqrt(i))+1
    for p in primes:
      if p>sqrt_i:
        break
      if i%p == 0:
        factors = dict(allFacts[i/p])
        if p in factors:
          factors[p] += 1
        else:
          factors[p] = 1
        allFacts.append(factors)
        break
    if i+1 != len(allFacts):
      allFacts.append({i:1})
  return allFacts

def main():
  MAX = 1000000
  allFacts = primeFacts(MAX)
  visited = [ False for i in xrange(MAX+1) ]
  chains = [properDivSum(i,v) for i,v in enumerate(allFacts)]
  maxChain, chainStart = 0,0
  for at in xrange(MAX+1):
    if visited[at]:
      continue
    path, curr = {}, at
    while curr <= MAX:
      if curr in path:
        l = len(path) - path[curr] + 1
        if l > maxChain:
          maxChain, chainStart = l, curr
          break
      if visited[curr]:
        break
      path[curr] = len(path)
      visited[curr] = True
      curr = chains[curr]

  at = chains[chainStart]
  minInChain = chainStart
  while at != chainStart:
    minInChain = min(at, minInChain)
    at = chains[at]

  print "Max Chain length: {}\nMin in Chain: {}".format(maxChain, minInChain)

if __name__ == '__main__':
  main()

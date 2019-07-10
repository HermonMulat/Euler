import sys
from termcolor import colored
from itertools import product

def main():
  def count(exps):
    return reduce(lambda x,y: x*y, map(lambda x:(2*x+1), exps))/2

  # Search space is using at most 15 primes with maximum exponent of 4
  n,m = 4,15
  target = 4000000
  primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
  def gen(maxv,t,curr):
    if len(curr) == t:
      solns = count(curr)
      if solns > target:
        return reduce(lambda x,y: x*y, map(lambda x: x[0]**x[1], zip(primes,curr)))
      return float('inf')

    minv = float('inf')
    for i in xrange(maxv,-1,-1):
      minv = min(minv, gen(i,t,curr+[i]))
    return minv

  print ("Smallest number with over {} solution is {}"
          .format(colored(target,'red') ,colored(gen(n,m,[]), "green")))


if __name__ == '__main__':
  main()

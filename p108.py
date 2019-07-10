import sys, math
from termcolor import colored

def sieve(n):
  mark = [True for i in xrange(n+1)]
  primes, p = [], 2
  while (p*p <= n):
    if mark[p]:
      primes.append(p)
      for i in xrange(2*p,n+1,p):
        mark[i] = False
    p += 1
  return primes

def countSoln(n, primes):
  numDivs = 1
  for p in primes:
    if p*p > n:
      break
    exp = 0
    while n%p == 0:
      n /= p
      exp += 1
    numDivs *= (exp+1)
  if n != 1:
    numDivs *= 2
  return numDivs

def main():
  # number of solution is the same as half of the number of divisors of n*n
  # num of divisors of the first 7 primes sqred is over 2k
  MAXVAL = 2*3*5*7*11*13*17
  primes = sieve(int(math.sqrt(MAXVAL))+1)
  ans = MAXVAL
  for i in xrange(1, MAXVAL):
    if countSoln(i*i, primes)/2 > 1000:
      ans = colored(i, "green")
      break
  print "Minimum value of n with at least 1000 solution is {}".format(ans)

if __name__ == '__main__':
  main()

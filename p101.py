import sys
from fractions import Fraction
from termcolor import colored

def optimumPoly(K,newX,y):
  # Use Lagrange iterpolation to solve for new value of x
  newY = Fraction(0,1)
  for i in xrange(K+1):
    Li = Fraction(1,1)
    for j in xrange(K+1):
      if j != i:
        Li *= Fraction(newX-j, i-j)
    newY += (Li*y[i])
  return newY

def main():
  MAX_DEGREE = 10
  f = lambda n: sum([(-n)**i for i in xrange(MAX_DEGREE+1)])
  y = [Fraction(f(x),1) for x in xrange(1,MAX_DEGREE+1)]
  ans = Fraction(0,1)
  for K in xrange(MAX_DEGREE):
    x = K
    while True:
      x += 1
      trueVal, interpolatedVal = Fraction(f(x),1), optimumPoly(K,x,y)
      if trueVal != interpolatedVal:
        ans += interpolatedVal
        break
  print colored("{}/{}".format(ans.numerator, ans.denominator), 'red')


if __name__ == '__main__':
  main()

import sys, math
from termcolor import colored

def main():
  x,r = 3, 1
  T = 0
  while T < 10**12:
    x, r = 3*x + 8*r, 3*r + x
    if x%2 == 1:
      b = (x+1)/2 + r
      T = b+r
      print ("{} blue discs and {} red discs"
              .format(colored(b,'blue'), colored(r, 'red')))

if __name__ == '__main__':
  main()

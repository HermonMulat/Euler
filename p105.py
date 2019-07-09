import sys
from termcolor import colored

def checkSet(nums):
  n = len(nums)
  sums = set()
  maxSums, minSums = [0 for i in xrange(n+1)], [sum(nums) for i in xrange(n+1)]
  for i in xrange(1<<n):
    subLen, subSum = 0, 0
    for j in xrange(n):
      if (i & (1<<j) != 0):
        subLen += 1
        subSum += nums[j]
    if subSum in sums:
      return False
    sums.add(subSum)
    maxSums[subLen] = max(maxSums[subLen], subSum)
    minSums[subLen] = min(minSums[subLen], subSum)

  prev = -1
  for maxS,minS in zip(maxSums, minSums):
    if not(minS > prev):
      return False
    prev = maxS
  return True

def main():
  total = 0
  for line in sys.stdin:
    nums = map(int, line.strip().split(","))
    if checkSet(nums):
      total += sum(nums)
  print "Sum of all Special Sum Sets is {}".format(colored(total, 'green'))


if __name__ == '__main__':
  main()

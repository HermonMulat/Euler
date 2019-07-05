import sys
from collections import Counter
from termcolor import colored

def sqAnagrams(w1, w2, squares):
  maxMatch = -1
  for sq in squares:
    sqMap, invMatch = {}, {}
    match = True
    for w,d in zip(w1,sq):
      if w not in sqMap and d not in invMatch:
        sqMap[w] = d
        invMatch[d] = w
      elif (w in sqMap and sqMap[w] != d) or (d in invMatch and invMatch[d] != w):
        match = False
        break
    if not match:
      continue
    w2Sq = "".join(map(lambda x : sqMap[x], w2))
    if w2Sq in squares:
      maxSq = max(int(sq), int(w2Sq))
      maxMatch = max(maxMatch, maxSq)
  if maxMatch != -1:
    print maxMatch, w1, w2
  return maxMatch

def main():
  words = sys.stdin.readline().strip().replace('"', '').split(',')
  anagrams, n = [], len(words)
  for i in xrange(n):
    for j in xrange(i+1,n):
      w1,w2 = words[i],words[j]
      if Counter(w1) == Counter(w2):
        anagrams.append((w1,w2))

  maxLen = max(map(lambda x: len(x[0]), anagrams))
  sqByLen = dict([(i,set()) for i in xrange(15)])
  for i in xrange(10**((maxLen+1)/2)):
    v = str(i*i)
    sqByLen[len(v)].add(v)

  maxSq = -1
  for w1,w2 in anagrams:
    maxSq = max(maxSq, sqAnagrams(w1,w2,sqByLen[len(w1)]))

  print("\nMax square number formed by square anagram pairs is {}".
        format(colored(maxSq, 'green')) )

if __name__ == '__main__':
  main()

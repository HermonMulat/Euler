import sys

def block_combinations(n,m):
  table = [1 for i in xrange(n+1)]
  for N in xrange(m, n+1):
    for pos in xrange(N-m+1):
      new_n = N-m-pos
      if new_n < m:
        table[N] += 1
      else:
        table[N] += table[new_n]
  return table[-1]-1

def main():
  n = int(sys.argv[1])

  print ( block_combinations(n,2) +
          block_combinations(n,3) +
          block_combinations(n,4))

if __name__ == '__main__':
  main()

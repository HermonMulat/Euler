import sys

def block_combinations(n,m):
  table = [1 for i in xrange(0,n+1)]
  for N in xrange(m, n+1):
    for min_len in xrange(m, N+1):
      for pos in xrange(N-min_len+1):
        new_n = N-min_len-pos-1
        if new_n < m:
          table[N] += 1
        else:
          table[N] += table[new_n]
  return table[-1]

def main():
  print block_combinations(int(sys.argv[1]),3)

if __name__ == '__main__':
  main()

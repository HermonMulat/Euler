import sys
from itertools import product, permutations, combinations

ops = ["+", "-", "*", "/"]
opSeqs = list(product(ops,ops,ops))

def allExpr(nums):
  all_res = set()
  for op1,op2,op3 in opSeqs:
    exprs = ["{}{}{}{}{}{}{}","({}{}{}){}{}{}{}","{}{}({}{}{}){}{}",
             "{}{}{}{}({}{}{})", "({}{}{}{}{}){}{}","{}{}({}{}{}{}{})",
             "({}{}{}){}({}{}{})", "(({}{}{}){}{}){}{}","{}{}(({}{}{}){}{})",
             "{}{}({}{}({}{}{}))","({}{}({}{}{})){}{}"]
    for expr in exprs:
      for a,b,c,d in permutations(nums):
        try:
          finalExpr = expr.format(float(a),op1,float(b),op2,float(c),op3,float(d))
          all_res.add(eval(finalExpr))
        except ZeroDivisionError:
          continue

  # Check how many consecutive numbers starting at 1 are produced
  count = 0
  for i in xrange(1,len(all_res)+1):
    if i in all_res:
      count += 1
    else:
      return count

def main():
  count, ans = 0, []
  for choice in combinations(range(10),4):
    c = allExpr(choice)
    if c > count:
      count, ans = c, choice
  print "The set {} produces max consecutive values from 1 - {}".format(ans,count)

if __name__ == '__main__':
  main()

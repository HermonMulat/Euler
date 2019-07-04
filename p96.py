import sys
from termcolor import colored
from itertools import product
from copy import deepcopy

class Grid:
  def __init__(self, grid):
    if type(grid) == type(self):
      self.probGrid = deepcopy(grid.probGrid)
      return
    self.probGrid = []
    for row in grid:
      probRow = []
      for elem in row:
        e = set(range(1,10)) if elem == 0 else set([elem])
        probRow.append(e)
      self.probGrid.append(probRow)

  def get(self, i, j):
    return self.probGrid[i][j]

  def getRow(self, r):
    row = set()
    for e in self.probGrid[r]:
      if len(e) == 1:
        row |= e
    return row

  def getCol(self, c):
    col = set()
    for i in xrange(9):
      e = self.probGrid[i][c]
      if len(e) == 1:
        col |= e
    return col

  def getCell(self,r,c):
    cell = set()
    for i in xrange(r*3, r*3+3):
      for j in xrange(c*3, c*3+3):
        e = self.probGrid[i][j]
        if len(e) == 1:
          cell |= e
    return cell

  def update(self, r,c):
    curr = self.probGrid[r][c]
    if len(curr) == 1:
      return False, curr
    forbidden = self.getRow(r) | self.getCol(c) | self.getCell(r/3,c/3)
    posUpdate = curr.difference(forbidden)
    return True, posUpdate

  def isFilled(self, r, c):
    return len(self.probGrid[r][c]) == 1

  def isComplete(self):
    for i in xrange(9):
      for j in xrange(9):
        if not self.isFilled(i,j):
          return False
    return True

  def show(self):
    def getElem(s):
      if len(s) != 1:
        return " "
      else:
        for i in s:
          return str(i)

    for r,row in enumerate(self.probGrid):
      if r % 3 == 0:
        print "+---+---+---+"
      strR = [getElem(elem) for elem in row]
      rowS = "".join(["|"] + strR[:3] +["|"]+ strR[3:6] +["|"]+ strR[6:] + ["|"])
      print rowS
    print "+---+---+---+"

TOTAL = 0
def sudoku(grid):
  global TOTAL
  while not grid.isComplete():
    for i,j in product(range(9),range(9)):
      change, updateSet = grid.update(i,j)
      grid.probGrid[i][j] = updateSet
    for i,j in product(range(9),range(9)):
      change, updateSet = grid.update(i,j)
      toRemove = set()
      if change:
        if len(updateSet) == 0:
          return False
        for elem in updateSet:
          newGrid = Grid(grid)
          newGrid.probGrid[i][j] = set([elem])
          if sudoku(newGrid):
            return True
          else:
            toRemove.add(elem)
        grid.probGrid[i][j] = updateSet.difference(toRemove)

  grid.show()
  getE = lambda x,y: str(list(grid.probGrid[x][y])[0])
  TOTAL += int("".join([getE(k[0],k[1]) for k in [(0,0),(0,1),(0,2)]]).strip())
  return True

def main():
  grid, count = [], 9
  gridCount = 0
  for line in sys.stdin:
    count += 1
    if count == 10:
      count, grid = 0, []
    else:
      grid.append(map(int, list(line.strip())))
      if count == 9:
        g = Grid(grid)
        gridCount += 1
        print "Solution for grid {}:".format(gridCount)
        sudoku(g)
        print
  ans = colored(TOTAL, 'green')
  print "\nSum of first 3 digits of all 50 solved grids is {}".format(ans)

if __name__ == '__main__':
  main()


import sys, curses, time
from termcolor import colored
from itertools import product
from collections import defaultdict as dd
from copy import deepcopy

stdscr = curses.initscr()
curses.start_color()
curses.use_default_colors()
stdscr.clear()
curses.noecho()
curses.cbreak()

class Grid:
  def __init__(self, grid):
    self.grid = grid
    self.rows, self.cols, self.box = dd(set), dd(set), dd(set)
    for r in range(9):
      for c in xrange(9):
        v = self.get(r,c)
        if v != 0:
          self.rows[r].add(v)
          self.cols[c].add(v)
          self.box[(r/3,c/3)].add(v)

  def get(self,r,c):
    return self.grid[r*9 + c]
  def set(self,r,c,v):
    self.grid[r*9 + c] = v
    self.rows[r].add(v)
    self.cols[c].add(v)
    self.box[(r/3,c/3)].add(v)
  def unset(self,r,c,v):
    self.grid[r*9 + c] = 0
    self.rows[r].remove(v)
    self.cols[c].remove(v)
    self.box[(r/3,c/3)].remove(v)

  def show(self):
    gridStr = []
    for r in xrange(9):
      if r % 3 == 0:
        gridStr.append("+---+---+---+")
      strR = [str(self.get(r,c)) for c in xrange(9)]
      rowS = "".join(["|"] + strR[:3] +["|"]+ strR[3:6] +["|"]+ strR[6:] + ["|"])
      gridStr.append(rowS.replace("0", " "))
    gridStr.append("+---+---+---+")
    return gridStr

TOTAL = 0
def sudoku(grid, at, px, py, show=True):
  global TOTAL,stdscr
  r,c =  divmod(at,9)
  if show:
    for i,s in enumerate(grid.show()):
      stdscr.addstr(px+i+1,py,s)
    stdscr.refresh()

  if at == 81:
    TOTAL += int("".join(map(str,grid.grid[:3])))
    return True

  if grid.get(r,c) != 0:
    return sudoku(grid, at+1, px, py, show)

  possible = set(range(1,10)).difference( grid.rows[r], grid.cols[c],
                    grid.box[(r/3, c/3)] )
  for v in possible:
    grid.set(r,c,v)
    if sudoku(grid, at+1, px, py, show):
      return True
    grid.unset(r,c,v)
  return False

def main():
  global stdscr
  curses.init_pair(1, curses.COLOR_GREEN, -1)
  grid, count = [], 9
  gridCount = 0
  for line in sys.stdin:
    count += 1
    if count == 10:
      count, grid = 0, []
    else:
      grid += map(int, list(line.strip()))
      if count == 9:
        g = Grid(grid)
        px,py = ( (gridCount%15)/5)*14, ((gridCount%15)%5)*14
        gridCount += 1
        stdscr.addstr(px,py, "Solving G{}:".format(gridCount),curses.color_pair(1))
        sudoku(g, 0, px, py, bool(int(sys.argv[1])))
        stdscr.addstr(px,py, "G{}:        ".format(gridCount))

if __name__ == '__main__':
  '''
  run as:
    python p96.py [show progress: 1/0] < p096_sudoku.txt
  '''
  try:
    main()
  finally:
    curses.echo()
    curses.nocbreak()
    curses.endwin()
    ans = colored(TOTAL, 'green')
    print "Sum of first 3 digits of all 50 solved grids is {}".format(ans)

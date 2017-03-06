import sys
import math
def main():
    f = open(sys.argv[1],"r")

    biggest = 0.0
    max_line = 0
    line_num = 1

    for line in f:
        line = line.split(",")
        b = int(line[0])
        ex = int(line[1])
        val = ex*math.log(b)
        if val > biggest:
            biggest = val
            max_line = line_num
        line_num +=1
    print biggest
    print max_line

if __name__ == '__main__':
    main()

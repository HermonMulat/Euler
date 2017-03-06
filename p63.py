import math
def count(p):
    counter = 0
    for i in range(1,10):
        d = len(str(int(math.pow(i,p))))
        if d == p:
            counter +=1
    return counter
def main():
    total = 0
    for i in range(1,23):
        c= count(i)
        print i, c
        total += c

    return total

if __name__ == '__main__':
    print main()

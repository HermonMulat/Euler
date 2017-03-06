import sys
def f1(x):
    if x%2 == 0:
        return x*x +1
    return x*x
def f2(x):
    return x*x - x +1

def main():
    print (sum([f1(x)+f2(x) for x in range(2,int(sys.argv[1]) +1)]) + 1)

if __name__ == '__main__':
    main()

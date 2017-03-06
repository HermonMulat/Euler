import sys,time
def digitSum(num):
    return sum(map(int,list(str(num))))

def main():
    n = eval(sys.argv[1])
    max_sum = 0
    for i in range(n):
        for j in range(n):
            val = digitSum(i**j)
            if max_sum < val:
                max_sum = val
    print(max_sum)


if __name__ == '__main__':
    s= time.time()
    main()
    print ("Total time taken:",time.time() - s,"seconds")

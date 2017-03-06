import sys,time,math

WORD_NUM = dict((i,j) for i,j in zip(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),range(1,27)))

def word_val(word):
    return sum([WORD_NUM[i] for i in word])
def is_tri(num):
    num2 = (8*num)+1
    return (int(math.sqrt(num2)))**2 == num2

def main():
    f = open(sys.argv[1],"r")
    count = 0
    lines = f.readline().split('\",\"')
    for word in lines:
        num = word_val(word.strip())
        if num!=0 and is_tri(num):
            count+=1
    print count

if __name__ == '__main__':
    start = time.time()
    main()
    print "Total time taken:",time.time() - start, "seconds"

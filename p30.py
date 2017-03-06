'''
The zero analysis solution - I made no effort to solve this and I am not
proud.
'''
import sys
def digit_pow(num,i):
    d = [int(j)**i for j in str(num)]
    return sum(d) == num
def main():
    fith_list = []
    i = 2
    while (len(str(i))!= int(sys.argv[1])):
        if digit_pow(i,5):
            fith_list.append(i)
        i +=1
    return fith_list

if __name__ == '__main__':
    import time
    s = time.time()
    a= main()
    print a,"==>",sum(a)
    print "Time taken:",time.time() - s, "seconds"

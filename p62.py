import sys,time
from math import ceil

def process(a_list,limit):

    for i in range(len(a_list)):
        match = [a_list[i]]
        d = sorted(list(str(a_list[i])))
        for j in range(i+1,len(a_list)):
            if d == sorted(list(str(a_list[j]))):
                match.append(a_list[j])
        if len(match) == limit:
            return match


def main():
    k = 12
    limit = int(sys.argv[1])
    ans = None
    while(ans == None):

        lower_bound = int(10**((k-1)/3)+1)
        upper_bound = int(10**(k/3)+1)

        cube_list = []
        for i in range(lower_bound,upper_bound):
            cube_list.append(i**3)
        ans = (process(cube_list,limit))
        k += 1
    print (ans)

if __name__ == '__main__':
    start = time.time()
    main()
    print("Total time take:",time.time()-start,"second")

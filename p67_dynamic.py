import sys,time

def max_path(a_list):
    path_sum = [[0]*(len(i)+2) for i in a_list]
    path_sum[0][1] = a_list[0][0]
    for i in range(1,len(a_list)):
        for j in range(len(a_list[i])):
            path_sum[i][j+1] = max(path_sum[i-1][j+1],path_sum[i-1][j]) + a_list[i][j]
    return max(path_sum[-1])
    
def main():
    tri = []
    with open(sys.argv[1],"r") as in_file:
        for line in in_file:
            line = [int(i) for i in line.split()]
            tri.append(line)
    print(tri[:3])
    print (max_path(tri))


if __name__ == '__main__':
    start = time.time()
    main()
    print ("Total time taken:",time.time()- start,"seconds")

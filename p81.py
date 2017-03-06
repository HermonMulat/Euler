from graph import *
def path_sum(filename):
    f = open(filename,"r")
    matrix = Graph()
    # build graph
    v_table = []
    # add all vertices
    for line in f:
        nums = [int(i) for i in line.strip().split(",")]
        row = []
        for key in nums:
            v = matrix.addVertex(key)
            row.append(v)
        v_table.append(row)

    # create all edges
    length = len(v_table)
    for i in range(length):
        for j in range(length):
            if i+1 < length:
                matrix.addEdge(v_table[i][j],v_table[i+1][j])
            if j+1 < length:
                matrix.addEdge(v_table[i][j],v_table[i][j+1])

    start_v = v_table[0][0]
    destination = v_table[-1][-1]
    path_distance = matrix.path(start_v,destination)
    print "Total path cost:", path_distance

def main():
    import sys
    import random
    path_sum(sys.argv[1])

if __name__ == '__main__':
    import time
    start = time.time()
    main()
    print "Total time taken:",time.time() - start, "seconds"

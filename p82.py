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
                matrix.addEdge(v_table[i][j],v_table[i+1][j])  # down
            if j+1 < length:
                matrix.addEdge(v_table[i][j],v_table[i][j+1])  # right
            if i-1 >= 0:
                matrix.addEdge(v_table[i][j],v_table[i-1][j])  # up

    left_col = []
    right_col = []
    for i in v_table:
        left_col.append(i[0])
        right_col.append(i[-1])

    min_dist = -1
    for startV in left_col:
            distance = matrix.all_path(startV)
            for dest in right_col:
                if min_dist == -1 or distance[dest.id] < min_dist:
                    min_dist = distance[dest.id]


    print "Total path cost:", min_dist

def main():
    import sys
    import random
    path_sum(sys.argv[1])

if __name__ == '__main__':
    import time
    start = time.time()
    main()
    print "Total time taken:",time.time() - start, "seconds"

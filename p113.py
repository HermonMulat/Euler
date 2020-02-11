import sys

def increasing(length):
    count = [1 for i in xrange(10)]
    count[0] = 0
    total = 0
    for i in xrange(1, length):
        total += sum(count)
        nxt = [0 for i in xrange(10)]
        for ending in xrange(10):
            for extension in xrange(ending,10):
                nxt[extension] += count[ending]
        count, nxt = nxt, count
    total += sum(count)
    return total

def decreasing(length):
    count = [1 for i in xrange(10)]
    count[0] = 0
    total = 0
    for i in xrange(1, length):
        total += sum(count)
        nxt = [0 for i in xrange(10)]
        for ending in xrange(10):
            for extension in xrange(0,ending+1):
                nxt[extension] += count[ending]
        count, nxt = nxt, count
    total += sum(count)
    return total

def main():
    length = int(sys.argv[1])
    print increasing(length)+decreasing(length)-(9*length)

if __name__ == '__main__':
    main()

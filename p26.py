import sys 

def count_cycle_length(n):
    """
    manual division of 1/n
    """
    remenders = [10**(len(str(n)))%n]
    r = remenders[-1]*10 % n
    while (r != remenders[0] and r!=0 and len(remenders)<n):
        remenders.append(r)
        r = remenders[-1]*10 % n

    if r==0 or len(remenders)==n:
        return 0
    return len(remenders)

def main():
    max_cycle = 6
    max_num = 7
    for i in range(1,1001):
        c = count_cycle_length(i)
        if c>max_cycle:
            max_cycle = c
            max_num = i
    print max_num


if __name__ == '__main__':
    main()

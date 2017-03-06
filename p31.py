import sys

def coinCount(n,coins):
    look_up = [[1]*(n+1) for i in range(len(coins))]
    for i in range(1,len(look_up)):
        for j in range(2,n+1):
            if j - coins[i] < 0:
                look_up[i][j] = look_up[i-1][j]
            else:
                look_up[i][j] = look_up[i-1][j] + look_up[i][j-coins[i]]
    return look_up


def main():
    coins = [1,2,5,10,20,50,100,200]
    table =  coinCount(200,coins)
    print table[-1][-1]


if __name__ == '__main__':
    main()

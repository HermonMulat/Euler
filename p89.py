import sys
TRANS = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
BACK = {1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",
        100:"C",400:"CD",500:"D",900:"CM",1000:"M"}

def minCoins(n,coins,coin_weight):

    a = [0]*(n+1)
    used = [0]*(n+1)

    for i in range(1,n+1):
        total_coin = i # worst case we use only one's
        last_used_coin = 0
        for j in range(0,len(coins)):
            if coins[j] <= i:
                current = (a[i-coins[j]] + coin_weight[j])
                if  total_coin > current :
                    total_coin = current
                    last_used_coin = j

        a[i] = total_coin
        used[i] = last_used_coin
    return a,used

def getDeci(roman):
    deci = [TRANS[i] for i in roman.upper()]+[0]
    final_deci = 0
    i = 0
    while i+1<len(deci):

        if deci[i]<deci[i+1]:
            final_deci +=(deci[i+1] - deci[i])
            i +=2
        else:
            final_deci += deci[i]
            i +=1
    return final_deci


def recover(val,u):
    coins = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    temp = 0
    coins_used = []
    while (val!=0):
        temp = u[val]
        coins_used.append(coins[temp])
        val = val - coins[temp]
    coins_used.sort()
    roman = [BACK[i] for i in reversed(coins_used)]
    return "".join(roman)



def main():
    coins = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    coin_weight = [1,2,1,2,1,2,1,2,1,2,1,2,1]
    file_name = sys.argv[1]

    romans = []
    deci = []
    max_val = 0
    with open(file_name,"r") as inf:
        for line in inf:
            line = line.strip()
            if line != "":
                romans.append(line)
                deci_rep = getDeci(line)
                deci.append(deci_rep)
                if max_val < deci_rep:
                    max_val = deci_rep

    min_weights,u = minCoins(max_val,coins,coin_weight)

    total_saved = 0
    f = open("solution.txt","w")
    txt = "Decimal".center(10," ")
    txt += "Roman".center(20," ")
    txt += "Alternative".center(15," ")
    txt += "\t"+"Saved Characters\n"
    f.write(txt)
    for rome,dec in zip(romans,deci):
        total_saved += (len(rome)- min_weights[dec])
        txt = str(dec).center(10," ")
        txt += rome.center(20," ")
        txt += recover(dec,u).center(15," ")
        txt += "\t"+str(len(rome)- min_weights[dec])+"\n"
        f.write(txt)
    print (total_saved)



if __name__ == '__main__':
    import time
    start = time.time()
    main()
    print ("Total time taken:",time.time() - start, "seconds")

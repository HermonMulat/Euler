import sys,time,math,bisect

def tri(n):
    return n*(n+1)//2

def pent(n):
    return n*(3*n-1)//2

def hexa(n):
    return n*(2*n-1)

def hept(n):
    return n*(5*n-3)//2

def octa(n):
    return n*(3*n-2)

def extend_chain(info,chain, complete_set):
    if len(chain) == 6:
        return chain[0]//100 == chain[-1]%100

    last2 = chain[-1]%100
    for i in range(len(complete_set)):
        if i not in info:
            index1 = bisect.bisect_left(complete_set[i],last2*100)
            index2 = bisect.bisect_left(complete_set[i],last2*100 + 99)
            poss_exten = complete_set[i][index1-1:index2+1]
            for ex in poss_exten:
                if last2 == ex//100:
                    chain.append(ex)
                    info.append(i)
                    if extend_chain(info,chain,complete_set):
                        return True
                    else:
                        del chain[-1] # backtrack
                        del info[-1]  # backtrack
    return False



def main():
    # got this range manually
    tris = [tri(i) for i in range(45,141)]
    squares = [i*i for i in range(32,100)]
    pentas = [pent(i) for i in range(26,82)]
    hexas = [hexa(i) for i in range(28,71)]
    heptas = [hept(i) for i in range(21,64)]
    octas = [octa(i) for i in range(19,59)]

    complete_set = [squares,pentas,hexas,heptas,octas]

    # creating the 6-cycle chain
    chain_list = []
    for j in tris:
        chain = []
        chain.append(j)
        info = []
        if extend_chain(info,chain,complete_set):
            break


    print (chain,sum(chain),sep="\nTotal sum is ")

if __name__ == '__main__':
    start = time.time()
    main()
    print ("Total time taken:",time.time()-start)

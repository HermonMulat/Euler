from support import *
def is_palinum(n):
    num_str=[]
    for i in str(n):
        num_str.append(i)
    num_str.reverse()
    num = int(''.join(num_str))
    return num==n

def find_3x3_pali():
    a_list=[]
    j=999
    while (j>=100):
        i=999    
        while (i>=100):
            num=j*i
            #print (num,'=',i,j, is_palinum(num))
            if is_palinum(num):
                a_list.append(num)
            i -=1
            
        j -=1
    return max(a_list)
print (find_3x3_pali())

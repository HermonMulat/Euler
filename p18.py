from support import *
import random
TRI=[]
#read file and save it as a 2D list
with open("triangel_for_18.txt","r")as in_file:
    for line in in_file:
        a=[]
        b=(line.strip()).split(' ')
        for i in b:
            a.append(int(i))
        TRI.append(a)
def inverse(a_list=TRI):
    TRI_INVERSE=[]
    for i in a_list:
        a=[]
        for j in i:
           a.append(max(i)-j)
        TRI_INVERSE.append(a)

    return TRI_INVERSE

def up_side_down(a_list):
    up_side=[]
    for i in range (len(a_list)):
        up_side.append(a_list[len(a_list)-1-i])
    return up_side

def the_rest(full,choice):
    #choice should always be either 0 or 1
    truncated=[]
    if choice==0:
        for i in full[1:]:
            truncated.append(i[:-1])
    else:
        for i in full[1:]:
            truncated.append(i[1:])

    return truncated


def silly_max_path(a_list):
    """
    I know this won't work - but what the hell...
    """
    total=0
    step=0
    current_index=0
    for i in a_list:

        if len(i)==1:
            total+=i[0]
            current_index=0
        else:
            total+=max(i[current_index],i[current_index+1])
            current_index=i.index(max(i[current_index],i[current_index+1]))
    return total

def max_path(a_list):
        if len(a_list)==2:
            return (a_list[0][0])+max(a_list[1])
        else:

            a=(a_list[0][0]+max_path(the_rest(a_list,0)))
            b=(a_list[0][0]+max_path(the_rest(a_list,1)))

            return(max(a,b))

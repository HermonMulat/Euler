from support import *
NAMES=[]
with open("names.txt","r")as in_file:
    for line in in_file:
        n=line.split(',')
        for i in n:
            NAMES.append(i.strip("\""))
NAMES=sorted(NAMES)
print((NAMES[-1]))
ALPHABET={}
av=1
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    ALPHABET[i]=av
    av+=1
def alp_value(name):
    value=0
    for i in name:
        value+=ALPHABET[i]

    return value
def name_score(name_list=NAMES):
    total=0
    for i in range(len(name_list)):
        total+=alp_value(name_list[i])*(i+1)
    return total
        
    

        

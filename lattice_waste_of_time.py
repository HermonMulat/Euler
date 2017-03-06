from random import  randint
from support import *


def path(l,r):
    
    """
    Warning: This is the most inefficient algorithim that generates the all paths
             for lxr (l units down and r units right)grid to reach from left-top
             corner to the right-bottom corner by going only DOWN (represented
             by 'L') and RIGHT('R')

    CONTINUE IF  YOU ACCEPT THE WASTEFULL ALLOCATION OF
    YOUR MACHINE'S RESOURCES!!!
    """
    right="R"
    left="L"
    possible_path=[]
    total_path=comb(l+r,r)
    while len(possible_path)!=total_path:
        path=''
        moves=0
        while moves!=(l+r):
            choice= randint(0,1)
            if (choice==1):
                path += right
            else:
                path += left
            moves += 1
            
        if (not(path in possible_path)) and (path.count("R")==r):
            
            possible_path.append(path)

    return possible_path                           

                
            
    
    
        



from support import *
from grid_20x20 import *

GRID_20x20=get_grid()

def max_four_num_prod():
    product=1
    
    for i in range(20):
        for j in range(20):
            
            #horizontal
            if j+3 <20:
                prod1=GRID_20x20[i][j]*GRID_20x20[i][j+1]*GRID_20x20[i][j+2]*GRID_20x20[i][j+3]
            else:
                prod1=0
                
            #Vertical
            if i+3 < 20:
                prod2=GRID_20x20[i][j]*GRID_20x20[i+1][j]*GRID_20x20[i+2][j]*GRID_20x20[i+3][j]
            else:
                prod2=0
                
            #diagonal_right
            if i+3 < 20 and j+3<20:
                prod3=GRID_20x20[i][j]*GRID_20x20[i+1][j+1]*GRID_20x20[i+2][j+2]*GRID_20x20[i+3][j+3]
            else:
                prod3=0
                
            #diagonal_left
            if i+3 < 20 and j-3>=0:
                prod4=GRID_20x20[i][j]*GRID_20x20[i+1][j-1]*GRID_20x20[i+2][j-2]*GRID_20x20[i+3][j-3]
            else:
                prod4=0

            if max(prod1,prod2,prod3,prod4)>product:
                product=max(prod1,prod2,prod3,prod4)
            
    return product
                

     
            
            
            
        
            


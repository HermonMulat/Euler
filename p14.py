def collatz_sequence(num):
    n=num
    seq=[n]
    while (True):
        if n%2 == 0:
            n=n/2
        else:
            n=3*n+1
            
        seq.append(int(n))
        if n==1:
            break
    return (seq)

def count_collatz_sequence(num):
    n=num
    seq=0
    while (True):
        if n%2 == 0:
            n=n/2
        else:
            n=3*n+1
            
        seq+=1
        if n==1:
            break
    return (seq)

    


    
def longest_collatz_under(n=1000000):
    num=1
    len_of_num=1
    the_list=list(range(int(n/2),n))
    '''collatzs=[]
    c_of_i=[]
    step=0'''

    
    while len(the_list)!=0:
        
        i=the_list[-1]
        the_list.remove(i)
        '''collatzs+=c_of_i
        if not(i in collatzs):
            c_of_i=collatz_sequence(i)
            step+=1
        else:
            c_of_i=[]'''
        c_of_i=collatz_sequence(i)
        
        if len(c_of_i)>=len_of_num:
            num=i
            len_of_num=len(c_of_i)
            
        i=i+1
        
    #print (step,"steps")
    return num

def longest_collatz_under_2(n=1000000):
    num=1
    len_of_num=1
    the_list=list(range(int(n/2),n))
    '''collatzs=[]
    c_of_i=[]
    step=0'''

    
    for i in the_list:
             
        if i%2 != 0:
            c_of_i=count_collatz_sequence(i)
            
            if (c_of_i)>=len_of_num:
                num=i
                len_of_num=(c_of_i)
            
        
    #print (step,"steps")
    return num


    


        

        
        

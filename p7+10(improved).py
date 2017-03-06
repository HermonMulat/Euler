import math
from support import *
def generate_primes(n):
    #generate nth prime   
    primes=[2,3]
    num = 3
    while (len(primes)<n):
            
        is_prime=True
        if ((num+1)%6 != 0) and ((num+5)%6 != 0):
            is_prime=False
        else:
            for i in primes:
                if (i>math.sqrt(num)):
                    break
                elif (num%i == 0):
                    is_prime=False
                    break
        if is_prime:
            primes.append(num)
        num+=2
        
    return primes

def generate_primes_2(m):
    #generate list of primes less that m   
    primes=[2,3]
    num = 3
    while ((primes[-1]<m)):
            
        is_prime=True
        if ((num+1)%6 != 0) and ((num+5)%6 != 0):
            is_prime=False
        else:
            for i in primes:
                if (i>math.sqrt(num)):
                    break
                elif (num%i == 0):
                    is_prime=False
                    break
        if is_prime :
            primes.append(num)
        num+=2
        
    return primes[:-1]
    
        
        
            
        
 
        
        
            
        

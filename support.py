import math

def all_the_sums(a_list):
    sums=[]
    for i in a_list:
        for j in a_list:
            if not((i+j)in sums):
                sums.append(i+j)
    return sums


def fact(n):
    if n==0 or n==1:
        return 1
    product=1
    for i in range (1,n+1):
        product*=i
    return product

def comb(n,m):
    return (fact(n)/(fact(m)*fact(n-m)))

def add_list(a_list):
    # adds the elements in a given list
    total=0
    for i in a_list:
        total +=i
    return total

def get_even(a_list):
    # gets the even numbers from a list
    even=[]
    for i in a_list:
        if ((i%2) == 0):
            even.append(i)

    return even

def is_prime(n):
    # checks if a number is a prime
    for i in range(2,n):
        if ((n%i)== 0):
            return False
    return True
def factors_of(n):
    #factorizes a given number (returns a list that contains all the factors)
    first_half=[]
    second_half=[]
    if n==1:
        return [1]

    for i in range (1,int(math.sqrt(n))):
        if (n%i == 0):
            l = n//i
            first_half.append(i)
            second_half.append(l)

    return sorted( list(set(first_half+second_half)))

def divisors_half(n):
    #factorizes a given number (returns a list that contains all the factors)
    first_half=[]
    if n==1:
        return [1]

    for i in range (2,int(math.sqrt(n))+1):
        if (n%i == 0):
            first_half.append(i)

    return first_half


def prime_factorize(n):
    #get prime factorization of a number
    k=0
    i=2
    p=0
    prime_fact={}
    num=n
    while (i<=num):
        if (num%i == 0):

            num=num//i
            p+=1

        else:
            if (p!=0):
                prime_fact[i] = p
            i+= 1
            p=0

        if (num==1)and (p!=0):
            prime_fact[i]=p
        k += 1
    '''print (k,"steps")'''
    return prime_fact

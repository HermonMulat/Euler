from support import *
def feb_seq(n):
    
    a_list=[1,2]
    m=3
    while m<n:
        length=len(a_list)
        m=a_list[length-1]+ a_list[length-2]
        a_list.append(m)

    a_list.pop()
    return a_list

even_from_feb = get_even(feb_seq(4000000))
print (add_list(even_from_feb))

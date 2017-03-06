NUM_TO_WORD={0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',
             8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',
             14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',
             19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',
             70:'seventy',80:'eighty',90:'ninety',100:'hundred',1000:'thousand'}
def num_word(n):
    n=str(n)
    power=(len(n)-1)
    word=''
    if int(n) in NUM_TO_WORD:
        return NUM_TO_WORD[int(n)]
    
    i=n[0]
    if power!=1 and (int(i)!=0):
        word += NUM_TO_WORD[int(i)]
        word += NUM_TO_WORD[int(10**power)]
    elif(int(i)!=0):
        word += NUM_TO_WORD[int(i)*int(10**power)]

        
    return word+num_word(n[1:])

def british_stand_word(n):
    # NOTE : 100 and 1000 will only be translated as hundred and thousand
    #so I will have to add 3 for each at the end(add 6)
    word=num_word(n)
    power=(len(str(n))-1)
    if power >1 and (str(n)[-2:]!='00'):
        word+='and'
    return(word)
def num_letter_count(n=1000):
    num=list(range(1,n+1))
    count=0
    for i in num:
        word=british_stand_word(i)
        count+=len(word)
        
    return count

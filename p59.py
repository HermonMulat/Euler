import time,sys
from operator import xor

FREQ = [8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,0.772,
        4.025,2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.056,2.758,0.978,
        2.360,0.150,1.974,0.074]

def translate(code_seq):
    return "".join([chr(int(i)) for i in code_seq])

def freq_diff(seq,i):
    plain = translate([xor(ord(i),j) for j in seq])
    seq_freq = [0]*26
    for i in plain.lower():
        if 97<=ord(i)<=122:
            seq_freq[ord(i)-97] += 1
    total = len(plain)
    seq_freq = [i*100/total for i in seq_freq]
    diff = 0
    for i,j in zip(seq_freq,FREQ):
        diff += abs(i-j)

    return plain,diff

def main():
    f = open(sys.argv[1],"r")
    code = f.readline().split(",")
    partitioned = [[],[],[]]
    for i in range(len(code)):
        partitioned[i%3].append(int(code[i]))

    p1,p2,p3 = partitioned
    keys = [1,1,1]
    plains = [1,1,1]
    for part in range(3):
        min_diff = 100
        p = partitioned[part]
        for key in "abcdefghijklmnopqrstuvwxyz":
            plain,diff = freq_diff(p,key)
            if min_diff > diff:
                min_diff = diff
                keys[part] = key
                plains[part] = (plain)

    print ("The Key is \'"+"".join(keys)+"\'")
    final_txt = ""
    max_length = max([len(i) for i in plains])
    s1 = len(plains[0])
    s2 = len(plains[1])
    s3 = len(plains[2])
    for i in range(max_length):
        if i < s1:
            final_txt += plains[0][i]
        if i < s2:
            final_txt += plains[1][i]
        if i < s3:
            final_txt += plains[2][i]

    print ("\nFinal text is:\n")
    print(final_txt)
    total_val =sum([ord(i) for i in final_txt])
    print ("\nSum of ASCII:",total_val)


if __name__ == '__main__':
    start = time.time()
    main()
    print ("Total time taken:",time.time()-start,"seconds")

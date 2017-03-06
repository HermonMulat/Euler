def replace(num,i):
    num = list(num)
    avg = (int(num[i]) + int(num[i+1]) + 1) // 2 # rounded up
    new_num = num[:i] + [str(avg)] + num[i+2:]
    return int("".join(new_num))

def solution(n):
    num = list(str(n))
    max_repl = 0
    for i in range(len(num)-1):
        val = replace(num,i)
        if max_repl < val:
            max_repl = val
    return max_repl

def main():
    print solution(623315)
if __name__ == '__main__':
    main()

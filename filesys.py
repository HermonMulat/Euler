
def solution(s):
    s = s.split("\n")

    currDir = ["/"]
    max_size  = 0
    ans = 0
    for line in s:
        file_name = line.strip()
        depth = (len(line) - len(file_name)) - len(currDir) + 1
        if depth <= 0:
            currDir = currDir[:depth-1]
        currDir.append(file_name)

        if file_name.split(".")[-1] in ["jpeg","png","gif"]: #found picture
            length = len("/".join(currDir))
            if max_size < length:
                max_size = length
                ans = len("/".join(currDir[:-1]))+1
    return ans

if __name__ == '__main__':
    s="dir1\n dir11\n dir12\n  picture.jpeg\n  dir121\n  file1.txt\ndir2\n file2.gif"
    print solution(s)

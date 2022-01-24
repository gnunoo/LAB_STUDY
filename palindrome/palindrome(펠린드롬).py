def solution(d):

    d = ''.join(filter(str.isalnum, d))
    d=d.lower()
    d1=d[0:int(len(d)/2)]
    d2=d[int(len(d)/2)+1:]
    d2=''.join(reversed(d2))
    print(d1,d2)
    if d1==d2:
        return True
    else:
        return False


def main():
    d=input()
    a=solution(d)
    print(a)


if __name__=="__main__":
    main()

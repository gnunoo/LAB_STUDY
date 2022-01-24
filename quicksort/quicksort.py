def quickSort(quickArr):
    if len(quickArr)<=1:
        return quickArr
    pivot=quickArr[0]

    small,equal,big=[],[],[]
    for num in quickArr:
        if num < pivot:
            small.append(num)
        elif num > pivot:
            big.append(num)
        else:
            equal.append(num)
    return quickSort(small) + equal + quickSort(big)

def main():
    quickArr=list(map(int,input().split()))
    print("정렬 전")
    print(quickArr)
    quickArr=quickSort(quickArr)
    print("결과:")
    print(quickArr)

if __name__ == "__main__":
    main()

#https://www.daleseo.com/sort-quick/  참고블로그

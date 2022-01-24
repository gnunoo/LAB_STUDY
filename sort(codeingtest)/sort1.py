def solution(array, commands):
    answer =[]
    #commands의 세로 길이
    Len=len(commands)

    for i in range(Len):
        first=commands[i][0]-1
        end=commands[i][1]
        answer.append(array[first:end])
    bubbleSort(answer)
    print(answer)
    for i in range(len(answer)):
        cheak = commands[i][2] - 1
        del answer[i][:cheak]
        del answer[i][1:]
    return answer
#버블정렬
def bubbleSort(answer):
    for k in range(len(answer)):
        for i in range(len(answer[k]) - 1, 0, -1):
            for j in range(0, i):
                if (answer[k][j] > answer[k][j + 1]):
                    answer[k][j], answer[k][j + 1] = answer[k][j + 1], answer[k][j]
def main():
    answer=[]
    array=[1,5,2,6,3,7,4]
    commands=[list(map(int,input().split())) for cow in range(3)]
    answer=solution(array, commands)
    print(answer)



if __name__=="__main__":
    main()

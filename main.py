class Queue:
    def __init__(self):
        self.myQueue = []
        self.front = -1 # 끝
        self.rear = -1 # 시작
    # 끝과 시작이 같은 위치에 있으면 데이터가 비어 있음

    def isEmpty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    # 시작이 큐의 길이를 넘어가면 데이터가 가득 차 있음
    def isFull(self):
        if self.rear > len(self.myQueue):
            return True
        else:
            return False

    # 데이터 삽입
    def pushQueue(self,data):

        if not self.isFull():
            for i in range(len(data)):
                self.rear = self.rear + 1
                self.myQueue.append(data[i])

    # 데이터 삭제
    def popQueue(self):
        if not self.isEmpty():
            temp = self.myQueue[0]
            del self.myQueue[0]
            self.rear = self.rear - 1
            print("remove: %s" % temp)
            return temp

    # 데이터 출력
    def printQueue(self):
        print(self.myQueue)

    def menu(self):
        while True:
            print('''
            1.pushQueue
            2.popQueue
            3.printQueue
            4.quit
            ''')
            a = int(input(">> 번호를 입력해주세요 "))
            if a == 1:
                data = list(input().split())
                self.pushQueue(data)
            elif a == 2:
                self.popQueue()
            elif a == 3:
                self.printQueue()
            else:
                print("end............")
                break

    def __del__(self):
        print(" 객체가 소멸합니다.")






class Stack:
    def __init__(self):
        self.my_stack = []
        self.top = -1  # 비어 있는 상태를 뜻 한다.
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    # 스택이 가득 차 있으면 True 반환
    def isFull(self):

        if self.top > len(self.my_stack) - 1:
            return True
        else:
            return False

    # 데이터가 가득 차 있지 않으면 데이터 삽입
    def mypush(self,data):
        if not self.isFull():
            for i in range(len(data)):
                self.top = self.top + 1
                self.my_stack.append(data[i])

    # 데이터가 비어 있지 않으면 데이터 삭제하고 반환
    def mypop(self):
        if not self.isEmpty():
            temp = self.my_stack[self.top]
            del self.my_stack[self.top]
            self.top = self.top - 1
            print("remove %s:" % temp)
            return temp

    # 데이터가 비어 있지 않으면 데이터 반환
    def mypeek(self):
        if not self.isEmpty():
            temp = self.my_stack[self.top]
            return temp

    # 출력
    def printStack(self):
        print(self.my_stack)

    def menu(self):
        while True:
            print('''
            1.push
            2.pop
            3.printStack
            4.quit
            ''')
            a = int(input(">> 번호를 입력해주세요 "))
            if a == 1:
                data = list(input().split())
                self.mypush(data)
            elif a == 2:
                self.mypop()
            elif a == 3:
                self.printStack()
            else:
                print("end............")
                break

    def __del__(self):
        print(" 객체가 소멸합니다.")


def Main_menu():
    while True:
        print('''
         1. 큐
         2. 스택
         3. 종료
         ''')
        a=int(input("선택하세요: "))

        if a==1:
            b = Queue()
            b.menu()
        elif a==2:
             c=Stack()
             c.menu()
        else:
            print("end...........")
            break


def main():
    Main_menu()

if __name__ == "__main__":
    main()
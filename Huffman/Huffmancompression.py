from queue import PriorityQueue

class HuffNode:

    def __init__ (self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None

    def __eq__(self, other):
        return self.freq == other.freq
    def __ne__(self, other):
        return self.freq != other.freq


    def preorder(self):
        print(self.freq,end=" ")
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    def makedig(self,dig="",arrdig=[],arrsymbol=[]):
        arrdig=arrdig
        dig=dig
        arrsymbol=arrsymbol
        arrsymbol.append(self.symbol)

        if self.left is not None:
            dig=dig+"0"
            arrdig.append(dig)
            self.left.makedig(dig,arrdig,arrsymbol)

        if self.right is not None:
            dig=list(dig)
            del dig[len(dig)-1]
            dig="".join(dig)
            dig=dig+"1"
            arrdig.append(dig)
            self.right.makedig(dig,arrdig,arrsymbol)

        return arrdig,arrsymbol
#버블 정렬 정렬하는데 빈도수를 내림차순으로 정렬하고 빈도수에 해당하는 문자도 정렬
def buble_sort(code,count):
    for i in range(len(count)):
        for j in range(len(count) - 1):
            if count[j] > count[j + 1]:
                count[j], count[j + 1] = count[j + 1], count[j]
                code[j], code[j + 1] = code[j + 1], code[j]
    return code,count
#허프만 알고리즘
def huffman (n, PQ):

    for _ in range(n - 1):
        p = PQ.get()[1]
        q = PQ.get()[1]
        r = HuffNode(' ', p.freq + q.freq)

        r.left = p
        r.right = q
        PQ.put((r.freq, r))

    return PQ.get()[1]
#파일에서 데이터 가져오기
def fileDataGet():

    with open("compression.txt","r") as f:
        #파일에서 데이터 가져오기
        data=f.read()
        code=[chr(i) for i in range(0,127) if chr(i) in data]
        count=[data.count(chr(i)) for i in range(0,127) if chr(i) in data]
        # 공백을 -1로 처리
        for i in range(len(code)):
            if code[i]==' ':
                code[i]=-1

    return code,count,data
 #우선순위 큐
def myQueue(codes,freqs):


    PQ = PriorityQueue()
    for i in range(len(codes)):
        node = HuffNode(codes[i], freqs[i])

        PQ.put((node.freq, node))

    root = huffman(len(codes), PQ)
    return root
def showdata(data1, data2):
    print(data1)
    print(data2)
    print()
def encoding(data,ecoding_data):
    data = list(data)
    for i in range(len(data)):
        for key, value in ecoding_data.items():
            if data[i] == key:
                data[i] = value
            elif data[i] == ' ':
                data[i] = ecoding_data[-1]
    return data
def main():
    codes,freqs,data=fileDataGet()
    print("정렬전:")
    showdata(codes,freqs)
    # 버블 정렬
    code,count=buble_sort(codes,freqs)
    print("정렬후:")
    showdata(codes,freqs)
    #우선순위 큐를 이용하기
    root=myQueue(codes,freqs)
    #트리 순회
    print("트리 순회 결과:")
    root.preorder()
    print()
    #만든 비트 가져오기
    arrdig,arrsymbol=root.makedig()
    del arrsymbol[0]

    # 알파벳:빈도수 이런식으로 딕셔너리 만들기
    ecoding_data=dict(zip(arrsymbol,arrdig))
    ecoding_data=dict({key:value for key,value in ecoding_data.items() if key != ' '})
    print("\n문자: 압축비트")
    for key,value in ecoding_data.items():
        print(key,value,sep=': ')
    #인코딩
    data=''.join(encoding(data,ecoding_data))
    print("\n압축 후:",end=" ")
    print(data)

if __name__=='__main__':
    main()
 
 
 #참고-https://www.youtube.com/watch?v=IDxnHM01fZY

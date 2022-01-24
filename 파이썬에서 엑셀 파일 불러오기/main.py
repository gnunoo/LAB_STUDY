import csv

with open('finalpart1.csv', 'r') as f:
    reader=csv.reader(f)

    cnt=0
    sum=0
    for n in reader:
        #print(n)
        if cnt%3==0 and n[cnt] != '':
            print(n[cnt+1])
        elif n[cnt]=='' and n[cnt+2].isdigit():
            sum=sum+int(n[cnt+2])
    print(sum)

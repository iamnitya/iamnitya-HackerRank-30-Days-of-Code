# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
dic = {}
for i in range(n):
    name, number = input().split(" ")
    dic[name]=number
while True:
    try:
        j = input()
        v = list(dic.keys())
        if j in v:
            print(j+"="+dic[j])
        else:
            print("Not found")
    except EOFError:
        break

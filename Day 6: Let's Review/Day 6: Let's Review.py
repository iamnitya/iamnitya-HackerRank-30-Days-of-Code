# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())
for a in range(N):
    S = input()
    k=""
    j=""
    for i in range(len(S)):
        if i%2==0:
            k=k+S[i]
        else:
            j=j+S[i]
    print(k,j)

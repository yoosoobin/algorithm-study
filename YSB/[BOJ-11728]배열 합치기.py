m,n = input().split()

fir  = list(map(int,input().split()))
sec  = list(map(int,input().split()))

ans = sorted(fir+sec)
for i in ans:
    print(i,end=' ')
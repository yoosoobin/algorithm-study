import sys
input = sys.stdin.readline

n,s = map(int,input().split())
cow_size = []
ans = 0
for _ in range(n):
    cow_size.append(int(input()))

a_pt = 0
b_pt = 0

while a_pt <=n-1:
    if a_pt == b_pt:
        b_pt +=1
    elif b_pt == n:
        a_pt+=1
        b_pt=a_pt
    elif cow_size[a_pt]+cow_size[b_pt]<=s:
        ans+=1
        b_pt+=1
    else:
        b_pt+=1

print(ans)

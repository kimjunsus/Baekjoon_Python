# 백준 10871번

a,b = map(int, input().split())
c = list(map(int,input().split()))

for i in c:
    if i < b:
        print(i, end=' ')
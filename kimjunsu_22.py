# 백준 11021번

a = int(input())

for i in range(1, a+1):
    b , c =map(int, input().split())
    d = b + c
    print("Case #{}:".format(i), d)
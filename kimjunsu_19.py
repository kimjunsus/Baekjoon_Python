# 백준 25304번
x = int(input())
a = int(input())
sum = 0
for i in range(a):
    b, c = map(int, input().split()) 
    sum += (b * c)
    if x == sum:
        print("Yes")
    else:
        print("No")
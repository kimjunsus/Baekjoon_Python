# 백준 25304번

x = int(input("총 금액:"))
n = int(input("구매 항목의 개수"))

sum = 0
for i in range(n):
    c, d = map(int, input(). split())
    sum += c * d

if sum == x:
    print("yes")
else:
    print("no")
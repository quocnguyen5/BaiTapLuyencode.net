def TinhGiaiThua(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    print(result)

n = int(input())
L = [int(x) for x in input().split()]
for i in L:
    TinhGiaiThua(i)
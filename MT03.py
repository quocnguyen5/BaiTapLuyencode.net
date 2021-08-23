n = int(input())
L = [int(x) for x in input().split()]
tong = 0

for i in range(0, len(L), n+1):
    tong += L[i]
print(tong)

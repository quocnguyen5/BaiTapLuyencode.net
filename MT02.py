m, n = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]
tong = 0
for i in range(1, len(L), 3):
    print(i)
    if L[i] % 2 != 0:
        tong += L[i - 1] + L[i] + L[i + 1]
print(tong)

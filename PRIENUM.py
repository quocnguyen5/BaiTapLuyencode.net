n = int(input())
L = [int(x) for x in input().split()]
L2 = list(set(L))
Tong = 0
kq = []
for i in L2:
    x = L.count(i)
    if x > 1:
        Tong += x
print(Tong)

a, b = [int(x) for x in input().split()]

if a % 2 == 0:
    a = a + 1
if b % 2 == 0:
    b = b - 1

SoHang = ((b - a) / 2) + 1
TongLe = ((b + a) * SoHang) / 2

print(int(TongLe))

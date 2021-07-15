TONG = 0
SNL = 0

n = int(input())
A = [int(x) for x in input().split()]
for i in A:
    if i % 2 != 0:
        SNL += 1
        TONG += i

if SNL == 0:
    print(0)
else:
    TBC = TONG / SNL
    print("{:.4f}".format(TBC))

n = int(input())
A = [int(x) for x in input().split()]

LAm = []
LDuong = []

for i in A:
    if i < 0:
        LAm.append(i)
    elif i > 0:
        LDuong.append(i)

print(len(LAm),end=' ')
print(len(LDuong))
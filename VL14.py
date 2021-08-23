a, b = [int(x) for x in input().split()]
a = abs(a)
b = abs(b)
UocSoA = []
UocSoB = []
UocChung = []
for i in range(1, a+1):
    if a % i == 0:
        UocSoA.append(i)

for i in range(1, b+1):
    if b % i == 0:
        UocSoB.append(i)
if UocSoB == [] or UocSoA == []:
    UocChung = UocSoA + UocSoB
    print(max(UocChung))
else:
    for i in UocSoA:
        for j in UocSoB:
            if i == j:
                UocChung.append(i)
    print(max(UocChung))

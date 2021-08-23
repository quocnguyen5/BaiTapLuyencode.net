a, b = [int(x) for x in input().split()]
x = y = 0
UocSoA = []
UocSoB = []
UocChung = []
if b == 0:
    print("INVALID")
elif a == 0:
    print(0)
else:
    x = abs(a)
    y = abs(b)
    for i in range(1, x + 1):
        if x % i == 0:
            UocSoA.append(i)

    for i in range(1, y + 1):
        if y % i == 0:
            UocSoB.append(i)
    if UocSoB == [] or UocSoA == []:
        UocChung = UocSoA + UocSoB
        print(max(UocChung))
    else:
        for i in UocSoA:
            for j in UocSoB:
                if i == j:
                    UocChung.append(i)

    tu = a / max(UocChung)
    mau = b / max(UocChung)

    if mau < 0:
        tu = -tu
        mau = abs(mau)
    if mau == 1:
        print(int(tu))
    else:
        print(int(tu), int(mau), sep=" ")

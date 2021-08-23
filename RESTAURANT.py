def CanhHinhVuong(a, b):
    a = abs(a)
    b = abs(b)
    UocSoA = []
    UocSoB = []
    CanhHinhVuong = []
    for i in range(1, a + 1):
        if a % i == 0:
            UocSoA.append(i)

    for i in range(1, b + 1):
        if b % i == 0:
            UocSoB.append(i)
    if UocSoB == [] or UocSoA == []:
        CanhHinhVuong = UocSoA + UocSoB
        return max(CanhHinhVuong)
    else:
        for i in UocSoA:
            for j in UocSoB:
                if i == j:
                    CanhHinhVuong.append(i)
        return max(CanhHinhVuong)


n = int(input())
kq = []

for i in range(n):
    a, b = [int(x) for x in input().split()]
    n = CanhHinhVuong(a, b)
    kq.append(int((a * b) / (n * n)))

for i in kq:
    print(i)
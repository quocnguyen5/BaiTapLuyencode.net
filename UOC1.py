a, b = [int(x) for x in input().split()]


def TimUocSo(n):
    UocSo = []
    if n == 0:
        UocSo = []
    else:
        for i in range(1, n + 1):
            if n % i == 0:
                UocSo.append(i)
    return UocSo


UocA = TimUocSo(a)
UocB = TimUocSo(b)
Lkq = []
for i in UocA:
    if i not in UocB:
        Lkq.append(i)
print(sum(Lkq))

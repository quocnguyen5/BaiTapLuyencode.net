n = int(input())
n = abs(n)
UocSo = []
if n ==0:
    print('INF')
else:
    for i in range(1, n+1):
        if n % i == 0:
            UocSo.append(i)
    UocSo.sort(reverse=True)

    for i in UocSo:
        print(i, end=' ')


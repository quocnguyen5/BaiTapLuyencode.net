n = int(input())
tong = 0
if n <= 0:
    print('NO')
else:
    for i in range(1, n,1):
        if n % i == 0:
            tong += i
    if tong == n:
        print('YES')
    else:
        print('NO')

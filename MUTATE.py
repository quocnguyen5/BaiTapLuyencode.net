n = int(input())
if 1 <= n <= 10 ** 6:
    print(n, end=" ")
    while True:
        if n == 1:
            break
        if n % 2 == 0:
            n = n / 2
            print(int(n), end=" ")
        else:
            n = n * 3 + 1
            print(int(n), end=" ")
        if n == 1:
            break

n, k = [int(x) for x in input().split()]


def ToHop(n, k):
    ketqua = 1
    if k == 0 or k == n:
        return 1
    elif k == 1 or n - k == 1:
        return n
    elif n == 0 or n == 1:
        ketqua = n*(n-1)
    elif n > k:

        if k >= n-k:
            x = n - k
            giaithuaX = 1
            for i in range(1, x+2):
                giaithuaX *= i
            for i in range(k, n+1):
                ketqua *= i
            print('th1',ketqua)
            return (ketqua/giaithuaX)
        elif k < n-k:
            x = k
            for i in range(1, x+1):
                giaithuaX *= i
            for i in range(n-k, n+1):
                ketqua *= i
            print('th2',ketqua)
            return (ketqua/giaithuaX)



ketqua = ToHop(n, k)
print(ketqua

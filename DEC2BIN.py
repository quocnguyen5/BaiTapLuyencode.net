T = int(input())
if 1 <= T <= pow(10,5):
    kq = []


    def DEC2BIN(n):
        k = ""
        L = []
        while n != 0:
            x = n % 2
            L.append(x)
            n = n // 2
        L.reverse()
        for i in L:
            k += str(i)
        return int(k)

    for i in range(1, T + 1):
        n = int(input())
        
        kq.append(DEC2BIN(n))

    for i in kq:
        print(i)

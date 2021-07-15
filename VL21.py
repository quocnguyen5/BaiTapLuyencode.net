n = int(input())
if n > 0:
    if n == 2:
        print(1)
    elif n == 1:
        print(0)

    def timi(n):
        x = 0
        for i in range(1, n):
            x += i
            if x > n:
                return i-1
print(timi(n))



n = int(input())

def timi(n):
    x = 0
    for i in range(1, n):
        x += i
        if x > n:
            return i-1
print(timi(n))
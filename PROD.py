a, b = [int(x) for x in input().split()]
if a * b < 0:
    print(-1)
elif a * b > 0:
    print(1)
else:
    print(0)

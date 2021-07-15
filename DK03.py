a, b = [int(x) for x in input().split()]
if abs(a) <= pow(10, 6) and abs(b) <= pow(10, 6):
    print(abs(a-b))


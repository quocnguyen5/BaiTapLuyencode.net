a, b = [int(x) for x in input().split()]

if ord(str(a)) > ord(str(b)):
    print(str(b) * a)
else:
    print(str(a) * b)

m, n = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]
x = 0
for i in L:
    print(i, end=" ")
    x += 1
    if x == n:
        print()
        x = 0

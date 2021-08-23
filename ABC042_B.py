a, b = [int(x) for x in input().split()]
L = []
for i in range(a):
    L.append(input())
L.sort()
for i in L:
    print(i,end='')
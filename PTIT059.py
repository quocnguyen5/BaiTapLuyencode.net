n = int(input())
N = [int(x) for x in input().split()]
x = int(input())

N.append(x)
N.sort()
for i in N:
    print(i, end=" ")

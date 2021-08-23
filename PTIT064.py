n = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

for i in B:
    A.append(i)

A.sort()

for i in A:
    print(i, end=" ")

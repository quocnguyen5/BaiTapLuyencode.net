n = int(input())
A = [int(x) for x in input().split()]
B = A[1 : (n - 1)]
B.sort()

A = [A[0]] + B + [A[n - 1]]

for i in A:
    print(i, end=" ")

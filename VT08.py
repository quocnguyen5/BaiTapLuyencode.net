n = int(input())
A = [int(x) for x in input().split()]
A.append(0)
for i in range(1, n, 2):
    A[i] = A[i] + abs((A[i + 1] - A[i - 1]))

del A[n]
for i in A:
    print(i, end=" ")

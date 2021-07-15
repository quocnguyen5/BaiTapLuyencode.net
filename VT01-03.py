n = int(input())
A = [int(x) for x in input().split()]
if len(A) == n:
    A.reverse()
    max = A[1]
    for x in range(n):
        if A[x] >= max:
            max = A[x]
print(n - (A.index(max)+1))

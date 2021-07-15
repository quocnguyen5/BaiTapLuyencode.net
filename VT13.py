n = int(input())
A = [int(x) for x in input().split()]

max = 0
so1 = 0
so2 = 0
if n % 2 == 1:
    A.append(A[0])
    for i in range(n):
        if A[i] + A[i + 1] > max:
            max = A[i] + A[i + 1]
            so1 = i
            so2 = i + 1
    if so1 == n:
        print(A[so2], A[so1])
    else:
        print(A[so1], A[so2])
else:
    for i in range(n - 1):
        if A[i] + A[i + 1] >= max:
            max = A[i] + A[i + 1]
            so1 = i
            so2 = i + 1
    print(A[so1], A[so2])

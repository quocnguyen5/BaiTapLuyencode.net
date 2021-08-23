n = int(input())
A = [int(x) for x in input().split()]

max = min = A[0]
for i in range(n):
    if A[i] > max:
        max = A[i]
    if A[i] < min:
        min = A[i]

print(max - min)

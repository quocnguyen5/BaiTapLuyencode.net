n = int(input())
A = [int(x) for x in input().split()]
dem = 0

for i in range(n - 1):
    if A[i] == A[i + 1]:
        dem += 1
print(dem)

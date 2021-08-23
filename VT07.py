A = [int(x) for x in input().split()]
x = A.pop(10)
if x in A:
    for i in range(10):
        if A[i] == x:
            print(i+1, end=' ')
else:
    print(-1)
import random

n = int(input())
L = []
A = []
for j in range(n):
    for i in range(n):
        A.append(random.randrange(100))
    L.append(A)
    A = []

print(L)
for i in L:
    for j in range(n):
        print(i[j], end=" ")
    print()

def transpose_and_yield_top(arr):
    while arr:
        yield arr[0]
        arr=list(reversed(zip(*arr[1:])))

print list(itertools.chain(*transpose_and_yield_top(arr)))
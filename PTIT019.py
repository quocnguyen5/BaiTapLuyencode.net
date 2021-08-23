A = [int(x) for x in input().split()]
A.sort(reverse=True)
for i in A:
    print(i, end=" ")

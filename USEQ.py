n = int(input())
A = [int(x) for x in input().split()]
B = set(A)

for i in B:
    if A.count(i) % 2 != 0:
        print(i)
        break

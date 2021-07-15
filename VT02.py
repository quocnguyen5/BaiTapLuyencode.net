n = int(input())
A = [int(x) for x in input().split()]
A2 = []


def SoLonThu2():
    max1 = max2 = A[1]
    for i in range(n):
        if A[i] >= max1:
            x = max1
            max1 = A[i]
            max2 = x
    return max2


for i in A:
    if i not in A2:
        A2.append(i)
if len(A2) == 1:
    print("NOT FOUND")
else:
    max = SoLonThu2()
    print(max)

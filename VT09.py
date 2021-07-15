n = int(input())
A = [int(x) for x in input().split()]


def LaNST(n):
    dem = 0
    for i in range(1, n + 1):
        if n % i == 0:
            dem += 1
    if dem == 2:
        return True
    return False


B = []
for n in A:
    if LaNST(n) and n not in B:
        B.append(n)
B.sort()
for i in B:
    print(i,end=' ')

n = int(input())
L = [int(x) for x in input().split()]
L2 = list(set(L))

max = L.count(L2[0])
imax = L2[0]
for i in L2:
    if L.count(i) > max:
        max = L.count(i)
        imax = i

print(imax, max, end=" ")

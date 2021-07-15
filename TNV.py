n = int(input())
L = [int(x) for x in input().split()]
L2 = list(set(L))
L2.sort(reverse=True)
if len(L2) == len(L):
    print(L2[0])
else:
    L2.sort(reverse=True)
    max = L.count(L2[0])
    imax = L2[0]
    for i in L2:
        if L.count(i) > max:
            max = L.count(i)
            imax = i

        elif L.count(i) == max:
            max = L.count(i)
            if i > imax:
                imax = i

    print(imax, max, end=" ")

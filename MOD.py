n = input()
L = []
kq = []
for i in n:
    L.append(i)
if len(L) >= 3:
    L = L[len(L) - 3 : len(L)]
    for i in L:
        print(i, end="")
elif len(L) == 2:
    print("0", end="")
    for i in L:
        print(int(i), end="")
elif len(L) == 1:
    print("00", end="")
    print(L[0])

import itertools
n = input()
L = []

for char in n:
    L.append(char)

L2 = list(set(itertools.permutations(L)))
L2.sort()
print(len(L2))
for i in L2:
    for j in i:
        print(j,end='')
    print()
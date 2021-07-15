L = []
n = input()

for i in n:
    L.append(i)
L = list(set(L))

print(len(L))
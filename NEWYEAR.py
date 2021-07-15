n = int(input())
L = []
for i in range(n):
    L.append(input())

print(len(list(set(L))))
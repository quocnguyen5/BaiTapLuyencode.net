n = int(input())
L = []
H = []
h = 0
j = 0
for i in range(n):
    L.append(int(input()))

while j <= L[-1]:
    if j == 0:
        h = 1
        H.append(h)
    elif j % 2 != 0:
        h *= 2
        H.append(h)
    elif j % 2 == 0:
        h += 1
        H.append(h)
    j += 1
    if j > L[-1]:
        break

for i in L:
    for j in range(len(H)):
        if i ==j:
            print(H[j])                
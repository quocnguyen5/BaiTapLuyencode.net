n = int(input())
kq = []
for i in range(n):
    x = int(input())
    S = 2 * (1 - 1 / (x + 1))
    kq.append(S)

for i in kq:
    print('{:.8f}'.format(i))
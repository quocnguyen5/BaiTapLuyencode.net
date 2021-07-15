n = int(input())
S = 0
for i in range(0,3*n+2):
    if i % 2 == 0:
        S = S - i
    else:
        S = S + i
print(S)

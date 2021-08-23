n = int(input())
S = 0
if n >= 2:
    for i in range(2, n+1):
        S = S + i
    print(S+2*n)

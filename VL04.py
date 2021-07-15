n = int(input())
S = 0
if 10**4 >= n >= 2:
    for i in range(2, n+1):
        S = S + 1/i
    print(("{:.4f}".format(S)))
else:
    n = int(input())

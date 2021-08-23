x, n = [int(x) for x in input().split()]
S = x
m = 1
for i in range(2, n+1):
    m = m*i
    S = S + (pow(x, i))/m
print('{:.2f}'.format(S))

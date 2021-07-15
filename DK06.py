a, b = [int(x) for x in input().split()]
if a== 0 and b== 0:
    print("INF")
elif a== 0 and b!= 0:
    print('NO')
elif a!= 0 and b== 0:
    print('0.00')
else:
    x = -b/a
    print(round(x,2))
    
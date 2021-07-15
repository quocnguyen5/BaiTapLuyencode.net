import math
a, b = [int(x) for x in input().split()]
if abs(a) <= 100 and abs(b) <= 100:
    print(a+b)
    print(a-b)
    print(a*b)
    
    if b == 0:
        print('INF')
    else:
        print(round(float(a/b),2))
        
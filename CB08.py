import math
a, b = [int(x) for x in input().split()]
if abs(a) <= pow(10,9) and abs(b) <= pow(10,9):
    print(a,'+',b,'=',a+b)
                
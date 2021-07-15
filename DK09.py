
y=int(input())
if 0 < y <=100000:
    if (y % 4 ==0 and y % 100 !=0) or y % 400 ==0:
        print('YES')
    else:
        print('NO')
else: 
    print('INVALID')
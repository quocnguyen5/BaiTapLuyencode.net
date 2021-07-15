# import math
# a, b, c = [int(x) for x in input().split()]
# if -1000 <= a <= 1000 and  -1000 <= b <= 1000 and  -1000 <= c <= 1000:
#     if a == 0:
#         #bx+c=0
#         if b == 0:
#             if c == 0:
#                 print('INF')
#             else:
#                 print('NO')
#         else:
#             if c == 0:
#                 print(0)

#             else:
#                 x = -c/b
#                 print(round(x, 2))


#     else:
#         delta = b**2-4*a*c
#         if delta < 0:
#             print('NO')
#         elif delta == 0:
#             x1 = x2 = -b/(2*a)
#             print(round(x1,2),round(x2))
#         else:
#             x1 = float((-b - math.sqrt(delta))/ (2 * a))
#             x2 = float((-b + math.sqrt(delta))/ (2 * a))
#             max = x1
#             min = x2
#             if x2 > max:
#                 max = x2
#                 min = x1
#             print(round(min, 2), round(max, 2))


import math


def giaiPTBac2(a, b, c):
    # kiểm tra các hệ số
    if a == 0:
        if b == 0:
            if c!=0:
                print('NO')
            else:
                print('INF')
        else:
            print("{:.2f}".format(+(-c / b)))
        return

    # tính delta
    delta = b * b - 4 * a * c
    # tính nghiệm
    if delta > 0:
        x1 = (float)((-b + math.sqrt(delta)) / (2 * a))
        x2 = (float)((-b - math.sqrt(delta)) / (2 * a))
        if x1 > x2:
            print("{:.2f}".format(x2), "{:.2f}".format(x1), end=" ")
    elif delta == 0:
        x1 = -b / (2 * a)
        print("{:.2f}".format(x1))
    else:
        print("NO")


a, b, c = [int(x) for x in input().split()]

giaiPTBac2(a, b, c)

import math

n = int(input())
if 0 <= n <= pow(10, 12):
    if n % 10 in (0, 1, 4, 5, 6, 9):
        if n == 0:
            print("YES")
        else:
            check = False

            for i in range(1, n + 1):
                if i ** 2 == n:
                    check = True
                    break

            if check == True:
                print("YES")
            else:
                print("NO")
    else:
        print("NO")
else:
    print("NO")

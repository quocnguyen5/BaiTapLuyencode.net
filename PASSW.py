
import re

n = int(input())
kq = []

for i in range(n):
    DoAT = 0
    n = input()

    if len(n) >=5:
        return False
    else:
        pass
    if not re.search("[a-z]", n):
        return False

    elif not re.search("[A-Z]", n):
        return False

    elif not re.search("[0-9]", n):




print(KiemTraMatKhau(n))

# n = input()
# import re
# kq = re.findall("\d+",n) #python RegEx: bieu thuc chinh quy. Xem chuoi co chua mau tim kiem duoc chi dinh khong
# print(len(kq))

import re
n = input()
kq = re.findall("[A-Z]+", n)
print(len(kq))

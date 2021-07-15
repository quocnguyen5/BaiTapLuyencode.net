# Đếm 1 số có bao nhiêu chữ số
# 1234
# n = a
# s = 1  # so chu so
# while n > 10:

#     if n // 10 > 0:
#         s = s+1
#         n = n // 10
n = int(input())

n = abs(n)
s = 1
while n > 10:

    if n // 10 > 0:
        s = s+1
        n = n // 10

print(s)

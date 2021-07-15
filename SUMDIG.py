n = int(input())
kq = []
SoDuong = []

for x in range(n):
    A = input()
    if int(A) > 0:
        SoDuong.append(A)

for i in SoDuong:
    tong = 0
    for letter in i:
        tong = tong + int(letter)
    print(tong)

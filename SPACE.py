# n = int(input())
# kq = []

# for i in range(n):
#     dem = 0
#     n = input()
#     if n[0] == " ":
#         dem += 1
#     if n[-1] == " ":
#         dem += 1
#     n = " ".join(n.split())
#     for char in n:
#         if char == " ":
#             dem += 1
#     kq.append(dem)

# for i in kq:
#     print(i)


kq = []
dem = 0
n = input()
if n[0] == " ":
    dem += 1
if n[-1] == " ":
    dem += 1
n = " ".join(n.split())
for char in n:
    if char == " ":
        dem += 1
kq.append(dem)

for i in kq:
    print(i)

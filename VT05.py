n, x = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
dem = 0
for i in A:
    if i == x:
        dem += 1
print(dem)

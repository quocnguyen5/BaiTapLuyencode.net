n = int(input())
n = abs(n)
dem = 0
if n == 0:
    print("INF")
else:
    for i in range(1, n + 1):
        if n % i == 0:
            dem += 1
print(dem)

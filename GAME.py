m, n = [int(x) for x in input().split()]

dem = (m / 2) * (n / 2)
conlai = (m * n) - (4 * dem)
if conlai % 2 == 0:
    dem += conlai / 2
else:
    dem += ((conlai / 2) + 1)

print(int(dem))

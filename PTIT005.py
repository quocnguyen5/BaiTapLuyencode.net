n = input()
tongso = 0

for i in n:
    tongso += int(i)

if int(n) % tongso == 0:
    print("YES")
else:
    print("NO")

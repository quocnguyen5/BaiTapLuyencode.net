s = input()
s = s.lower()
T = int(input())
L = []
for i in range(T):
    L.append(input().lower())

for i in L:
    print(s.count(i))

a, b = [(x) for x in input().split()]
L = []
for i in range(int(a)):
    n = input()
    if b not in n:  
        L.append(n)

for i in L:
    print(i)
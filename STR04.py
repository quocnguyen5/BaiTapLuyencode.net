s = input()
s = s.lower()

L = []
for i in s:
    if (48 <= ord(i) <= 57) or (97 <= ord(i) <= 122):
        if i not in L:
            L.append(i.lower())
L.sort()
for i in L:
    print(i, s.count(i))

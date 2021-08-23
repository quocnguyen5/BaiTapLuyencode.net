str = input()
Lstr = []
for char in str:
    Lstr.append(char)

Lstr = list(set(Lstr))

for i in Lstr:
    print(i,end='')


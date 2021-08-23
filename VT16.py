A = [int(x) for x in input().split()]

SoAm = []
for i in A:
    if i < 0:
        SoAm.append(i)

if SoAm != []:
    for i in SoAm:
        print(i, end=' ')
else:
    print('NOT FOUND')
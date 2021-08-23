a, b = [int(x) for x in input().split()]
ChiaChoBa = []
for i in range(b - 1, a, -1):
    if i % 3 == 0:
        ChiaChoBa.append(i)
if ChiaChoBa == []:
    print('NOT FOUND')
else:
    for i in ChiaChoBa:
        print(i, end=' ')
    

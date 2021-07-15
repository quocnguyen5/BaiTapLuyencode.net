D1 = input().split()
D2 = input().split()

HD = 0
HP = 0

for i in range(0,3):
    if int(D1[i]) > int(D2[i]):
        HD += 1
    if int(D1[i]) < int(D2[i]):
        HP += 1

print(HD, HP)

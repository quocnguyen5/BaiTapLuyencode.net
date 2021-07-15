n = input()
Lalpha = []
Lnumberic = []
tong = 0
for i in n:
    if i.isalpha():
        Lalpha.append(i)
    elif i.isnumeric():
        Lnumberic.append(i)

for i in Lnumberic:
    tong += int(i)

for i in Lalpha:
    print(i, end='')
print(tong)

n = input()
TSC = 0
TSL = 0

for i in n:
    if int(i) % 2 == 0:
        TSC += int(i)
    else:
        TSL += int(i)
        
print(TSC)
print(TSL)

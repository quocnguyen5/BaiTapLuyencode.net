s = input()
L=[]
for i in s:
    L.append(i)
L2=list(set(L))
print(int(len(L)/len(L2)),end='')
for i in L2:
    print(i, end='')


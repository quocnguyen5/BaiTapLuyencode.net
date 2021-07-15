t=int(input())
h=(t//3600)%24
m=(t%3600)//60
s=(t%3600)%60
if len(str(h)) == 1:
    h = '0' + str(h)
if len(str(m)) == 1:
    m = '0' + str(m)
if len(str(s)) == 1:
    s = '0' + str(s)
print(h,':',m,':',s,sep='')

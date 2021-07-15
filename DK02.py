a, b, c = [int(x) for x in input().split()]
max = a
if(max < b):
    max = b
if(max < c):
    max = c
print(max)

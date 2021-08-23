
a, b = [str(x) for x in input().split()]

for i in range(ord(a), ord(b)+1): 
    print("{:c}".format(i).upper(), end=' ')
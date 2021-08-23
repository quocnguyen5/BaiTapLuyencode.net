n = input()
if ord(n) == 122:
    print("a")
else:
    print("{:c}".format(ord(n) + 1))

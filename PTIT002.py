a1, b1, c1 = [int(x) for x in input().split()]
a2, b2, c2 = [int(x) for x in input().split()]
a3, b3, c3 = [int(x) for x in input().split()]

kq = a1*b2*c3 + b1*c2*a3 + c1*a2*b3 - c1*b2*a3 - b1*a2*c3 - a1*c2*b3
print(kq)
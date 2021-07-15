# a, b = [int(x) for x in input().split()]
# s = 0
# if a % 2 != 0:
#     a += 1
# else:
#     a = a
# for i in range(a, b+1, 2):
#     s = s + i
# print(s)
a, b = [int(x) for x in input().split()]
sum=0
while a<=b:
    if a % 2 == 0:
        sum=sum+a
    a=a+1
print(sum)
# 38. VT02 - Tìm số lớn thứ hai của mảng

# n = int(input())
# A = [int(x) for x in input().split()]
# A = list(set(A))
#
# if n == 1:
#     print("NOT FOUND")
# elif n > 2:
#     max1 = max(A)
#     A.remove(max1)
#     max2 = max(A)
#
# print(max2)
#
# n = int(input())
# A = [int(x) for x in input().split()]
# A = list(set(A))
# HamSNT = []
#
#
# def CheckSNT(n):
#     dem = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             dem += 1
#     if dem == 2:
#         return True
#     else:
#         return False
#
#
# for i in A:
#     if CheckSNT(i):
#         HamSNT.append(i)
# HamSNT.sort()
# for i in HamSNT:
#     print(i, end=' ')
# import re
# n = input()
# kq = re.findall("\d+",n)
# print((len(kq)))
# import re
# n = input()
# kq = re.findall("\d+",n)
# print(len(kq))
# import itertools
# n = input()
# A = []
# for i in n:
#     A.append(i)

# L2 = list(set(itertools.permutations(A)))
# L2.sort()
# print(len(L2))
# for i in L2:
#     for j in i:
#         print(j,end='')
#     print()
# A = 'nguyen quoc nguyen'
# B = ['a','b','c','a','d']
# print(A.count('n'))
# print(B.count('a'))
# A = A.replace('nguyen','thien')
# print(A)
# A = A.split()
# print(A)
# B = '-'.join(B)
# print(B)

n = int(input())
A = [int(x) for x in input().split()]
A.reverse()
x = A.index(max(A))
print(n-x-1)

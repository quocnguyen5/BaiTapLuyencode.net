1. CB01 - Tổng 2 số Nguyên
```python
print('Lap Trinh Khong Kho!')
```

2. CB02 - Tính tổng của 3 số nguyên
```python
a, b = [int(x) for x in input().split()]
print(a+b)
```

3. CB03 - Tính tổng của 3 số nguyên
```python
a, b, c = [int(x) for x in input().split()]
print(a + b + c)
```

4. CB04 - Tính tổng, hiệu, tích, thương của 2 số nguyên
```python
import math
a, b = [int(x) for x in input().split()]
if abs(a) <= 100 and abs(b) <= 100:
    print(a+b)
    print(a-b)
    print(a*b)
    
    if b == 0:
        print('INF')
    else:
        print(round(float(a/b),2)
```

5. CB05 - Tìm số dư
```python
a, b = [int(x) for x in input().split()]
if 0 < a <= 5000 and 0 < b <= 5000:
    print((a+b)*2)
    print(a*b)
```

6. CB06 - Tính chu vi, diện tích hình chữ nhật
```python
a, b = [int(x) for x in input().split()]
if 0 < a <= 5000 and 0 < b <= 5000:
    print((a+b)*2)
    print(a*b)
```

7. CB07 - Tính chu vi, diện tích hình tròn
```python
r = float(input())
p = 3.14
if 0 < r < 1000:
    c = r*r*p
    s = r*2*p
print(round(s,3), round(c,3))
```

8. CB08 - Lại là tính tổng 2 số
```python
import math
a, b = [int(x) for x in input().split()]
if abs(a) <= pow(10,9) and abs(b) <= pow(10,9):
    print(a,'+',b,'=',a+b)
```

9. DK01 - Tìm số lớn nhất
```python
a, b = [int(x) for x in input().split()]

max = a
if(max < b):
    max = b

print( max)
```

10. DK02 - Tìm số lớn nhất trong 3 số
```python
a, b, c = [int(x) for x in input().split()]
max = a
if(max < b):
    max = b
if(max < c):
    max = c
print(max)
```

11. DK03 - Tìm chênh lệch giá trị của 2 số nguyên
```python
a, b = [int(x) for x in input().split()]
if abs(a) <= pow(10, 6) and abs(b) <= pow(10, 6):
    print(abs(a-b))
```

12. DK04 - Làm tròn số
```python
n = float(input())
if int(n) % 2 == 0 and n-int(n)==0.5:
    print(int(n)+1)
    
else: 
    print(round(n))
```

13. DK06 -  Giải phương trình bậc nhất 1 ẩn
```python
a, b = [int(x) for x in input().split()]
if a== 0 and b== 0:
    print("INF")
elif a== 0 and b!= 0:
    print('NO')
elif a!= 0 and b== 0:
    print('0.00')
else:
    x = -b/a
    print(round(x,2))
```

14. DK09 - Kiểm tra năm nhuận
```python
y=int(input())
if 0 < y <=100000:
    if (y % 4 ==0 and y % 100 !=0) or y % 400 ==0:
        print('YES')
    else:
        print('NO')
else: 
    print('INVALID')
```

15. DK10 - Tìm số ngày của tháng
```python
a, b = [int(x) for x in input().split()]
if a in (1,3,5,7,8,10,12):
    print('31')
elif a in (4,6,9,11):
    print('30')
elif a ==2:
    if (b % 4 ==0 and b % 100 !=0) or (b % 400 ==0):
        print( '29')
    else:
        print('28')
else:
    print('INVALID')
```

16. VL01 - In ra các số từ a đến b
```python
a, b = [int(x) for x in input().split()]
for i in range (a,b+1):
    print (i, end=' ')
```

17. SUM1 - Tính tổng phiên bản 1
```python
a = int(input())
s = 0
for i in range (1, a+1):
    s = s + i
print (s)
```

18. DK08 - Máy tính bỏ túi đơn giản
```python
nhap = str(input())
result = 0
try:
    a, c, b = [str(x) for x in nhap.split()]
    a = float(a)
    b = float(b)

    if abs(a) <= 10000 and abs(b) < 10000:
        if c == '/':
            if b == 0:
                print('Math Error')
            else:
                result = a/b
                print("{:.2f}".format(result))
        elif c == '+':
            result = a+b
            print("{:.2f}".format(result))
        elif c == '-':
            result = a-b
            print("{:.2f}".format(result))
        elif c == '*':
            result = a*b
            print("{:.2f}".format(result))
    else:
        print('Math Error')

except:

    # a,b= [float(x) for x in nhap.split('+' or '-' or '/' or '*')]
    # a= float(a)
    # b= float(b)
    for letter in nhap:
        if letter == '/':
            a, b = [float(x) for x in nhap.split('/')]
            if b == 0:
                print('Math Error')
            else:
                result = a/b
                print("{:.2f}".format(result))
        elif letter == '+':
            a, b = [float(x) for x in nhap.split('+')]
            result = a+b
            print("{:.2f}".format(result))
        elif letter == '-':
            a, b = [float(x) for x in nhap.split('-')]
            result = a-b
            print("{:.2f}".format(result))
        elif letter == '*':
            a, b = [float(x) for x in nhap.split('*')]
            result = a*b
            print("{:.2f}".format(result))

```
19. VL03 - Tính tổng S = (2 + 3 + 4... + n) + 2n
```python
n = int(input())
S= 0
if n >= 2:
    for i in range(2,n+1):
        S= S + i
    print(S+2*n)
```
20. VL04 - Tính tổng S = 1/2 + 1/3 + ... + 1/n

```python
n = int(input())
S = 0
if 10**4 >= n >= 2:
    for i in range(2, n+1):
        S = S + 1/i
    print(("{:.4f}".format(S)))
else:
    n = int(input())
```
21. VL05 - Tính giá trị S = 1 - 2 + 3 - ... + (3n + 1)
```python
n = int(input())
S = 0
for i in range(0,3*n+2):
    if i % 2 == 0:
        S = S - i
    else:
        S = S + i
print(S)
```
22. GT1 - Tính giai thừa 1
```python
n = int(input())
result = 1
for i in range(1, n+1):
    result = result * i
print(result)
``` 
23. VL08 - Tính tổng các số chẵn trong [a, b]
```python
a, b = [int(x) for x in input().split()]
s = 0
if a % 2 != 0:
    a += 1
else:
    a = a
for i in range(a, b+1, 2):
    s = s + i
print(s)
```
24. VL09 - Tính S = x + x^2/2! + ... + x^n/n!
```python
x, n = [int(x) for x in input().split()]
S = x
m = 1
for i in range(2, n+1):
    m = m*i
    S = S + (pow(x,i))/m
print('{:.2f}'.format(S))
```
25. VL10 - Đếm số lượng chữ số của số n
```python
n = int(input()) #Cách này trong phần bình luận mọi người giới thiệu
print("{}".format(len(str(n).replace("-", ""))))

n = abs(n) # Cách tự làm
s = 1
while n > 10:

    if n // 10 > 0:
        s = s+1
        n = n // 10

print(s)
```
26. VL12 - Liệt kê các ước số
```python
n = int(input())
n = abs(n)
UocSo = []
if n ==0:
    print('INF')
else:
    for i in range(1, n+1):
        if n % i == 0:
            UocSo.append(i)
    UocSo.sort(reverse=True)

    for i in UocSo:
        print(i, end=' ')
```
27. VL13 - Kiểm tra số hoàn hảo
```python
n = int(input())
tong = 0
if n <= 0:
    print('NO')
else:
    for i in range(1, n,1):
        if n % i == 0:
            tong += i
    if tong == n:
        print('YES')
    else:
        print('NO')
```
28. VL14 - Tìm ước chung lớn nhất của 2 số
```python
a, b = [int(x) for x in input().split()]
a = abs(a)
b = abs(b)
UocSoA = []
UocSoB = []
UocChung = []
for i in range(1, a+1):
    if a % i == 0:
        UocSoA.append(i)

for i in range(1, b+1):
    if b % i == 0:
        UocSoB.append(i)
if UocSoB == [] or UocSoA == []:
    UocChung = UocSoA + UocSoB
    print(max(UocChung))
else:
    for i in UocSoA:
        for j in UocSoB:
            if i == j:
                UocChung.append(i)
    print(max(UocChung))
```
29. VL15 - Rút gọn phân số
```python
a, b = [int(x) for x in input().split()]
x = y = 0
UocSoA = []
UocSoB = []
UocChung = []
if b == 0:
    print("INVALID")
elif a == 0:
    print(0)
else:
    x = abs(a)
    y = abs(b)
    for i in range(1, x + 1):
        if x % i == 0:
            UocSoA.append(i)

    for i in range(1, y + 1):
        if y % i == 0:
            UocSoB.append(i)
    if UocSoB == [] or UocSoA == []:
        UocChung = UocSoA + UocSoB
        print(max(UocChung))
    else:
        for i in UocSoA:
            for j in UocSoB:
                if i == j:
                    UocChung.append(i)

    tu = a / max(UocChung)
    mau = b / max(UocChung)

    if mau < 0:
        tu = -tu
        mau = abs(mau)
    if mau == 1:
        print(int(tu))
    else:
        print(int(tu), int(mau), sep=" ")
```
30. VL16 - Tìm bội chung nhỏ nhất của 2 số
```python
a = abs(a)
b = abs(b)
UocSoA = []
UocSoB = []
UocChung = []
for i in range(1, a+1):
    if a % i == 0:
        UocSoA.append(i)

for i in range(1, b+1):
    if b % i == 0:
        UocSoB.append(i)
if UocSoB == [] or UocSoA == []:
    UocChung = UocSoA + UocSoB
    print(max(UocChung))
else:
    for i in UocSoA:
        for j in UocSoB:
            if i == j:
                UocChung.append(i)
    
BCNN = a * b // max(UocChung)
print(BCNN)
```
31. VL17 - Đếm số lượng ước số
```python
n = int(input())
n = abs(n)
dem = 0
if n == 0:
    print("INF")
else:
    for i in range(1, n + 1):
        if n % i == 0:
            dem += 1
print(dem)

```
32. VL19 - In ra các số chia hết chia hết cho 3
```python
a, b = [int(x) for x in input().split()]
ChiaChoBa = []
for i in range(b - 1, a, -1):
    if i % 3 == 0:
        ChiaChoBa.append(i)
if ChiaChoBa == []:
    print('NOT FOUND')
else:
    for i in ChiaChoBa:
        print(i, end=' ')
```
33. VL20 - In ra các chữ cái
```python
import string
a, b = [str(x) for x in input().split()]

for i in range(ord(a), ord(b)+1): 
    print("{:c}".format(i).upper(), end=' ') #Hoặc đùng chr()
```
34. DK05 - Kiểm tra số chính phương
```python
import math

n = int(input())
if 0 <= n <= pow(10, 12):
    if n % 10 in (0, 1, 4, 5, 6, 9):
        if n == 0:
            print("YES")
        else:
            check = False

            for i in range(1, n + 1):
                if i ** 2 == n:
                    check = True
                    break

            if check == True:
                print("YES")
            else:
                print("NO")
    else:
        print("NO")
else:
    print("NO")
```
35. VL18 - Tìm số đảo ngược
```python
n = int(input())
ham = []
if 0 < n <= pow(10, 1000):
    for letter in str(n):
        ham.append(letter)
    ham.reverse()
    x = ""
    for i in ham:
        x = x + i
    print(int(x))

```
36. VL21 - Đi tìm ẩn số
```python
n = int(input())

def timi(n):
    x = 0
    for i in range(1, n):
        x += i
        if x > n:
            return i-1
print(timi(n))
```
37. VT01 - Tìm số lớn nhất trong mảng
```python
n = int(input())
A = [int(x) for x in input().split()]
if len(A) == n :
    max = A[1]
    for x in A:
        if x > max:
            max = x
print(max)
```
38. VT02 - Tìm số lớn thứ hai của mảng
```python
n = int(input())
A = [int(x) for x in input().split()]
A2 = []


def SoLonThu2():
    max1 = max2 = A[1]
    for i in range(n):
        if A[i] >= max1:
            x = max1
            max1 = A[i]
            max2 = x
    return max2


for i in A:
    if i not in A2:
        A2.append(i)
if len(A2) == 1:
    print("NOT FOUND")
else:
    max = SoLonThu2()
    print(max)
```
39. VT03 - Chỉ số mảng có giá trị lớn nhất
```python
n = int(input())
A = [int(x) for x in input().split()]
if len(A) == n:
    A.reverse()
    max = A[1]
    for x in range(n):
        if A[x] >= max:
            max = A[x]
print(n - (A.index(max)+1))
```
40. VT04 - Tìm kiếm trong mảng
```python
n, x = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
if x in A:
    print('YES')
else:
    print('NO')
```
41. VT05 - Học đếm trong mảng
```python
n, x = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
dem = 0
for i in A:
    if i == x:
        dem += 1
print(dem)
```
42. VT06 - Tính trung bình cộng của mảng
```python
TONG = 0
SNL = 0

n = int(input())
A = [int(x) for x in input().split()]
for i in A:
    if i % 2 != 0:
        SNL += 1
        TONG += i

if SNL == 0:
    print(0)
else:
    TBC = TONG / SNL
    print("{:.4f}".format(TBC))
```
43. VT07 - Vẫn là tìm kiếm trong mảng
```python
A = [int(x) for x in input().split()]
x = A.pop(10)
if x in A:
    for i in range(10):
        if A[i] == x:
            print(i+1, end=' ')
else:
    print(-1)
```
44. VT08 - Biến đổi mảng 1 chiều
```python
n = int(input())
A = [int(x) for x in input().split()]
A.append(0)
for i in range(1, n, 2):
    A[i] = A[i] + abs((A[i + 1] - A[i - 1]))

del A[n]
for i in A:
    print(i, end=" ")
```
45. VT09 - Tìm số nguyên tố trong mảng
```python
n = int(input())
A = [int(x) for x in input().split()]


def LaNST(n):
    dem = 0
    for i in range(1, n + 1):
        if n % i == 0:
            dem += 1
    if dem == 2:
        return True
    return False


B = []
for n in A:
    if LaNST(n) and n not in B:
        B.append(n)
B.sort()
for i in B:
    print(i,end=' ')
```
46. VT10 - Sắp xếp mảng giảm dần
```python
n = int(input())
A = [int(x) for x in input().split()]

A.sort(reverse=True)
for i in A:
    print(i, end=" ")
```
47. VT11 - Lại là sắp xếp mảng
```python
n = int(input())
A = [int(x) for x in input().split()]
B = A[1 : (n - 1)]
B.sort()

A = [A[0]] + B + [A[n - 1]]

for i in A:
    print(i, end=" ")
```
48. VT12 - Tìm chênh lệch lớn nhất trong mảng
```python
n = int(input())
A = [int(x) for x in input().split()]

max = min = A[0]
for i in range(n):
    if A[i] > max:
        max = A[i]
    if A[i] < min:
        min = A[i]

print(max - min)
```
49. VT13 - Đi tìm cặp đôi
```python
n = int(input())
A = [int(x) for x in input().split()]

max = 0
so1 = 0
so2 = 0
if n % 2 == 1:
    A.append(A[0])
    for i in range(n):
        if A[i] + A[i + 1] > max:
            max = A[i] + A[i + 1]
            so1 = i
            so2 = i + 1
    if so1 == n:
        print(A[so2], A[so1])
    else:
        print(A[so1], A[so2])
else:
    for i in range(n - 1):
        if A[i] + A[i + 1] >= max:
            max = A[i] + A[i + 1]
            so1 = i
            so2 = i + 1
    print(A[so1], A[so2])
```
50. VT14 - Lại là đi tìm cặp đôi
```python
n = int(input())
A = [int(x) for x in input().split()]

LAm = []
LDuong = []
MaxDuong = 0
MaxAm = 0


for i in A:
    if i < 0:
        LAm.append(i)
    elif i > 0:
        LDuong.append(i)


def TichSoAm(A, LAm):
    max1am = max2am = 0

    for i in LAm:
        if abs(i) > max1am:
            max1am = abs(i)
    LAm.remove(-max1am)

    for i in LAm:
        if abs(i) > max2am:
            max2am = abs(i)
    return max1am, max2am


def TichSoDuong(A, LDuong):
    max1duong = max2duong = 0

    for i in LDuong:
        if i > max1duong:
            max1duong = i
    LDuong.remove(max1duong)

    for i in LDuong:
        if i > max2duong:
            max2duong = i
    return max1duong, max2duong


def inKQ(A, LAm, LDuong, TichSoAm, TichSoDuong):
    
    if LAm == []:
        max1duong, max2duong = TichSoDuong(A, LDuong)
        print(max1duong * max2duong)

    elif LDuong == []:
        max1am, max2am = TichSoAm(A, LAm)
        print(max1am * max2am)

    elif LAm != [] and LDuong != []:
        max1duong, max2duong = TichSoDuong(A, LDuong)
        max1am, max2am = TichSoAm(A, LAm)
        MaxDuong = max1duong * max2duong
        MaxAm = max1am * max2am
        if MaxDuong > MaxAm:
            print(MaxDuong)
        else:
            print(MaxAm)


inKQ(A, LAm, LDuong, TichSoAm, TichSoDuong)
```
51. VT16 - Liệt kê các số âm
```python
A = [int(x) for x in input().split()]

SoAm = []
for i in A:
    if i < 0:
        SoAm.append(i)

if SoAm != []:
    for i in SoAm:
        print(i, end=' ')
else:
    print('NOT FOUND')
```
52. DT1 - Tính diện tích hình
```python
import math
a = int(input())
ketqua = (math.pi*pow(a,2))/2
print("{:.3f}".format(ketqua))
```
53. SUM2 - Tính tổng phiên bản 2
```python
n = int(input())
ketqua = (n * (n + 1) * (2 * n + 1)) / 6
print(int(ketqua))
```
54. SUM3 - Tính tổng phiên bản 3
```python
n = int(input())
ketqua = 1 - 1 / (n + 1)
print("{:.5f}".format(ketqua))
```
55. 
```python
n = int(input())
kq = []
SoDuong = []

for x in range(n):
    A = input()
    if int(A) > 0:
        SoDuong.append(A)

for i in SoDuong:
    tong = 0
    for letter in i:
        tong = tong + int(letter)
    print(tong)
```
56. GPTB1 - Hệ phương trình bậc nhất
```python
a1, b1, c1, a2, b2, c2 = [int(x) for x in input().split()]

D = a1 * b2 - a2 * b1
Dx = c1 * b2 - c2 * b1
Dy = a1 * c2 - a2 * c1

if D == 0:
    if Dx == Dy:
        print("VOSONGHIEM")
    else:
        print("VONGHIEM")
else:
    x = Dx / D
    y = Dy / D
    if x == -0:
        x = 0
    if y == -0:
        y = 0

    print("{:.2f}".format(x), "{:.2f}".format(y), end=" ")
```
57. DK07 - Giải phương trình
```python
import math


def giaiPTBac2(a, b, c):
    # kiểm tra các hệ số
    if a == 0:
        if b == 0:
            if c!=0:
                print('NO')
            else:
                print('INF')
        else:
            print("{:.2f}".format(+(-c / b)))
        return

    delta = b * b - 4 * a * c
    # tính nghiệm
    if delta > 0:
        x1 = (float)((-b + math.sqrt(delta)) / (2 * a))
        x2 = (float)((-b - math.sqrt(delta)) / (2 * a))
        if x1 > x2:
            print("{:.2f}".format(x2), "{:.2f}".format(x1), end=" ")
    elif delta == 0:
        x1 = -b / (2 * a)
        print("{:.2f}".format(x1))
    else:
        print("NO")


a, b, c = [int(x) for x in input().split()]

giaiPTBac2(a, b, c)
```
58. VECTOR - Véc tơ
```python
n = int(input())
print(n*(n-1))
```
59. TRIPLETS - So sánh bộ ba số
```python
D1 = input().split()
D2 = input().split()

HD = 0
HP = 0

for i in range(0,3):
    if int(D1[i]) > int(D2[i]):
        HD += 1
    if int(D1[i]) < int(D2[i]):
        HP += 1

print(HD, HP)
```
60. THETICH - Tổng thể tích
```python
n = int(input())
TT = 0

for i in range(1,n+1):
    TT += pow(i,3)

print(TT)

```
61. STR01 - Chuyển chuỗi về viết thường
```python
s = input()
print(s.lower())
```
62. SCBN1 - Số cặp bằng nhau 1
```python
n = int(input())
A = [int(x) for x in input().split()]
dem = 0

for i in range(n - 1):
    if A[i] == A[i + 1]:
        dem += 1
print(dem)
```
63. PTIT001 - Vẽ hình chữ nhật đặc
```python
n = int(input())
for i in range(n):
    print(n * "*")
```
64. PTIT002 - Tìm định thức của ma trận vuông
```python
a1, b1, c1 = [int(x) for x in input().split()]
a2, b2, c2 = [int(x) for x in input().split()]
a3, b3, c3 = [int(x) for x in input().split()]

kq = a1*b2*c3 + b1*c2*a3 + c1*a2*b3 - c1*b2*a3 - b1*a2*c3 - a1*c2*b3
print(kq)
```
65. PTIT004 - Số đơn giản
```python
n = input()


def check(n):
    if len(n) == 1:
        return True
    return False


def rutgon(n):
    x = 0
    for i in n:
        x += int(i)
        n = str(x)
    return n


while check(n) == False:
    n = rutgon(n)
print(n)
```
66. PTIT005 - Số đặc biệt
```python
n = input()
tongso = 0

for i in n:
    tongso += int(i)

if int(n) % tongso == 0:
    print("YES")
else:
    print("NO")
```
67. PTIT012 - Thế nào là tràn số?
```python
a, b = [int(x) for x in input().split()]
c = a + b
d = a - b
f = a * b
print(c,d,f)
```
68. PTIT014 - Chữ số tận cùng của 2^n
```python
n = int(input())
b = str(pow(2,n))
print(int(b[-1]))
```
69. PTIT019 - Sắp xếp 3 số nguyên
```python
A = [int(x) for x in input().split()]
A.sort(reverse=True)
for i in A:
    print(i, end=" ")
```
70. PTIT023 - Bạn bao nhiêu tuổi?
```python
n = int(input())
print(2021 - n)
```
71. PTIT051 - Hoàn thành câu lệnh
```python
b, a, c = [int(x) for x in input().split()]
print("users setClock ", "\\", a, "\\", b, "\\", c, sep="")
```
72. VL11 - Kiểm tra số nguyên tố
```python
n = int(input())
def KiemTraSNT(n):
    if n < 2:
        return False
    if n in (2,3,5):
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False
    for i in range(5, int(n ** (1 / 2)), 2):  
        if n % i == 0:
            return False
    return True

if KiemTraSNT(n):
    print('YES')
else:
    print('NO')
```
73. PTIT056 - Số đặc biệt 2
```python
def KiemTraSNT(n):
    if n < 2:
        return False
    if n in (2, 3, 5):
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False
    for i in range(5, int(n ** (1 / 2)), 2):
        if n % i == 0:
            return False
    return True


n = int(input())
Tongchuso = 0
for i in str(n):
    Tongchuso += int(i)

if KiemTraSNT(n) and KiemTraSNT(Tongchuso):
    print("YES")
else:
    print("NO")
```
74. PTIT059 - Thêm phần tử vào mảng
```python
n = int(input())
N = [int(x) for x in input().split()]
x = int(input())

N.append(x)
N.sort()
for i in N:
    print(i, end=" ")
```
75. PTIT064 - Gộp mảng
```python
n = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

for i in B:
    A.append(i)

A.sort()

for i in A:
    print(i, end=" ")
```
76. STRPOW - Lũy thừa của chuỗi
```python
S = input()
T = input()
K = int(input())

if S * K == T:
    print("YES")
else:
    print("NO")
```
77. PROD - PRODUCT
```python
a, b = [int(x) for x in input().split()]
if a * b < 0:
    print(-1)
elif a * b > 0:
    print(1)
else:
    print(0)
```
78. SEGMENT - Đoạn thẳng
```python
n = int(input())
print(int(n*(n-1)/2))
```
79. PREP - Chuẩn bị cho năm học mới
```python
a, b, x, y = [int(x) for x in input().split()]

Tien = a * x + b * y
print(Tien)
```
80. POINTSTR - Điểm trên 1 chuỗi
```python
n = int(input())
s = input()
print(s.count('luyencode'))
```
81. PHTINH - Phép toán lớp 3
```python
a, b, c = [int(x) for x in input().split()]
print((a-b)*c)
```
82. NHATCHU - Robot nhặt chữ
```python
str = input()
Lstr = []
Lstr2 = []

for char in str:
    Lstr.append(char)
    
for i in Lstr:   
    if i not in Lstr2:
        Lstr2.append(i)

for i in Lstr2:
    print(i, end="")
```
83. GAPDOI - Số gấp đôi
```python
n = int(input())
print(2 * n)
```
84. NEXTCHAR - Ký tự liền sau
```python
n = input()
if ord(n) == 122:
    print("a")
else:
    print("{:c}".format(ord(n) + 1))
```
85. FUNCTION - Tính giá trị hàm bậc 2
```python
a, b, c, x = [int(x) for x in input().split()]
f = a * x * x + b * x + c
print(f)
```
86. AVG3NUM - Trung bình cộng của 3 số
```python
a, b, x = [int(x) for x in input().split()]
c = 3 * x - a - b
print(c)
```
87. CGAME - Pokémon Trading Card Game
```python
a, b = [int(x) for x in input().split()]
if a < b:
    print(0)
elif b < a:
    print(1)
```
88. STR02 - Chuẩn hóa tên riêng
```python
n = int(input())
L =[]
for i in range(n):
   L.append(input()) 

for i in L:
    print(i.title())
```
89. STR03 - Đếm số lượng ký tự
```python
s = input()
s = s.lower()
T = int(input())
L = []
for i in range(T):
    L.append(input().lower())

for i in L:
    print(s.count(i))
```
90. STR04 - Tần suất xuất hiện các ký tự
```python
s = input()
s = s.lower()

L = []
for i in s:
    if (48 <= ord(i) <= 57) or (97 <= ord(i) <= 122): #Dùng hệ mã ASCII
        if i not in L:
            L.append(i.lower())
L.sort()
for i in L:
    print(i, s.count(i))
```
91. KTMOI - Ký Tự Mới
```python
n =input()
print(n.lower())
```
92. CHUANHOA - Chuẩn hóa xấu
```python
n = int(input())
L = []
for i in range(n):
    L.append(input())

for i in L:
    print(" ".join(i.split()))
```
93. DEMTU - Bé học tiếng Anh
```python
n = input()
dem = 0
n = n.split()
print(len(n))
```
94. DEMSO - Đếm số trong chuỗi
```python
import re
n = input()
kq = re.findall("\d+",n)
print(len(kq))
```
95. UPWORD - Đếm từ viết hoa
```python
import re
n = input()
kq = re.findall("[A-Z]+", n)
print(len(kq))
```
96. MUTATE - Biến đổi
```python
n = int(input())
if 1 <= n <= 10 ** 6:
    print(n, end=" ")
    while True:
        if n == 1:
            break
        if n % 2 == 0:
            n = n / 2
            print(int(n), end=" ")
        else:
            n = n * 3 + 1
            print(int(n), end=" ")
        if n == 1:
            break
```
97. OLDSUM - Lẻ lẻ
```python
a, b = [int(x) for x in input().split()]

if a % 2 == 0:
    a = a + 1
if b % 2 == 0:
    b = b - 1

SoHang = ((b - a) / 2) + 1
TongLe = ((b + a) * SoHang) / 2

print(int(TongLe))
```
98. OLDEVEN - Tổng chẵn lẻ
```python
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
```
99. SUMRANGE - Tổng các số lẻ
```python
a, b = [int(x) for x in input().split()]

if a % 2 == 0:
    a = a + 1
if b % 2 == 0:
    b = b - 1

SoHang = ((b - a) / 2) + 1
TongLe = ((b + a) * SoHang) / 2

print(int(TongLe))
```
100. ENCRYPT - Mã hóa mật khẩu
```python
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
```
101. ABC051_A - Thơ Haiku
```python
n = input()
print(n.replace(',',' '))
```
102. STRCMP - So sánh chuỗi
```python
a, b = [int(x) for x in input().split()]

if ord(str(a)) > ord(str(b)):
    print(str(b) * a)
else:
    print(str(a) * b)
```
103. KH_05 - Sinh chuỗi
```python
import itertools
n = input()
L = []

for char in n:
    L.append(char)

L2 = list(set(itertools.permutations(L)))
L2.sort()
print(len(L2))
for i in L2:
    for j in i:
        print(j,end='')
    print()
```
104. ABC042_B - Iroha và chuỗi ký tự
```python
a, b = [int(x) for x in input().split()]
L = []

for i in range(a):
    L.append(input())
L.sort()
for i in L:
    print(i,end='')
```
105. MEDICINE - Ghép tên thuốc
```python
L = []
n = input()

for i in n:
    L.append(i)
L = list(set(L))

print(len(L))
```
106. NAME - Chuẩn hóa danh từ riêng
```python
n = int(input())
L = []
for i in range(n):
    n = input()
    L.append(n.title())

for i in L:
    print(i)
```
107. MEET - Địa điểm họp mặt
```python
a, b = [(x) for x in input().split()]
L = []
for i in range(int(a)):
    n = input()
    if b not in n:  
        L.append(n)

for i in L:
    print(i)
```
108. FCDEM - Đếm số âm, dương trong mảng
```python
n = int(input())
A = [int(x) for x in input().split()]

LAm = []
LDuong = []

for i in A:
    if i < 0:
        LAm.append(i)
    elif i > 0:
        LDuong.append(i)

print(len(LAm),end=' ')
print(len(LDuong))
```
109. CUTTING - Cắt bánh sinh nhật
```python
n, m = [int(x) for x in input().split()]q  
`
print(n * m - 1)
```
110. RESTAURANT - Nhà hàng bánh ngọt
```python
def CanhHinhVuong(a, b):
    a = abs(a)
    b = abs(b)
    UocSoA = []
    UocSoB = []
    CanhHinhVuong = []
    for i in range(1, a + 1):
        if a % i == 0:
            UocSoA.append(i)

    for i in range(1, b + 1):
        if b % i == 0:
            UocSoB.append(i)
    if UocSoB == [] or UocSoA == []:
        CanhHinhVuong = UocSoA + UocSoB
        return max(CanhHinhVuong)
    else:
        for i in UocSoA:
            for j in UocSoB:
                if i == j:
                    CanhHinhVuong.append(i)
        return max(CanhHinhVuong)


n = int(input())
kq = []

for i in range(n):
    a, b = [int(x) for x in input().split()]
    n = CanhHinhVuong(a, b)
    kq.append(int((a * b) / (n * n)))

for i in kq:
    print(i)
```
111. MAXTRI - Số lớn nhất tạo thành
```python
A = [int(x) for x in input().split()]
A.sort(reverse=True)
for i in A:
    print(i, end="")
```
112. SUMBIG - Tính tổng 2 số nguyên lớn
```python
a = int(input())
b = int(input())
print(a + b)
```
113. SUM4 - Tính tổng phiên bản 4
```python
n = int(input())
kq = []
for i in range(n):
    x = int(input())
    S = 2 * (1 - 1 / (x + 1))
    kq.append(S)

for i in kq:
    print('{:.8f}'.format(i))
```
114. MT01 - In mảng 2 chiều dạng bảng
```python
m, n = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]
x = 0
for i in L:
    print(i, end=" ")
    x += 1
    if x == n:
        print()
        x = 0
```
115. MULBIG - Nhân 2 số nguyên lớn
```python
a = int(input())
b = int(input())
print(a*b)
```
116. GT2 - Tính giai thừa 2
```python
def TinhGiaiThua(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    print(result)

n = int(input())
L = [int(x) for x in input().split()]
for i in L:
    TinhGiaiThua(i)
```
117. DATE2 - Đổi thời gian
```python
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
```
118. NEWYEAR - Lời chúc tết
```python
n = int(input())
L = []
for i in range(n):
    L.append(input())

print(len(list(set(L))))
```
119. MOD - MOD
```python
n = input()
L = []
kq = []
for i in n:
    L.append(i)
if len(L) >= 3:
    L = L[len(L) - 3 : len(L)]
    for i in L:
        print(i, end="")
elif len(L) == 2:
    print("0", end="")
    for i in L:
        print(int(i), end="")
elif len(L) == 1:
    print("00", end="")
    print(L[0])
```
120. MT03 - Tính tổng đường chéo chính
```python
n = int(input())
L = [int(x) for x in input().split()]
tong = 0

for i in range(0, len(L), n+1):
    tong += L[i]
print(tong)
```
120.
```python
```
121.
```python
```
122.
```python
```
120.
```python
```
120.
```python
```
120.
```python
```
120.
```python
```
120.
```python
```
120.
```python
```
120.
```python
```

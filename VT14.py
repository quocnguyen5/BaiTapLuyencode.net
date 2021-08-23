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

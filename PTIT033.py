n = int(input())
a, b = (int(x) for x in input().split())

if a == 0 and b == 0:
    print("Khong chia het cho so nao ca.")
elif a == 0 or b == 0:
    if a == 0 and n % b == 0:
        print("Chi chia het cho ", b, ".", sep="")
    if a == 0 and n % b != 0:
        print("Khong chia het cho so nao ca.")
    if b == 0 and n % a == 0:
        print("Chi chia het cho ", a, ".", sep="")
    if b == 0 and n % a != 0:
        print("Khong chia het cho so nao ca.")
else:
    if n % b == 0 and n % a == 0:
        print("Co, tat ca!")
    elif n % b == 0 and n % a != 0:
        print("Chi chia het cho ", b, ".", sep="")
    elif n % a == 0 and n % b != 0:
        print("Chi chia het cho ", a, ".", sep="")
    else:
        print("Khong chia het cho so nao ca.")

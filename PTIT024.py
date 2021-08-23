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


s = input()
for i in range(len(s)):
    if KiemTraSNT(i):
        s = s.replace(s[i], "*")
    else:
        continue
print(s)

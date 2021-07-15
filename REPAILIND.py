def isPalindrome(str):

    for i in range(0, int(len(str) / 2)):

        if str[i] != str[len(str) - i - 1]:
            return False
    return True

T = int(input())
KQ = []
for i in range(1,3,-1):
    str = input()
    k = int(input())
    if isPalindrome(str):
        KQ.append('YES')
    else:
        KQ.append('NO')
    if k == 1:
        break

for i in KQ:
    print(i)
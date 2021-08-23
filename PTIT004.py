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

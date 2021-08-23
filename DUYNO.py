def check(string):
    if string[0] == string[-1]:
        return True
    return False



while True:
    str = input()
    if str == "":
        break
    if check(str):
        print("YES")
    else:
        print("NO")

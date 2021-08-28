def check(string):
    if string[0] == string[-1]:
        return True
    return False



while True:
    try:
        str = input()
        if check(str):
            print("YES")
        else:
            print("NO")
    except EOFError:
        break
    

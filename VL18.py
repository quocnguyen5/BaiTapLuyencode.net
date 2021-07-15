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

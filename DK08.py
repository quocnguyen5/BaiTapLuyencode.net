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

        # print("{:.2f}".format(result))

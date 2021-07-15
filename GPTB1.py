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




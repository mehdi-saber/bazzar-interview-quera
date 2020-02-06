y = int(input())


def kabise(y):
    c1 = y % 400 == 0
    c2 = y % 4 == 0 and y % 100 != 0
    return (c1 or c2) and (not c1 or not c2)


k = 0
z = y
y_kab = kabise(y)
while True:
    z += 1
    kab = kabise(z)
    k += 366 % 7 if kab else 365 % 7
    if k % 7 == 0 and kab == y_kab:
        break

print(z)
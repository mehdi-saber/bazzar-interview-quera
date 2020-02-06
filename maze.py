import math

q = int(input())
for i in range(q):
    cmd, n = input().split()
    n = int(n)
    if cmd == 'item':
        n = n - 1
        y = math.floor((n+0.5) ** 0.5 - 0.5)
        r = math.ceil(y / 2)
        l = math.floor(y / 2)
        u = math.ceil(y / 2)
        d = math.floor(y / 2)
        remain = n - int(y * (y + 1))
        dx = 0
        dy = 0
        if y % 2 == 1:
            dx -= min(y + 1, remain)
            if remain > (y + 1):
                dy -= remain % (y + 1)
        else:
            dx += min(y + 1, remain)
            if remain > (y + 1):
                dy += remain % (y + 1)
        lx = r ** 2 - l * (l + 1) + dx
        ly = u ** 2 - d * (d + 1) + dy
        print(str(lx) + ' ' + str(ly))
    elif cmd == 'list':
        dire = 0
        step = 1
        lx, ly = (0, 0)
        print('0  0')
        while n > 1:
            dlx, dly = (0, 0)
            if dire == 0:
                dlx += 1
            elif dire == 1:
                dly += 1
            elif dire == 2:
                dlx -= 1
            elif dire == 3:
                dly -= 1
            for k in range(step):
                if n <= 1:
                    break
                n -= 1
                lx += dlx
                ly += dly
                print(str(lx) + ' ' + str(ly))
            if dire in [1, 3]:
                step += 1
            dire = (dire + 1) % 4
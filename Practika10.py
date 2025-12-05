import math


def task1_1():
    with open('vvod.txt', 'r') as f:
        n = int(f.readline())
        a = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            a.append(row)

    s = c = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i][j] > 0:
                s += a[i][j]
                c += 1

    with open('vivod.txt', 'w') as f:
        f.write(f"{s} {c}")


def task1_2():
    with open('vvod.txt', 'r') as f:
        n, m = map(int, f.readline().split())
        b = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            b.append(row)

    for i in range(n):
        mn = min(b[i])
        mx = max(b[i])
        mni = b[i].index(mn)
        mxi = b[i].index(mx)
        b[i][0], b[i][mni] = b[i][mni], b[i][0]
        b[i][-1], b[i][mxi] = b[i][mxi], b[i][-1]

    with open('vivod.txt', 'w') as f:
        for r in b:
            f.write(' '.join(map(str, r)) + '\n')


def task2_1():
    with open('vvod.txt', 'r') as f:
        n = int(f.readline())
        a = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            a.append(row)

    s = sum(a[0])
    fg = 1
    for i in range(n):
        if sum(a[i]) != s:
            fg = 0
            break
    for j in range(n):
        if sum(a[i][j] for i in range(n)) != s:
            fg = 0
            break

    with open('vivod.txt', 'w') as f:
        f.write(str(fg))


def task2_2():
    with open('vvod.txt', 'r') as f:
        n, m = map(int, f.readline().split())
        a = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            a.append(row)

    for i in range(n):
        a[i][0], a[i][-1] = a[i][-1], a[i][0]

    with open('vivod.txt', 'w') as f:
        for r in a:
            f.write(' '.join(map(str, r)) + '\n')


def task3_1():
    with open('vvod.txt', 'r') as f:
        n = int(f.readline())
        a = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            a.append(row)

    fg = 1
    for i in range(n):
        for j in range(i + 1, n):
            if a[i][j] != a[j][i]:
                fg = 0
                break

    with open('vivod.txt', 'w') as f:
        f.write(str(fg))


def task3_2():
    with open('vvod.txt', 'r') as f:
        n, m = map(int, f.readline().split())
        a = []
        for _ in range(n):
            row = list(map(float, f.readline().split()))
            a.append(row)

    mx = a[0][0]
    mxi = mxj = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] > mx:
                mx = a[i][j]
                mxi, mxj = i, j

    a[0], a[mxi] = a[mxi], a[0]
    for i in range(n):
        a[i][0], a[i][mxj] = a[i][mxj], a[i][0]

    with open('vivod.txt', 'w') as f:
        for r in a:
            f.write(' '.join(map(str, r)) + '\n')


def task4_1():
    with open('vvod.txt', 'r') as f:
        n, m = map(int, f.readline().split())
        a = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            a.append(row)

    s = [sum(r) for r in a]
    mxi = s.index(max(s))
    mni = s.index(min(s))

    with open('vivod.txt', 'w') as f:
        f.write(' '.join(map(str, a[mxi])) + ' ' + str(s[mxi]) + '\n')
        f.write(' '.join(map(str, a[mni])) + ' ' + str(s[mni]))


def task4_2():
    with open('vvod.txt', 'r') as f:
        n = int(f.readline())
        a = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            a.append(row)

    for i in range(n):
        for j in range(n):
            if a[i][j] > 0:
                a[i][j] = 1
            elif a[i][j] < 0:
                a[i][j] = 0

    with open('vivod.txt', 'w') as f:
        for i in range(n):
            for j in range(i + 1):
                f.write(str(a[i][j]) + ' ')
            f.write('\n')


def task5_1():
    with open('vvod.txt', 'r') as f:
        n, m = map(int, f.readline().split())
        a = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            a.append(row)

    for i in range(n):
        a[i].sort()

    with open('vivod.txt', 'w') as f:
        for r in a:
            f.write(' '.join(map(str, r)) + '\n')


def task5_2():
    with open('vvod.txt', 'r') as f:
        n, m = map(int, f.readline().split())
        a = []
        for _ in range(n):
            row = list(map(float, f.readline().split()))
            a.append(row)

    for i in range(n):
        mn = min(a[i])
        mni = a[i].index(mn)
        if mn % 2 == 0:
            a[i][mni] = 0
        else:
            a[i][mni] = 1

    with open('vivod.txt', 'w') as f:
        for r in a:
            f.write(' '.join(map(str, r)) + '\n')


def task6_1():
    with open('vvod.txt', 'r') as f:
        n = int(f.readline())
        a = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            a.append(row)

    rm = [max(r) for r in a]
    cm = [min(a[i][j] for i in range(n)) for j in range(n)]

    with open('vivod.txt', 'w') as f:
        f.write(' '.join(map(str, rm)) + '\n')
        f.write(' '.join(map(str, cm)))


def task6_2():
    with open('vvod.txt', 'r') as f:
        n = int(f.readline())
        a = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            a.append(row)

    mx = a[0][0]
    mxi = mxj = 0
    for i in range(n):
        if a[i][i] > mx:
            mx = a[i][i]
            mxi = mxj = i
        if a[i][n - 1 - i] > mx:
            mx = a[i][n - 1 - i]
            mxi, mxj = i, n - 1 - i

    c = n // 2
    a[mxi][mxj], a[c][c] = a[c][c], a[mxi][mxj]

    with open('vivod.txt', 'w') as f:
        for r in a:
            f.write(' '.join(map(str, r)) + '\n')


def task7_1():
    with open('vvod.txt', 'r') as f:
        n = int(f.readline())
        sz = n * (n + 1) // 2
        arr = list(map(int, f.readline().split()))

    a = [[0] * n for _ in range(n)]
    idx = 0
    for i in range(n):
        for j in range(i, n):
            a[i][j] = arr[idx]
            a[j][i] = arr[idx]
            idx += 1

    with open('vivod.txt', 'w') as f:
        for r in a:
            f.write(' '.join(map(str, r)) + '\n')


def task7_2():
    with open('vvod.txt', 'r') as f:
        n = int(f.readline())
        a = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            a.append(row)

    d = [a[i][i] for i in range(n)]
    t = sum(d)

    for i in range(n):
        if i % 2 == 0:
            for j in range(n):
                a[i][j] /= t

    with open('vivod.txt', 'w') as f:
        f.write(str(t) + '\n')
        for r in a:
            f.write(' '.join(map(str, r)) + '\n')


def task8_1():
    with open('vvod.txt', 'r') as f:
        n = int(f.readline())
        k = int(f.readline())
        a = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            a.append(row)

    d = a[k][k]
    for j in range(n):
        a[k][j] /= d

    with open('vivod.txt', 'w') as f:
        for r in a:
            f.write(' '.join(map(str, r)) + '\n')


def task8_2():
    with open('vvod.txt', 'r') as f:
        n = int(f.readline())
        a = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            a.append(row)

    for i in range(n):
        for j in range(i + 1, n):
            a[i][j], a[j][i] = a[j][i], a[i][j]

    with open('vivod.txt', 'w') as f:
        for r in a:
            f.write(' '.join(map(str, r)) + '\n')


def task9_1():
    with open('vvod.txt', 'r') as f:
        n = int(f.readline())
        k = int(f.readline())
        a = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            a.append(row)

    mx = -10 ** 9
    cnt = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] % k == 0:
                cnt += 1
                if a[i][j] > mx:
                    mx = a[i][j]

    with open('vivod.txt', 'w') as f:
        f.write(f"{cnt} {mx}")


def task9_2():
    with open('vvod.txt', 'r') as f:
        n = int(f.readline())
        a = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            a.append(row)

    mx = abs(a[0][0])
    mxi = mxj = 0
    for i in range(n):
        for j in range(n):
            if abs(a[i][j]) > mx:
                mx = abs(a[i][j])
                mxi, mxj = i, j

    b = [[0] * (n - 1) for _ in range(n - 1)]
    bi = 0
    for i in range(n):
        if i == mxi:
            continue
        bj = 0
        for j in range(n):
            if j == mxj:
                continue
            b[bi][bj] = a[i][j]
            bj += 1
        bi += 1

    with open('vivod.txt', 'w') as f:
        for r in b:
            f.write(' '.join(map(str, r)) + '\n')


def task10_1():
    with open('vvod.txt', 'r') as f:
        n, m = map(int, f.readline().split())
        a = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            a.append(row)

    mx = -10 ** 9
    for i in range(n):
        inc = all(a[i][j] <= a[i][j + 1] for j in range(m - 1))
        dec = all(a[i][j] >= a[i][j + 1] for j in range(m - 1))
        if inc or dec:
            rm = max(a[i])
            if rm > mx:
                mx = rm

    with open('vivod.txt', 'w') as f:
        f.write(str(mx))


def task10_2():
    with open('vvod.txt', 'r') as f:
        n, m = map(int, f.readline().split())
        k = int(f.readline())
        d = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            d.append(row)

    c = list(range(m))
    c.sort(key=lambda j: d[k][j])

    for i in range(n):
        d[i] = [d[i][j] for j in c]

    with open('vivod.txt', 'w') as f:
        for r in d:
            f.write(' '.join(map(str, r)) + '\n')


def task11_1():
    with open('vvod.txt', 'r') as f:
        n = int(f.readline())
        a = []
        for _ in range(n):
            row = list(map(float, f.readline().split()))
            a.append(row)

    mn = a[0][0]
    mni = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] < mn:
                mn = a[i][j]
                mni = i

    with open('vivod.txt', 'w') as f:
        f.write(str(sum(a[mni])))


def task11_2():
    with open('vvod.txt', 'r') as f:
        n, m = map(int, f.readline().split())
        a = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            a.append(row)

    mp = 10 ** 9
    mj = -1
    for j in range(m):
        if all(abs(a[i][j]) <= 10 for i in range(n)):
            p = 1
            for i in range(n):
                p *= a[i][j]
            if p < mp:
                mp = p
                mj = j

    if mj > 0:
        for i in range(n):
            a[i][mj], a[i][mj - 1] = a[i][mj - 1], a[i][mj]

    with open('vivod.txt', 'w') as f:
        for r in a:
            f.write(' '.join(map(str, r)) + '\n')


def task12_1():
    with open('vvod.txt', 'r') as f:
        n = int(f.readline())
        a = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            a.append(row)

    with open('vivod.txt', 'w') as f:
        for k in range(n):
            if all(a[k][j] == a[j][k] for j in range(n)):
                f.write(str(k) + ' ')


def task12_2():
    with open('vvod.txt', 'r') as f:
        n, m = map(int, f.readline().split())
        a = []
        for _ in range(n):
            row = list(map(float, f.readline().split()))
            a.append(row)

    l = a[-1]
    for i in range(n - 1):
        for j in range(m):
            a[i][j] -= l[j]

    with open('vivod.txt', 'w') as f:
        for r in a:
            f.write(' '.join(map(str, r)) + '\n')


def task13_1():
    with open('vvod.txt', 'r') as f:
        n, m = map(int, f.readline().split())
        a = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            a.append(row)

    with open('vivod.txt', 'w') as f:
        for i in range(0, n, 2):
            f.write(str(min(a[i])) + ' ')


def task13_2():
    with open('vvod.txt', 'r') as f:
        n, m = map(int, f.readline().split())
        a = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            a.append(row)

    mn = mx = a[0][0]
    mni = mnj = mxi = mxj = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] < mn:
                mn = a[i][j]
                mni, mnj = i, j
            if a[i][j] > mx:
                mx = a[i][j]
                mxi, mxj = i, j

    a[mni][mnj], a[mxi][mxj] = a[mxi][mxj], a[mni][mnj]

    with open('vivod.txt', 'w') as f:
        for r in a:
            f.write(' '.join(map(str, r)) + '\n')


def task14_1():
    with open('vvod.txt', 'r') as f:
        n = int(f.readline())
        m = int(f.readline())
        a = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            a.append(row)

    mx = a[0][0]
    mxi = 0
    for i in range(n):
        if a[i][i] > mx:
            mx = a[i][i]
            mxi = i

    a[mxi], a[m] = a[m], a[mxi]

    with open('vivod.txt', 'w') as f:
        for r in a:
            f.write(' '.join(map(str, r)) + '\n')


def task14_2():
    with open('vvod.txt', 'r') as f:
        n = int(f.readline())

    a = [[0] * n for _ in range(n)]
    num = 1
    l, r, t, b = 0, n - 1, 0, n - 1

    while l <= r and t <= b:
        for j in range(l, r + 1):
            a[t][j] = num
            num += 1
        for i in range(t + 1, b + 1):
            a[i][r] = num
            num += 1
        if t < b:
            for j in range(r - 1, l - 1, -1):
                a[b][j] = num
                num += 1
        if l < r:
            for i in range(b - 1, t, -1):
                a[i][l] = num
                num += 1
        l += 1
        r -= 1
        t += 1
        b -= 1

    with open('vivod.txt', 'w') as f:
        for r in a:
            f.write(' '.join(map(str, r)) + '\n')


def task15_1():
    with open('vvod.txt', 'r') as f:
        n, m = map(int, f.readline().split())
        c = int(f.readline())
        d = int(f.readline())
        r = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            r.append(row)

    for i in range(n):
        if any(r[i][j] == c for j in range(m)):
            for j in range(m):
                r[i][j] *= d

    with open('vivod.txt', 'w') as f:
        for rw in r:
            f.write(' '.join(map(str, rw)) + '\n')


def task15_2():
    with open('vvod.txt', 'r') as f:
        n, m = map(int, f.readline().split())
        a = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            a.append(row)

    ms = -1
    mr = -1
    for i in range(n):
        if all(a[i][j] % 2 != 0 for j in range(m)):
            rs = sum(abs(a[i][j]) for j in range(m))
            if rs > ms:
                ms = rs
                mr = i

    with open('vivod.txt', 'w') as f:
        f.write(str(mr))


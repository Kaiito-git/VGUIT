def task1_1():
    count = int(input())
    numbers = []
    for _ in range(count):
        row = list(map(int, input().split()))
        numbers.append(row)

    total = 0
    k = 0
    for i in range(count):
        for j in range(i + 1, count):
            if numbers[i][j] > 0:
                total += numbers[i][j]
                k += 1
    print(total)
    print(k)

def task1_2():
    count = int(input())
    m = int(input())
    numbers = []
    for _ in range(count):
        row = list(map(int, input().split()))
        numbers.append(row)

    for i in range(count):
        row_max = max(numbers[i])
        row_min = min(numbers[i])
        idx_max = numbers[i].index(row_max)
        idx_min = numbers[i].index(row_min)
        numbers[i][0], numbers[i][idx_max] = numbers[i][idx_max], numbers[i][0]
        numbers[i][-1], numbers[i][idx_min] = numbers[i][idx_min], numbers[i][-1]

    for row in numbers:
        print(*row)

def task2_1():
    count = int(input())
    numbers = []
    for _ in range(count):
        row = list(map(int, input().split()))
        numbers.append(row)

    row_sum = sum(numbers[0])
    flag = True

    for i in range(count):
        if sum(numbers[i]) != row_sum:
            flag = False
            break

    for j in range(count):
        col_sum = 0
        for i in range(count):
            col_sum += numbers[i][j]
        if col_sum != row_sum:
            flag = False
            break

    print(flag)

def task2_2():
    count = int(input())
    numbers = []
    for _ in range(count):
        row = list(map(int, input().split()))
        numbers.append(row)

    for i in range(count):
        numbers[i][0], numbers[i][-1] = numbers[i][-1], numbers[i][0]

    for row in numbers:
        print(*row)

def task3_1():
    count = int(input())
    numbers = []
    for _ in range(count):
        row = list(map(int, input().split()))
        numbers.append(row)

    flag = True
    for i in range(count):
        for j in range(i + 1, count):
            if numbers[i][j] != numbers[j][i]:
                flag = False
                break
        if not flag:
            break
    print(flag)

def task3_2():
    count = int(input())
    m = int(input())
    numbers = []
    for _ in range(count):
        row = list(map(float, input().split()))
        numbers.append(row)

    mx = numbers[0][0]
    im = 0
    jm = 0
    for i in range(count):
        for j in range(m):
            if numbers[i][j] > mx:
                mx = numbers[i][j]
                im = i
                jm = j

    numbers[0], numbers[im] = numbers[im], numbers[0]
    for i in range(count):
        numbers[i][0], numbers[i][jm] = numbers[i][jm], numbers[i][0]

    for row in numbers:
        print(*row)

def task4_1():
    count = int(input())
    m = int(input())
    numbers = []
    for _ in range(count):
        row = list(map(int, input().split()))
        numbers.append(row)

    row_sums = [sum(row) for row in numbers]
    idx_max = row_sums.index(max(row_sums))
    idx_min = row_sums.index(min(row_sums))

    print(*numbers[idx_max])
    print(row_sums[idx_max])
    print(*numbers[idx_min])
    print(row_sums[idx_min])

def task4_2():
    count = int(input())
    numbers = []
    for _ in range(count):
        row = list(map(int, input().split()))
        numbers.append(row)

    for i in range(count):
        for j in range(count):
            if numbers[i][j] < 0:
                numbers[i][j] = 0
            elif numbers[i][j] > 0:
                numbers[i][j] = 1

    for i in range(count):
        for j in range(i + 1):
            print(numbers[i][j], end=' ')
        print()

def task5_1():
    count = int(input())
    m = int(input())
    numbers = []
    for _ in range(count):
        row = list(map(int, input().split()))
        numbers.append(row)

    for i in range(count):
        numbers[i].sort()

    for row in numbers:
        print(*row)

def task5_2():
    count = int(input())
    m = int(input())
    numbers = []
    for _ in range(count):
        row = list(map(float, input().split()))
        numbers.append(row)

    for i in range(count):
        row_min = min(numbers[i])
        idx = numbers[i].index(row_min)
        if row_min % 2 == 0:
            numbers[i][idx] = 0
        else:
            numbers[i][idx] = 1

    for row in numbers:
        print(*row)

def task6_1():
    count = int(input())
    numbers = []
    for _ in range(count):
        row = list(map(int, input().split()))
        numbers.append(row)

    row_max = [max(row) for row in numbers]
    col_min = []
    for j in range(count):
        col = [numbers[i][j] for i in range(count)]
        col_min.append(min(col))

    print(*row_max)
    print(*col_min)

def task6_2():
    count = int(input())
    numbers = []
    for _ in range(count):
        row = list(map(float, input().split()))
        numbers.append(row)

    mx = numbers[0][0]
    im = 0
    jm = 0
    for i in range(count):
        if numbers[i][i] > mx:
            mx = numbers[i][i]
            im = i
            jm = i
        if numbers[i][count - 1 - i] > mx:
            mx = numbers[i][count - 1 - i]
            im = i
            jm = count - 1 - i

    center = count // 2
    numbers[im][jm], numbers[center][center] = numbers[center][center], numbers[im][jm]

    for row in numbers:
        print(*row)

def task7_1():
    count = int(input())
    numbers = list(map(int, input().split()))

    a = [[0] * count for _ in range(count)]
    k = 0
    for i in range(count):
        for j in range(i, count):
            a[i][j] = numbers[k]
            a[j][i] = numbers[k]
            k += 1

    for row in a:
        print(*row)

def task7_2():
    count = int(input())
    numbers = []
    for _ in range(count):
        row = list(map(float, input().split()))
        numbers.append(row)

    diag = [numbers[i][i] for i in range(count)]
    total = sum(diag)

    for i in range(count):
        if i % 2 == 1:
            for j in range(count):
                numbers[i][j] /= total

    for row in numbers:
        print(*row)

def task8_1():
    count = int(input())
    numbers = []
    for _ in range(count):
        row = list(map(float, input().split()))
        numbers.append(row)
    k = int(input())

    d = numbers[k][k]
    for j in range(count):
        numbers[k][j] /= d

    for row in numbers:
        print(*row)

def task8_2():
    count = int(input())
    numbers = []
    for _ in range(count):
        row = list(map(int, input().split()))
        numbers.append(row)

    b = [[0] * count for _ in range(count)]
    for i in range(count):
        for j in range(count):
            b[j][i] = numbers[i][j]

    for row in b:
        print(*row)

def task9_1():
    count = int(input())
    numbers = []
    for _ in range(count):
        row = list(map(int, input().split()))
        numbers.append(row)
    k = int(input())

    mx = -10**9
    c = 0
    for i in range(count):
        for j in range(count):
            if numbers[i][j] % k == 0:
                c += 1
                if numbers[i][j] > mx:
                    mx = numbers[i][j]

    print(c)
    print(mx)

def task9_2():
    count = int(input())
    numbers = []
    for _ in range(count):
        row = list(map(float, input().split()))
        numbers.append(row)

    mx = abs(numbers[0][0])
    im = 0
    jm = 0
    for i in range(count):
        for j in range(count):
            if abs(numbers[i][j]) > mx:
                mx = abs(numbers[i][j])
                im = i
                jm = j

    b = []
    for i in range(count):
        if i == im:
            continue
        row = []
        for j in range(count):
            if j == jm:
                continue
            row.append(numbers[i][j])
        b.append(row)

    for row in b:
        print(*row)

def task10_1():
    count = int(input())
    m = int(input())
    numbers = []
    for _ in range(count):
        row = list(map(int, input().split()))
        numbers.append(row)

    mx = -10**9
    for i in range(count):
        inc = True
        dec = True
        for j in range(1, m):
            if numbers[i][j] < numbers[i][j - 1]:
                inc = False
            if numbers[i][j] > numbers[i][j - 1]:
                dec = False
        if inc or dec:
            cur_max = max(numbers[i])
            if cur_max > mx:
                mx = cur_max
    print(mx)

def task10_2():
    count = int(input())
    m = int(input())
    numbers = []
    for _ in range(count):
        row = list(map(int, input().split()))
        numbers.append(row)
    k = int(input())

    for i in range(m):
        for j in range(i + 1, m):
            if numbers[k][i] > numbers[k][j]:
                for t in range(count):
                    numbers[t][i], numbers[t][j] = numbers[t][j], numbers[t][i]

    for row in numbers:
        print(*row)

def task11_1():
    count = int(input())
    numbers = []
    for _ in range(count):
        row = list(map(float, input().split()))
        numbers.append(row)

    mn = numbers[0][0]
    im = 0
    for i in range(count):
        for j in range(count):
            if numbers[i][j] < mn:
                mn = numbers[i][j]
                im = i

    s = sum(numbers[im])
    print(s)

def task11_2():
    count = int(input())
    m = int(input())
    numbers = []
    for _ in range(count):
        row = list(map(int, input().split()))
        numbers.append(row)

    best_prod = 10**9
    best_col = -1
    for j in range(m):
        flag = True
        prod = 1
        for i in range(count):
            if abs(numbers[i][j]) > 10:
                flag = False
                break
            prod *= numbers[i][j]
        if flag and prod < best_prod:
            best_prod = prod
            best_col = j

    if best_col > 0:
        for i in range(count):
            numbers[i][best_col], numbers[i][best_col - 1] = numbers[i][best_col - 1], numbers[i][best_col]

    for row in numbers:
        print(*row)

def task12_1():
    count = int(input())
    numbers = []
    for _ in range(count):
        row = list(map(int, input().split()))
        numbers.append(row)

    for k in range(count):
        flag = True
        for i in range(count):
            if numbers[k][i] != numbers[i][k]:
                flag = False
                break
        if flag:
            print(k)

def task12_2():
    count = int(input())
    m = int(input())
    numbers = []
    for _ in range(count):
        row = list(map(float, input().split()))
        numbers.append(row)

    for i in range(count - 1):
        for j in range(m):
            numbers[i][j] -= numbers[-1][j]

    for row in numbers:
        print(*row)

def task13_1():
    count = int(input())
    m = int(input())
    numbers = []
    for _ in range(count):
        row = list(map(int, input().split()))
        numbers.append(row)

    for i in range(0, count, 2):
        print(min(numbers[i]))

def task13_2():
    count = int(input())
    m = int(input())
    numbers = []
    for _ in range(count):
        row = list(map(int, input().split()))
        numbers.append(row)

    mx = numbers[0][0]
    imx = 0
    jmx = 0
    mn = numbers[0][0]
    imn = 0
    jmn = 0
    for i in range(count):
        for j in range(m):
            if numbers[i][j] > mx:
                mx = numbers[i][j]
                imx = i
                jmx = j
            if numbers[i][j] < mn:
                mn = numbers[i][j]
                imn = i
                jmn = j

    numbers[imx][jmx], numbers[imn][jmn] = numbers[imn][jmn], numbers[imx][jmx]

    for row in numbers:
        print(*row)

def task14_1():
    count = int(input())
    numbers = []
    for _ in range(count):
        row = list(map(int, input().split()))
        numbers.append(row)
    m = int(input())

    md = numbers[0][0]
    im = 0
    for i in range(count):
        if numbers[i][i] > md:
            md = numbers[i][i]
            im = i

    numbers[im], numbers[m] = numbers[m], numbers[im]

    for row in numbers:
        print(*row)

def task14_2():
    count = int(input())
    numbers = [[0] * count for _ in range(count)]

    i, j = 0, 0
    di, dj = 0, 1
    for k in range(1, count * count + 1):
        numbers[i][j] = k
        if (i + di < 0 or i + di >= count or
            j + dj < 0 or j + dj >= count or
            numbers[i + di][j + dj] != 0):
            di, dj = dj, -di
        i += di
        j += dj

    for row in numbers:
        print(*row)

def task15_1():
    count = int(input())
    m = int(input())
    numbers = []
    for _ in range(count):
        row = list(map(int, input().split()))
        numbers.append(row)
    c = int(input())
    d = int(input())

    for i in range(count):
        if c in numbers[i]:
            for j in range(m):
                numbers[i][j] *= d

    for row in numbers:
        print(*row)

def task15_2():
    count = int(input())
    m = int(input())
    numbers = []
    for _ in range(count):
        row = list(map(int, input().split()))
        numbers.append(row)

    best_sum = -1
    best_row = -1
    for i in range(count):
        flag = True
        s = 0
        for j in range(m):
            if numbers[i][j] % 2 == 0:
                flag = False
                break
            s += abs(numbers[i][j])
        if flag and s > best_sum:
            best_sum = s
            best_row = i

    if best_row != -1:
        print(*numbers[best_row])
    else:
        print(-1)

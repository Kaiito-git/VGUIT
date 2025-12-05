import math

def triangle_area(side1, side2, side3):
    half_perimeter = (side1 + side2 + side3) / 2
    return math.sqrt(half_perimeter * (half_perimeter - side1) *
                     (half_perimeter - side2) * (half_perimeter - side3))

def task1_1():
    a, b = float(input()), float(input())
    c, d = float(input()), float(input())
    e, count = float(input()), float(input())
    print(a * b)
    print(0.5 * c * d)
    print(math.pi * e * e)

def task1_2():
    for _ in range(3):
        count = int(input())
        numbers = [int(input()) for _ in range(count)]
        sum_numbers = sum(numbers)
        print(sum_numbers, sum_numbers / count)

def triangle_area2(side1, side2, side3):
    half_perimeter = (side1 + side2 + side3) / 2
    return math.sqrt(half_perimeter * (half_perimeter - side1) *
                     (half_perimeter - side2) * (half_perimeter - side3))

def task2_1():
    count = float(input())
    print(6 * triangle_area2(count, count, count))

def task2_2():
    for _ in range(3):
        a, b = float(input()), float(input())
        print(a * b)

def hypotenuse(cathet1, cathet2):
    return math.sqrt(cathet1 * cathet1 + cathet2 * cathet2)

def task3_1():
    a, b = float(input()), float(input())
    c, d = float(input()), float(input())
    x = hypotenuse(a, b)
    y = hypotenuse(c, d)
    print(x, y)
    print(1 if x > y else 2)

def task3_2():
    numbers = input().split()
    for word in numbers:
        print(''.join(sorted(word)), end=' ')
    print()

def gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1

def task4_1():
    a, b, c, d = int(input()), int(input()), int(input()), int(input())
    x = a * d
    y = b * c
    g = gcd(x, y)
    print(x // g, y // g)

def inside_circle(x, y, center_x, center_y, radius):
    return (x - center_x) ** 2 + (y - center_y) ** 2 < radius * radius

def task4_2():
    a, b, r = float(input()), float(input()), float(input())
    count = 0
    for _ in range(3):
        x, y = float(input()), float(input())
        if inside_circle(x, y, a, b, r):
            count += 1
    print(count)

def task5_1():
    a, b, c, d = int(input()), int(input()), int(input()), int(input())
    x = a * d - b * c
    y = b * d
    g = gcd(x, y)
    print(x // g, y // g)

def task5_2():
    count = int(input())
    for i in range(1, count + 1):
        if count % i == 0:
            print(i, end=' ')
    print()

def task6_1():
    a, b = int(input()), int(input())
    x, y = a, b
    while b:
        a, b = b, a % b
    print(a, x * y // a)

def two_triangles(a, b, c, d, e):
    p1 = (a + b + e) / 2
    p2 = (c + d + e) / 2
    return (math.sqrt(p1 * (p1 - a) * (p1 - b) * (p1 - e)) +
            math.sqrt(p2 * (p2 - c) * (p2 - d) * (p2 - e)))

def task6_2():
    a, b, c, d, e = (float(input()), float(input()),
                     float(input()), float(input()), float(input()))
    print(two_triangles(a, b, c, d, e))

def right_triangle_area(cathet1, cathet2):
    return 0.5 * cathet1 * cathet2

def rectangle_area(side1, side2):
    return side1 * side2

def task7_1():
    a, b, c, d = float(input()), float(input()), float(input()), float(input())
    print(right_triangle_area(a, b) + rectangle_area(c, d))

def task7_2():
    count = int(input())
    print(f"{count:010o}")

def good_number(n):
    t = n
    while t:
        d = t % 10
        if d == 0 or n % d != 0:
            return False
        t //= 10
    return True

def task8_1():
    count = int(input())
    for i in range(1, count + 1):
        if good_number(i):
            print(i)

def swap_edges(numbers):
    if len(numbers) > 1:
        numbers[0], numbers[-1] = numbers[-1], numbers[0]

def task8_2():
    count = int(input())
    numbers = [int(input()) for _ in range(count)]
    swap_edges(numbers)
    print(numbers)

def digit_sum(n):
    return sum(int(d) for d in str(n))

def task9_1():
    count = int(input())
    steps = 0
    while count > 0:
        count -= digit_sum(count)
        steps += 1
    print(steps)

def task9_2():
    for _ in range(3):
        count = int(input())
        numbers = [int(input()) for _ in range(count)]
        product = 1
        for x in numbers:
            product *= x
        print(product, sum(numbers) / count)

def allowed_digits(n, a, b, c):
    digits_set = set(str(n))
    return digits_set.issubset({str(a), str(b), str(c)})

def task10_1():
    n, a, b, c = int(input()), int(input()), int(input()), int(input())
    count = 0
    for i in range(100, n + 1):
        if allowed_digits(i, a, b, c):
            count += 1
    print(count)

def task10_2():
    numbers = input().split()
    print(' '.join(numbers[::-1]))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def task11_1():
    count = int(input())
    for i in range(count, 2 * count - 1):
        if is_prime(i) and is_prime(i + 2):
            print(i, i + 2)

def matrix_max(matrix):
    return max(max(row) for row in matrix)

def task11_2():
    a = [[int(input()) for _ in range(2)] for _ in range(2)]
    b = [[int(input()) for _ in range(2)] for _ in range(2)]
    x = matrix_max(a)
    y = matrix_max(b)
    for i in range(2):
        for j in range(2):
            if a[i][j] == x:
                a[i][j] = y
            if b[i][j] == y:
                b[i][j] = x
    print(a)
    print(b)

def sum_divisors(n):
    return sum(i for i in range(1, n) if n % i == 0)

def task12_1():
    count = int(input())
    for i in range(1, count + 1):
        j = sum_divisors(i)
        if j > i and sum_divisors(j) == i:
            print(i, j)

def median(a, b, c):
    return 0.5 * math.sqrt(2 * b * b + 2 * c * c - a * a)

def task12_2():
    a, b, c = float(input()), float(input()), float(input())
    ma = median(a, b, c)
    mb = median(b, a, c)
    mc = median(c, a, b)
    mma = median(ma, mb, mc)
    mmb = median(mb, ma, mc)
    mmc = median(mc, ma, mb)
    print(mma, mmb, mmc)

def armstrong(n):
    digits = [int(x) for x in str(n)]
    power = len(digits)
    return sum(x ** power for x in digits) == n

def task13_1():
    count = int(input())
    for i in range(1, count + 1):
        if armstrong(i):
            print(i)

def angle(x, y):
    return math.atan2(y, x)

def task13_2():
    points = []
    for _ in range(3):
        x, y = float(input()), float(input())
        points.append((x, y, angle(x, y)))
    best = min(points, key=lambda t: abs(t[2]))
    print(best[0], best[1])

def divisors_count(n):
    return sum(1 for i in range(1, n + 1) if n % i == 0)

def task14_1():
    m, n = int(input()), int(input())
    max_count = 0
    result = []
    for i in range(m, n + 1):
        c = divisors_count(i)
        if c > max_count:
            max_count = c
            result = [i]
        elif c == max_count:
            result.append(i)
    print(result)

def distance2(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def task14_2():
    points = []
    for _ in range(4):
        x, y = float(input()), float(input())
        points.append((x, y))
    max_dist = 0
    pair = None
    for i in range(4):
        for j in range(i + 1, 4):
            d = distance2(points[i][0], points[i][1],
                          points[j][0], points[j][1])
            if d > max_dist:
                max_dist = d
                pair = (i, j)
    print(max_dist, pair)

def is_palindrome(s):
    return s == s[::-1]

def task15_1():
    count = int(input())
    for i in range(2, count + 1):
        if is_prime(i) and is_palindrome(bin(i)[2:]):
            print(i)

def distance3(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1) ** 2 +
                     (y2 - y1) ** 2 +
                     (z2 - z1) ** 2)

def task15_2():
    points = []
    for _ in range(4):
        x, y, z = float(input()), float(input()), float(input())
        points.append((x, y, z))
    min_dist = float('inf')
    pair = None
    for i in range(4):
        for j in range(i + 1, 4):
            d = distance3(points[i][0], points[i][1], points[i][2],
                          points[j][0], points[j][1], points[j][2])
            if d < min_dist:
                min_dist = d
                pair = (i, j)
    print(min_dist, pair)

def main():
    f = {
        (1, 1): task1_1, (1, 2): task1_2,
        (2, 1): task2_1, (2, 2): task2_2,
        (3, 1): task3_1, (3, 2): task3_2,
        (4, 1): task4_1, (4, 2): task4_2,
        (5, 1): task5_1, (5, 2): task5_2,
        (6, 1): task6_1, (6, 2): task6_2,
        (7, 1): task7_1, (7, 2): task7_2,
        (8, 1): task8_1, (8, 2): task8_2,
        (9, 1): task9_1, (9, 2): task9_2,
        (10, 1): task10_1, (10, 2): task10_2,
        (11, 1): task11_1, (11, 2): task11_2,
        (12, 1): task12_1, (12, 2): task12_2,
        (13, 1): task13_1, (13, 2): task13_2,
        (14, 1): task14_1, (14, 2): task14_2,
        (15, 1): task15_1, (15, 2): task15_2
    }

    while True:
        c = input()
        if c == 'q':
            break
        try:
            v, z = map(int, c.split())
            f[(v, z)]()
        except:
            pass

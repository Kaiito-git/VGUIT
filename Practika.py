print("№1")
N = int(input("Введите целое число N: "))
i = 1
print("Квадраты натуральных чисел, не превосходящие", N, ":")
while i * i <= N:
    print(i * i, end=' ')
    i += 1
print("\n")


print("№2")
n = int(input("Введите целое число (не меньше 2): "))
divisor = 2
while n % divisor != 0:
    divisor += 1
print("Наименьший натуральный делитель:", divisor)


print("№3")
N = int(input("Введите натуральное число N: "))
power = 1
exponent = 0
while power * 2 <= N:
    power *= 2
    exponent += 1
print(f"Показатель степени: {exponent}, Степень: {power}")


print("№4")
x = float(input("Введите начальный пробег x: "))
y = float(input("Введите целевой пробег y: "))
day = 1
distance = x
while distance < y:
    distance += distance * 0.1
    day += 1
print(f"Номер дня, когда пробег составит не менее {y} км: {day}")


print("№5")
print("Вводите последовательность целых неотрицательных чисел (0 для завершения):")
count = 0
num = int(input("Введите число: "))
while num != 0:
    count += 1
    num = int(input("Введите число: "))
print(f"Количество членов последовательности: {count}")


print("№6")
print("Вводите последовательность чисел (0 для завершения):")
total = 0
count = 0
num = int(input("Введите число: "))
while num != 0:
    total += num
    count += 1
    num = int(input("Введите число: "))
if count > 0:
    print(f"Среднее значение: {total / count:.2f}")
else:
    print("Среднее значение: 0")


print("№7")
print("Вводите последовательность натуральных чисел (0 для завершения):")
count_greater = 0
prev = int(input("Введите число: "))
if prev == 0:
    print("Количество элементов больше предыдущего: 0")
else:
    num = int(input("Введите число: "))
    while num != 0:
        if num > prev:
            count_greater += 1
        prev = num
        num = int(input("Введите число: "))
    print(f"Количество элементов больше предыдущего: {count_greater}")


print("№8")
print("Вводите последовательность натуральных чисел (0 для завершения):")
max_count = 1
current_count = 1

prev = int(input("Введите число: "))
if prev == 0:
    print("Наибольшее число подряд идущих одинаковых элементов: 0")
else:
    num = int(input("Введите число: "))
    while num != 0:
        if num == prev:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 1
        prev = num
        num = int(input("Введите число: "))

    print(f"Наибольшее число подряд идущих одинаковых элементов: {max_count}")

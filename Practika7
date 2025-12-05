def task1_1():
    count = int(input())
    numbers = []
    for _ in range(count):
        numbers.append(int(input()))
    maximum = max(numbers)
    print(maximum)
    print(numbers[::-1])

def task1_2():
    count = int(input())
    numbers = []
    for _ in range(count):
        numbers.append(float(input()))
    average = sum(numbers) / len(numbers)
    for j in range(len(numbers)):
        if numbers[j] == 0:
            numbers[j] = average
    print(numbers)

def task2_1():
    count = int(input())
    numbers = []
    for _ in range(count):
        numbers.append(int(input()))
    minimum = min(numbers)
    pos = numbers.index(minimum)
    print(pos)

def task2_2():
    count = int(input())
    numbers = []
    for _ in range(count):
        numbers.append(int(input()))
    positives = [num for num in numbers if num > 0]
    non_positives = [num for num in numbers if num <= 0]
    print(positives)
    print(non_positives)

def task3_1():
    count = int(input())
    numbers = []
    for _ in range(count):
        numbers.append(float(input()))
    total = 0
    for k in range(1, len(numbers), 2):
        total += numbers[k]
    print(numbers)
    print(total)

def task3_2():
    numbers = []
    for _ in range(8):
        numbers.append(int(input()))
    for idx in range(len(numbers)):
        if numbers[idx] < 15:
            numbers[idx] *= 2
    print(numbers)

def task4_1():
    count = int(input())
    numbers = []
    for _ in range(count):
        numbers.append(int(input()))
    max_val = max(numbers)
    max_pos = numbers.index(max_val)
    print(max_val)
    print(max_pos + 1)

def task4_2():
    count = int(input())
    numbers = []
    for _ in range(count):
        numbers.append(int(input()))
    odds = [val for val in numbers if val % 2 != 0]
    if not odds:
        print("нет")
    else:
        odds.sort(reverse=True)
        print(odds)

def task5_1():
    numbers = []
    for _ in range(10):
        numbers.append(int(input()))
    for idx in range(len(numbers) - 1):
        if numbers[idx] < 0 and numbers[idx + 1] < 0:
            print(numbers[idx], numbers[idx + 1])

def task5_2():
    numbers = []
    for _ in range(10):
        numbers.append(int(input()))
    uniques = []
    for item in numbers:
        if item not in uniques:
            uniques.append(item)
    print(uniques)

def task6_1():
    numbers = []
    for _ in range(10):
        numbers.append(int(input()))
    mean_val = sum(numbers) / len(numbers)
    max_value = max(numbers)
    below_max_count = sum(1 for val in numbers if val < max_value)
    above_mean_count = sum(1 for val in numbers if val > mean_val)
    print(below_max_count)
    print(above_mean_count)

def task6_2():
    numbers = []
    for _ in range(10):
        numbers.append(int(input()))
    total_above_5 = sum(val for val in numbers if val > 5)
    print(total_above_5)

def task7_1():
    count = int(input())
    numbers = []
    for _ in range(count):
        numbers.append(int(input()))
    even_sum = 0
    odd_product = 1
    for pos in range(len(numbers)):
        if pos % 2 == 0:
            even_sum += numbers[pos]
        else:
            odd_product *= numbers[pos]
    print(even_sum)
    print(odd_product)

def task7_2():
    count = int(input())
    numbers = []
    for _ in range(count):
        numbers.append(int(input()))
    min_idx = numbers.index(min(numbers))
    max_idx = numbers.index(max(numbers))
    numbers[min_idx], numbers[max_idx] = numbers[max_idx], numbers[min_idx]
    print(numbers)

def task8_1():
    count = int(input())
    numbers = []
    for _ in range(count):
        numbers.append(int(input()))
    array_sum = sum(numbers)
    array_prod = 1
    for num in numbers:
        array_prod *= num
    print(array_sum)
    print(array_prod)

def task8_2():
    count = int(input())
    numbers = []
    for _ in range(count):
        numbers.append(float(input()))
    mean_value = sum(numbers) / len(numbers)
    for pos in range(len(numbers)):
        if numbers[pos] == 0:
            numbers[pos] = mean_value
    print(numbers)

def task9_1():
    count = int(input())
    numbers = []
    for _ in range(count):
        numbers.append(float(input()))
    min_abs = min(numbers, key=abs)
    print(min_abs)
    print(numbers[::-1])

def task9_2():
    numbers1 = []
    numbers2 = []
    for _ in range(10):
        numbers1.append(float(input()))
    for _ in range(10):
        numbers2.append(float(input()))
    numbers1, numbers2 = numbers2, numbers1
    print(numbers1)
    print(numbers2)

def task10_1():
    count = int(input())
    numbers = []
    for _ in range(count):
        numbers.append(int(input()))
    duplicates = []
    seen = set()
    for num in numbers:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        seen.add(num)
    if duplicates:
        print(duplicates)
    else:
        print("нет")

def task10_2():
    numbers = []
    for _ in range(15):
        numbers.append(int(input()))
    print(numbers)
    for pos in range(len(numbers)):
        if numbers[pos] < 10:
            numbers[pos] = 0
        elif numbers[pos] > 20:
            numbers[pos] = 1
    print(numbers)

def task11_1():
    count = int(input())
    numbers = []
    for _ in range(count):
        numbers.append(int(input()))
    even_nums = [num for num in numbers if num % 2 == 0]
    if even_nums:
        print(max(even_nums))
    else:
        print("нет")

def task11_2():
    count = int(input())
    numbers = []
    for _ in range(count):
        numbers.append(int(input()))
    small_evens = [num for num in numbers if num % 2 == 0 and num < 10]
    if not small_evens:
        print("нет")
    else:
        small_evens.sort()
        print(small_evens)

def task12_1():
    count = int(input())
    numbers = []
    for _ in range(count):
        numbers.append(int(input()))
    odd_numbers = [num for num in numbers if num % 2 != 0]
    if odd_numbers:
        print(min(odd_numbers))
    else:
        print("нет")

def task12_2():
    numbers1 = []
    numbers2 = []
    for _ in range(10):
        numbers1.append(float(input()))
    for _ in range(10):
        numbers2.append(float(input()))
    numbers1, numbers2 = numbers2, numbers1
    print(numbers1)
    print(numbers2)

def task13_1():
    count = int(input())
    numbers = []
    for _ in range(count):
        numbers.append(int(input()))
    positions_dict = {}
    for idx, value in enumerate(numbers):
        if numbers.count(value) > 1:
            if value not in positions_dict:
                positions_dict[value] = []
            positions_dict[value].append(idx)
    if positions_dict:
        for key, pos_list in positions_dict.items():
            print(key, pos_list)
    else:
        print("нет")

def task13_2():
    numbers = []
    for _ in range(8):
        numbers.append(int(input()))
    for idx in range(len(numbers)):
        if numbers[idx] < 15:
            numbers[idx] *= 2
    print(numbers)

def task14_1():
    count = int(input())
    numbers = []
    for _ in range(count):
        numbers.append(float(input()))
    min_pos = numbers.index(min(numbers))
    max_pos = numbers.index(max(numbers))
    numbers[min_pos], numbers[max_pos] = numbers[max_pos], numbers[min_pos]
    print(numbers)

def task14_2():
    numbers = []
    for _ in range(10):
        numbers.append(int(input()))
    avg_val = sum(numbers) / len(numbers)
    for idx in range(len(numbers)):
        if numbers[idx] > avg_val:
            numbers[idx] = 1
    print(numbers)

def task15_1():
    count = int(input())
    numbers = []
    for _ in range(count):
        numbers.append(int(input()))
    repeats = []
    tracked = set()
    for item in numbers:
        if item in tracked and item not in repeats:
            repeats.append(item)
        tracked.add(item)
    if repeats:
        print(repeats)

def task15_2():
    count = int(input())
    numbers = []
    for _ in range(count):
        numbers.append(int(input()))
    odd_vals = [val for val in numbers if val % 2 != 0]
    if not odd_vals:
        print("нет")
    else:
        odd_vals.sort(reverse=True)
        print(odd_vals)

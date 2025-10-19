print("№1")
text1 = input("Введите русскоязычный текст: ")
words1 = text1.split()
count_e = 0
for word in words1:
    if word.strip('.,!?;:"').lower().startswith('е'):
        count_e += 1
print(f"Количество слов, начинающихся с 'е': {count_e}")


print("№2")
text2 = input("Введите строку с двоеточиями: ")
replace_count2 = text2.count(':')
new_text2 = text2.replace(':', '%')
print(f"Результат замены: {new_text2}")
print(f"Количество замен: {replace_count2}")


print("№3")
text3 = input("Введите строку с точками: ")
delete_count3 = text3.count('.')
new_text3 = text3.replace('.', '')
print(f"Результат после удаления точек: {new_text3}")
print(f"Количество удаленных точек: {delete_count3}")


print("№4")
text4 = input("Введите строку: ")
replace_count4 = text4.count('а')
new_text4 = text4.replace('а', 'о')
print(f"Результат замены 'а' на 'о': {new_text4}")
print(f"Количество замен: {replace_count4}")
print(f"Количество символов в строке: {len(text4)}")


print("№5")
text5 = input("Введите строку с заглавными буквами: ")
new_text5 = text5.lower()
print(f"Результат: {new_text5}")


print("№6")
text6 = input("Введите строку: ")
delete_count6 = text6.count('а')
new_text6 = text6.replace('а', '')
print(f"Результат после удаления 'а': {new_text6}")
print(f"Количество удаленных 'а': {delete_count6}")


print("№7")
text7 = input("Введите строку: ")
n = len(text7)
half_length = n // 2
first_half = text7[:half_length]
second_half = text7[half_length:]
modified_first_half = first_half.replace('п', '*')
new_text7 = modified_first_half + second_half
print(f"Результат: {new_text7}")


print("№8")
text8 = input("Введите строку, заканчивающуюся точкой: ")
if text8.endswith('.'):
    text8 = text8[:-1]
words8 = text8.split()
print(f"Количество слов в строке: {len(words8)}")


print("№9")
text9 = input("Введите текст: ")
search_word = input("Введите слово для поиска: ")
words9 = text9.split()
count_word = 0
for word in words9:
    if word.strip('.,!?;:"').lower() == search_word.lower():
        count_word += 1
print(f"Слово '{search_word}' встречается {count_word} раз(а)")


print("№10")
text10 = input("Введите предложение на английском языке: ")
words10 = text10.split()
capitalized_words = []
for word in words10:
    if word:
        capitalized_words.append(word[0].upper() + word[1:].lower())
new_text10 = ' '.join(capitalized_words)
print(f"Результат: {new_text10}")


print("№11")
text11 = input("Введите строку: ")
max_n_sequence = 0
current_sequence = 0
for char in text11:
    if char.lower() == 'н':
        current_sequence += 1
        max_n_sequence = max(max_n_sequence, current_sequence)
    else:
        current_sequence = 0
new_text11 = text11.replace('!', '.')
print(f"Самая длинная последовательность 'н': {max_n_sequence}")
print(f"Результат замены '!' на '.': {new_text11}")


print("№12")
text12 = input("Введите строку: ")
words12 = text12.split()
words_ending_with_ya = []
for word in words12:
    cleaned_word = word.strip('.,!?;:"')
    if cleaned_word.lower().endswith('я'):
        words_ending_with_ya.append(cleaned_word)
print("Слова, оканчивающиеся на 'я':", ', '.join(words_ending_with_ya))


print("№13")
text13 = input("Введите строку с одной парой скобок: ")
start_index = text13.find('(')
end_index = text13.find(')')
if start_index != -1 and end_index != -1 and start_index < end_index:
    inside_brackets = text13[start_index + 1:end_index]
    print(f"Символы внутри скобок: {inside_brackets}")
else:
    print("Скобки не найдены или расположены некорректно")


print("№14")
text14 = input("Введите строку: ")
words14 = text14.split()
words_starting_with_a = []
words_ending_with_ya = []
for word in words14:
    cleaned_word = word.strip('.,!?;:"')
    if cleaned_word.lower().startswith('а'):
        words_starting_with_a.append(cleaned_word)
    if cleaned_word.lower().endswith('я'):
        words_ending_with_ya.append(cleaned_word)
print("Слова, начинающиеся на 'а':", ', '.join(words_starting_with_a))
print("Слова, оканчивающиеся на 'я':", ', '.join(words_ending_with_ya))


print("№15")
text15 = input("Введите строку текста: ")
count_t = text15.lower().count('т')
print(f"Количество букв 'т' в строке: {count_t}")

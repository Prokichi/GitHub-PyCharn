number = input('Введите четырехзначное число: ')
if len(number) != 4 or not number.isdigit():
    print('Неверно. Введите четырехзначное число')
else:
    result = 1
for digit in number:
    result *= int(digit)
print(result)

meters = float(input('Введите количество метров'))
centimeter = meters * 100
decimeters = meters * 10
millimeters = meters * 1000
mile = meters / 1609.34
if meters == 1:
    print(f"{meters} метре ")
    print(f"{centimeter} сантиметров ")
    print(f"{decimeters} дециметров ")
    print(f"{millimeters} миллиметров ")
    print(f"{mile} миль ")
else:
    print(f"{meters} метрах ")
    print(f"{centimeter} сантиметров ")
    print(f"{decimeters} дециметров ")
    print(f"{millimeters} миллиметров ")
    print(f"{mile} миль ")

    import random

    size = 20
    list1 = [random.randint(1, 20) for _ in range(size)]
    list2 = [random.randint(1, 20) for _ in range(size)]

    combined = list1 + list2

    unique_list = list(set(combined))

    common_elements = list(set(list1) & set(list2))

    unique1 = list(set(list1))
    unique2 = list(set(list2))
    unique_elements = unique1 + unique2

    min_max_list1 = [min(list1), max(list1)]
    min_max_list2 = [min(list2), max(list2)]
    min_max_combined = min_max_list1 + min_max_list2

    print("Список 1:", list1)
    print("Список 2:", list2)
    print("Элементы из обоих списков:", combined)
    print("Элементы без повторений:", unique_list)
    print("Общие элементы:", common_elements)
    print("Уникальные элементы из каждого списка:", unique_elements)
    print("Минимальное и максимальное значение мз списков:", min_max_combined)
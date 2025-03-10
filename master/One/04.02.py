"""Задание 1
Два списка целых заполняются случайными числами.
Необходимо:
■ Сформировать третий список, содержащий элементы
обоих списков;
■ Сформировать третий список, содержащий элементы
обоих списков без повторений;
■ Сформировать третий список, содержащий элементы
общие для двух списков;
■ Сформировать третий список, содержащий только
уникальные элементы каждого из списков;
■ Сформировать третий список, содержащий только
минимальное и максимальное значение каждого из
списков."""

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
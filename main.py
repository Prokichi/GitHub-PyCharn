number = input('Введите четырехзначное число: ')
if len(number) != 4 or not number.isdigit():
    print('Неверно. Введите четырехзначное число')
else:
    result = 1
for digit in number:
    result *= int(digit)
print(result)'''

'''meters = float(input('Введите количество метров'))
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
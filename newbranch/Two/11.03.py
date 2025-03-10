"""Задание 1
Создать базовый класс Фигура с методом для подсчета
площади. Создать производные классы: прямоугольник,
круг, прямоугольный треугольник, трапеция со своими
методами для подсчета площади.
Задание 2
Для классов из задания 1 нужно переопределить магические методы int(возвращает площадь) и str(возвращает
информацию о фигуре)"""

'''
import math

class Figure:
    def area(self):
        raise NotImplementedError

    def __int__(self):
        return int(self.area())

    def __str__(self):
        return "Фигура"

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __int__(self):
        return int(self.area())

    def __str__(self):
        return f"Прямоугольник: ширина = {self.width}, высота = {self.height}, площадь = {self.area()}"

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def __int__(self):
        return int(self.area())

    def __str__(self):
        return f"Круг: радиус = {self.radius}, площадь = {self.area()}"

class RightTriangle(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __int__(self):
        return int(self.area())

    def __str__(self):
        return f"Прямоугольный треугольник: основание = {self.base}, высота = {self.height}, площадь = {self.area()}"

class Trapezoid(Figure):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

    def __int__(self):
        return int(self.area())

    def __str__(self):
        return f"Трапеция: основание 1 = {self.base1}, основание 2 = {self.base2}, высота = {self.height}, площадь = {self.area()}"
    '''

"""Задание 3
Создайте базовый класс Shape для рисования плоских
фигур.
Определите методы:
■ Show() — вывод на экран информации о фигуре;
■ Save() — сохранение фигуры в файл;
■ Load() — считывание фигуры из файла.
1
Определите производные классы:
■ Square — квадрат, который характеризуется координатами левого верхнего угла и длиной стороны;
■ Rectangle — прямоугольник с заданными координатами верхнего левого угла и размерами;
■ Circle — окружность с заданными координатами центра и радиусом;
■ Ellipse — эллипс с заданными координатами верхнего
угла описанного вокруг него прямоугольника со сторонами, параллельными осям координат, и размерами
этого прямоугольника.
Создайте список фигур, сохраните фигуры в файл,
загрузите в другой список и отобразите информацию о
каждой из фигур."""

'''import pickle

class Shape:

    def __init__(self):
        pass

    def show(self):

        print("Это абстрактная фигура.")

    def save(self, filename):

        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
            print(f"Фигура сохранена в файл: {filename}")
        except Exception as e:
            print(f"Ошибка при сохранении в файл: {e}")

    def load(self, filename):

        try:
            with open(filename, 'rb') as f:
                loaded_shape = pickle.load(f)
            print(f"Фигура загружена из файла: {filename}")
            return loaded_shape
        except FileNotFoundError:
            print(f"Файл не найден: {filename}")
            return None
        except Exception as e:
            print(f"Ошибка при загрузке из файла: {e}")
            return None


class Square(Shape):

    def __init__(self, x, y, side):
        super().__init__()
        self.x = x
        self.y = y
        self.side = side

    def show(self):
        print(f"Квадрат: Левый верхний угол ({self.x}, {self.y}), Сторона = {self.side}")


class Rectangle(Shape):

    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        print(f"Прямоугольник: Левый верхний угол ({self.x}, {self.y}), Ширина = {self.width}, Высота = {self.height}")


class Circle(Shape):

    def __init__(self, center_x, center_y, radius):
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def show(self):
        print(f"Окружность: Центр ({self.center_x}, {self.center_y}), Радиус = {self.radius}")


class Ellipse(Shape):

    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        print(f"Эллипс: Описанный прямоугольник - Левый верхний угол ({self.x}, {self.y}), Ширина = {self.width}, Высота = {self.height}")


shapes = [
    Square(10, 20, 30),
    Rectangle(5, 5, 20, 10),
    Circle(0, 0, 5),
    Ellipse(100, 100, 50, 25)
]

filename = "shapes.dat"
try:
    with open(filename, 'wb') as f:
        pickle.dump(shapes, f)
    print(f"Список фигур сохранен в файл: {filename}")
except Exception as e:
    print(f"Ошибка при сохранении списка фигур в файл: {e}")

loaded_shapes = []
try:
    with open(filename, 'rb') as f:
        loaded_shapes = pickle.load(f)
    print(f"Список фигур загружен из файла: {filename}")
except FileNotFoundError:
    print(f"Файл не найден: {filename}")
except Exception as e:
    print(f"Ошибка при загрузке списка фигур из файла: {e}")

if loaded_shapes:
    print("\nИнформация о загруженных фигурах:")
    for shape in loaded_shapes:
        shape.show()
else:
    print("Список загруженных фигур пуст.")'''

def longest_line_lenght(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = f.readlines()
        max1 = max(map(len, data))
        for line in data:
            if len(line.strip()) == max1:
                print(line)
                break
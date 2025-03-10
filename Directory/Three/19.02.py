'''Задание 1
Реализуйтекласс«Автомобиль». Необходимохранить
в полях класса: название модели, год (выпуска, производителя,
объемдвигателя, цветмашины,цену.Реализуйте)
методы класса для ввода данных, вывода данных, реализуйте
доступ котдельнымполямчерезметодыкласса.'''

'''class Car:
    def __init__(self, model="", year=0, manufacturer="", engine_volume=0.0, color="", price=0.0):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def input_data(self):
        self.model = input("Введите название модели: ")
        self.year = int(input("Введите год выпуска: "))
        self.manufacturer = input("Введите производителя: ")
        self.engine_volume = float(input("Введите объем двигателя (л): "))
        self.color = input("Введите цвет машины: ")
        self.price = float(input("Введите цену: "))

    def display_data(self):
        print(f"Модель: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Производитель: {self.manufacturer}")
        print(f"Объем двигателя: {self.engine_volume} л")
        print(f"Цвет: {self.color}")
        print(f"Цена: {self.price} у.е.")

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_manufacturer(self):
        return self.manufacturer

    def get_engine_volume(self):
        return self.engine_volume

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price'''

'''Задание 2
Реализуйте класс «Книга». Необходимо хранить в 
полях класса: название книги, год выпуска, издателя, 
жанр, автора, цену. Реализуйте методы класса для ввода 
данных, выводаданных,реализуйтедоступкотдельным 
полям через методы класса'''

'''class Book:
    def __init__(self, title="", year=0, publisher="", genre="", author="", price=0.0):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def input_data(self):
        self.title = input("Введите название книги: ")
        self.year = int(input("Введите год выпуска: "))
        self.publisher = input("Введите издателя: ")
        self.genre = input("Введите жанр: ")
        self.author = input("Введите автора: ")
        self.price = float(input("Введите цену: "))

    def display_data(self):
        print(f"Название: {self.title}")
        print(f"Год выпуска: {self.year}")
        print(f"Издатель: {self.publisher}")
        print(f"Жанр: {self.genre}")
        print(f"Автор: {self.author}")
        print(f"Цена: {self.price}")

    def get_title(self):
        return self.title
    def get_year(self):
        return self.year
    def get_publisher(self):
        return self.publisher
    def get_genre(self):
        return self.genre
    def get_author(self):
        return self.author
    def get_price(self):
        return self.price'''
'''Задание 3
Реализуйте класс «Стадион». Необходимо хранить в 
полях класса: название стадиона, дату открытия, страну, 
город, вместимость. Реализуйте методыклассадляввода 
данных, выводаданных,реализуйтедоступкотдельным 
полям через методы класса.'''

'''class Stadium:
    def __init__(self, name="", opening_date="", country="", city="", capacity=0):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def input_data(self):
        self.name = input("Введите название стадиона: ")
        self.opening_date = input("Введите дату открытия (дд.мм.гггг): ")
        self.country = input("Введите страну: ")
        self.city = input("Введите город: ")
        self.capacity = int(input("Введите вместимость: "))

    def display_data(self):
        print(f"Название стадиона: {self.name}")
        print(f"Дата открытия: {self.opening_date}")
        print(f"Страна: {self.country}")
        print(f"Город: {self.city}")
        print(f"Вместимость: {self.capacity}")

    def get_name(self):
        return self.name

    def get_opening_date(self):
        return self.opening_date

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city

    def get_capacity(self):
        return self.capacity'''

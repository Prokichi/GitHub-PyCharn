'''Задание 1
 Дано два текстовых файла. Выяснить, совпадают ли
их строки. Если нет, то вывести несовпадающую строку
из каждого файла.'''
'''def compare_files(file1, file2):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        lines1, lines2 = f1.readlines(), f2.readlines()
        for l1, l2 in zip(lines1, lines2):
            if l1.strip() != l2.strip():
                print(l1, l2)'''

'''Задание 2
Дан текстовый файл.Необходимо создать новый файл 
и записать в него следующую статистику по исходному 
файлу:
 ■ Количество символов;
 ■ Количество строк;
 ■ Количество гласных букв;
 ■ Количество согласных букв;
 ■ Количество цифр.'''
'''def file_statistics(file, output_file):
    vowels = 'аеёиоуыюяАЕЁИОУЫЭЮЯaeiouAEIOU'
    consonants = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩbcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
        stats = {
            'Количество символов': len(text) - text.count('\n'),
            'Количество строк': text.count('\n') + 1,
            'Количество гласных букв': sum(1 for ch in text if ch in vowels),
            'Количество согласных букв': sum(1 for ch in text if ch in consonants),
            'Количество цифр': sum(1 for ch in text if ch.isdigit())
        }
    with open(output_file, 'w', encoding='utf-8') as out:
        for key, value in stats.items():
            out.write(f"{key}: {value}\n")'''

''' Задание 3
 Дан текстовый файл. Удалить из него последнюю 
строку. Результат записать в другой файл.'''

'''def remove_last_line(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(lines[:-1])'''

'''Задание 4
 Дан текстовый файл. Найти длину самой длинной 
строки.'''

'''def longest_line_lenght(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = f.readlines()
        max1 = max(map(len, data))
        for line in data:
            if len(line.strip()) == max1:
                print(line)
                break'''

'''Задание 5
 Дан текстовый файл. Посчитать сколько раз в нем 
встречается заданное пользователем слово.'''

'''def count_word_occurrences(file, word):
    with open(file, 'r', encoding='utf-8') as f:
        return sum(line.lower().split().count(word.lower()) for line in f)'''

''' Задание 6
 Дан текстовый файл. Найти изаменить в немзадан
ное слово. Что искать и на что заменять определяется 
пользователем.'''

'''def replace_word_in_file(file, search_word, replace_word):
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    with open(file, 'w', encoding='utf-8') as f:
        f.write(text.replace(search_word, replace_word))'''
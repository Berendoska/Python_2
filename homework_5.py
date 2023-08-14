import os

''' 
Задача 1
Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.'''

def create_tulpe(path_file: str):
    path, name = os.path.split(path_file)
    name, ext = os.path.splitext(name)
    return path, name, ext

print(create_tulpe("C:\ProgramFiles\Sem_5\\homework_5.py"))

'''Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате
получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается
как ставка умноженная на процент премии'''

names = ["Kate", "Dima", "Helen"]
salaries = [5000, 1000000, 11]
bonus = ["5.25%", "1.25%", "3.25%"]

result = {n: (float(b[:-1]) * s) for n, b, s in zip(names, bonus, salaries)}

print(result)

''' Задача 3
Создайте функцию генератор чисел Фибоначчи (см. Википедию).'''

def fib(n: int):
    x1, x2 = 1, 1
   
    for _ in range(n):
        print(x1, end=' ')
        x1, x2 = x2, x1 + x2

fib(9)

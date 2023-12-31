"""Задание
Напишите функцию группового переименования файлов. Она должна:
✔ принимать параметр желаемое конечное имя файлов.
+ При переименовании в конце имени добавляется порядковый номер.
✔ принимать параметр количество цифр в порядковом номере.
✔ принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
✔ принимать параметр расширение конечного файла.
✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
[3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

"""

import os

__all__ = ['rename_file_group']

def rename_file_group(last_filename: str, amount_num: int, first_ext: str, final_ext: str, rng: list[int]) -> None:
    count = 1
    for file in os.listdir('./'):
        if file.endswith(first_ext):
            start, end = rng
            filename = file.split('.')[0][start:end] + last_filename + str(count).zfill(amount_num)
            count += 1
            os.rename(file, f'{filename}.{final_ext}')


if __name__ == '__main__':
    rename_file_group('test', 2, 'txt', 'docs', [3, 6])
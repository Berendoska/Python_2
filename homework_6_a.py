"""
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

"""
from homework_6 import check_date

def input_date()->str:
    date=input('Введите дату в формате DD.MM.YYYY: ')
    return date

if __name__=="__main__":
    print(check_date(input_date()))
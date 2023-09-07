"""
Добавьте к ним логирование ошибок и полезной информации. Также реализуйте возможность запуска из
командной строки с передачей параметров.
на примере  сравнение, умножение, сложение двух матриц
"""

import logging




logging.basicConfig(filename='Log.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{asctime} {levelname:<8} функция "{funcName}()" строка {lineno:>3d} : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

class MatrixApp:

    def __init__(self, matrix: list):
            """Конструктор
            класса.Инициализирует
            матрицу."""
            self.matrix = matrix

    def print_matrix(self):
        """Вывод матриц на печать."""
        for row in self.matrix:
            print(" ".join(str(element) for element in row))

    def __eq__(self, other: 'MatrixApp') -> bool:
        """Сравнение матриц."""
        logger.info(f' РАВЕНСТВО:  {self.matrix} = {other.matrix} ')
        return self.matrix == other.matrix

    def __add__(self, other):
        """Сложение матриц."""
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
                logger.error(f'Не возможно выполнить сложение матриц, размерности матриц несовместимы:  [{len(self.matrix)}][{len(self.matrix[0])}] !=  [{len(other.matrix)}][{len(other.matrix[0])}]')
                #raise ValFormatError
        result_matrix = [
            [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
            for i in range(len(self.matrix))
        ]
        logger.info(f' СЛОЖЕНИЕ:  {self.matrix} + {other.matrix} = {result_matrix}  ')
        return MatrixApp(result_matrix)

    def __mul__(self, other):
        """Умножение матриц."""
        if len(self.matrix[0]) != len(other.matrix):
            logger.error(f'Не возможно выполнить умножение матриц, размерности матриц несовместимы: [{len(self.matrix)}][{len(self.matrix[0])}] !=  [{len(other.matrix)}][{len(other.matrix[0])}]')
        result_matrix = [
            [sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(other.matrix)))
                for j in range(len(other.matrix[0]))]
            for i in range(len(self.matrix))
        ]
        logger.info(f' УМНОЖЕНИЕ:  {self.matrix} * {self.matrix} = {result_matrix}  ')
        return MatrixApp(result_matrix)

    @staticmethod
    def print_docstring():
        """Вывод документации класса на печать."""
        print(MatrixApp.__doc__)


if __name__ == '__main__':
    MatrixApp.print_docstring()

    # matrix1 = MatrixApp([[1, 2, 3], [3, 4, 3]])
    matrix1 = MatrixApp([[1, 2], [3, 4]])
    matrix2 = MatrixApp([[1, 2], [3, 4]])
   

    print("Матрица 1:")
    matrix1.print_matrix()

    print("Матрица 2:")
    matrix2.print_matrix()

    if matrix1 == matrix2:
        print("Матрицы равны.")
    else:
        print("Матрицы не равны.")

    result_sum = matrix1 + matrix2
    print("Сумма матриц:")
    result_sum.print_matrix()

    result_mul = matrix1 * matrix2
    print("Произведение матриц:")
    result_mul.print_matrix()
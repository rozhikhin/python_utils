"""
Модуль содержит класс для работы с файлами
"""
import tempfile
import os


class File:
    """
    Класс содержит методы для работы с файлами
    При создании экземпляра класса нужно передать путь к фпайлу.
    В классе переопределн метод сложения. При сложении двух классов данного типа
    создается класс такого же типа, которому передается путь к файлу, содержащему суммарное содержимое файлов
    двух слагаемых классов.
    Также реализован итератор по строкам файла
    """

    def __init__(self, path_file):
        """
        :param path_file: - Путь к файлу
        """
        self.path_file = path_file
        self.counter = 0

    def write(self, s):
        """
        :param s: - Строка, которую необходимо записать в файл
        :return: None
        """
        with open(self.path_file, 'w') as f:
            f.write(s)

    def read(self):
        with open(self.path_file, 'r') as f:
            return f.read()

    def __add__(self, other):
        """

        :param other: - экзепляр этого класса, с которым нужно сложить такой же экземпляр этого же класса
        :return: None
        """
        result_file = os.path.join(tempfile.gettempdir(), 'result_content.txt')
        with open(result_file, 'w') as f:
            f.write(self.read() + other.read())
        return File(result_file)

    def __str__(self):
        return self.path_file

    def __iter__(self):
        return self

    def __next__(self):
        """
        Итератор
        :return: Nono
        """
        with open(self.path_file) as f:
            lines = f.readlines()
            if self.counter >= len(lines):
                raise StopIteration

            line = lines[self.counter]
            self.counter += 1
            return line


if __name__ == '__main__':

    file1 = File('1.txt')
    file2 = File('2.txt')
    file3 = file1 + file2

    print(file3)

    for i in file3:
        print(i)

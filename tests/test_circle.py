import unittest #импортировала библиотеку для тестов
from circle import area, perimeter #импортировала нужные функции для круга
import math #для числа пи

class TestCircle(unittest.TestCase): #создала класс тестов для круга, который наследуется
#                                     от базового для тестов (для assertEqual и тп)

    def test_area_positive(self): #создала метод-тест от текущего экземпляра класса
        """Проверка площади круга с положительным радиусом"""
        self.assertAlmostEqual(area(1), math.pi) #обращаемся к методу текущего экземпляр класса, вызываем функцию, которая должна возвращать дробное значение, поэтому используем специальное сравнение
        self.assertAlmostEqual(area(2), math.pi * 4)

    def test_area_zero(self): 
        """Проверка площади круга с радиусом 0"""
        self.assertEqual(area(0), 0) #сравнение для целых чисел

    def test_area_negative(self):
        """Проверка, что площадь не может быть отрицательной"""
        with self.assertRaises(ValueError): #контекстный менеджер with создает область, где мы следим, вылезла ли лжидаемая ошибка значения
            area(-1)

    def test_perimeter_positive(self):
        """Проверка периметра круга с положительным радиусом"""
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(perimeter(2), 4 * math.pi)

    def test_perimeter_zero(self):
        """Проверка периметра круга с радиусом 0"""
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_negative(self):
        """Проверка, что периметр не может быть отрицательным"""
        with self.assertRaises(ValueError):
            perimeter(-1)
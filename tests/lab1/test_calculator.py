import unittest
from src.lab1.calculator import calc

class CalculatorTestCase(unittest.TestCase):

    # Тест для проверки работы, можно удалить
    def test_lab1(self):
        self.assertEqual(calc('+',10,43),53.0)
        self.assertEqual(calc('-', 158, 58), 100.0)
        self.assertEqual(calc('/', 24, 0), 'Деление на ноль!')
        self.assertEqual(calc('/', 10, 2), 5.0)
        self.assertEqual(calc('*', 4, 5), 20)
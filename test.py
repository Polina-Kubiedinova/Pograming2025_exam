import unittest
from exam import get_factorial  # Імпортуємо функцію з вашого файлу app.py

class TestFactorial(unittest.TestCase):

   # Тест 1: Перевірка звичайного позитивного числа
   def test_factorial_positive(self):
      # Перевіряємо, що 5! = 120
      self.assertEqual(get_factorial(5), 120)
      # Перевіряємо, що 3! = 6
      self.assertEqual(get_factorial(3), 6)

   # Тест 2: Перевірка граничного значення (нуль)
   def test_factorial_zero(self):
      # За математичним правилом 0! = 1
      self.assertEqual(get_factorial(0), 1)

   # Тест 3: Перевірка генерації виключення при від'ємному числі
   def test_factorial_negative(self):
      # Очікуємо, що виклик get_factorial(-1) підніме помилку ValueError
      with self.assertRaises(ValueError):
            get_factorial(-1)
            
      with self.assertRaises(ValueError):
            get_factorial(-10)

if __name__ == '__main__':
   unittest.main()
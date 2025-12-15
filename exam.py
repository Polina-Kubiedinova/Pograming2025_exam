def get_factorial(n):
   """
   Функція обчислює факторіал числа n.
   Якщо n < 0, генерується виключення ValueError.
   """
   if n < 0:
      raise ValueError("Число n не може бути від'ємним (n < 0).")
   
   if n == 0:
      return 1
      
   result = 1
   for i in range(1, n + 1):
        result *= i
   return result

if __name__ == "__main__":
   try:
         # Отримання даних від користувача
         user_input = input("Введіть ціле число n для обчислення факторіалу: ")
         
         n = int(user_input)
         
         result = get_factorial(n)
         print(f"{n}! = {result}")
         
   except ValueError as e:
         # Обробка виключення (якщо n < 0 або введено не число)
         print(f"Помилка: {e}")
   except Exception as e:
         # Обробка будь-яких інших помилок
         print(f"Виникла неочікувана помилка: {e}")
import time
import pyautogui
import random
import threading
from calculator import keep_calculators_open, distort_screen

def generate_random_expression():
    """Генерирует случайные математические выражения."""
    operators = ['+', '-', '*', '/']
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(operators)
    return f"{num1}{operator}{num2}"

def type_expression(expression):
    """Быстро вводит выражение в калькулятор."""
    for char in expression:
        pyautogui.typewrite(char, interval=0.05)  # Уменьшаем интервал для быстрого ввода
    pyautogui.press("enter")  # Нажимаем Enter для выполнения выражения

def infinite_input():
    """Бесконечный ввод случайных выражений в калькуляторы."""
    while True:
        expression = generate_random_expression()
        print(f"Вводим выражение: {expression}")
        type_expression(expression)  # Вводим выражение в текущий калькулятор
        time.sleep(1)  # Пауза между вводами

def main():
    # Запускаем мониторинг калькуляторов в отдельном потоке
    threading.Thread(target=keep_calculators_open, daemon=True).start()

    # Запускаем "безумие" с экраном в другом потоке
    threading.Thread(target=distort_screen, daemon=True).start()

    # Запускаем ввод значений в калькуляторы
    threading.Thread(target=infinite_input, daemon=True).start()

    # Основной поток ждет, пока остальные потоки не завершатся (но они будут работать вечно)
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()

import subprocess
import pygetwindow as gw
import random
import time
import psutil

def open_calculator():
    """Запускает стандартный калькулятор Windows."""
    try:
        return subprocess.Popen("calc.exe")
    except FileNotFoundError:
        print("Калькулятор не найден. Убедитесь, что используете Windows.")
        exit()

def position_calculators():
    """Располагает окна калькуляторов в разных частях экрана."""
    calc_windows = gw.getWindowsWithTitle("Калькулятор")  # Получаем все окна с названием "Калькулятор"
    
    # Координаты для размещения окон
    positions = [(0, 0), (960, 0), (0, 540), (960, 540)]  # Для 7 окон, распределенных по углам экрана
    
    # Перемещаем только существующие калькуляторы (не больше 7)
    for i, window in enumerate(calc_windows[:7]):  # Проверяем не более 7 окон
        if i < len(positions):  # Проверяем, что есть доступная позиция
            x, y = positions[i]
            window.moveTo(x, y)

def close_extra_calculators():
    """Закрывает все калькуляторы, кроме первых 7 окон."""
    calc_windows = gw.getWindowsWithTitle("Калькулятор")  # Находим все окна с названием "Калькулятор"
    if len(calc_windows) > 7:
        for window in calc_windows[7:]:  # Закрываем лишние окна
            try:
                # Получаем процесс, связанный с окном
                process_name = "Calculator" if "Calculator" in window.title else "Калькулятор"
                for proc in psutil.process_iter(['pid', 'name']):
                    if process_name.lower() in proc.info['name'].lower():
                        proc.terminate()
                        break
            except Exception as e:
                print(f"Не удалось закрыть окно: {e}")

def distort_screen():
    """Искажает размеры и положение окон калькулятора каждые 3 секунды."""
    while True:
        calc_windows = gw.getWindowsWithTitle("Калькулятор")  # Находим окна с названием "Калькулятор"
        for window in calc_windows:
            if window.isMaximized or window.isMinimized:
                continue  # Пропускаем окна, если они свернуты или развернуты на весь экран
            try:
                # Случайные новые размеры и координаты
                new_width = random.randint(200, 600)
                new_height = random.randint(200, 600)
                new_x = random.randint(0, 1920 - new_width)
                new_y = random.randint(0, 1080 - new_height)
                window.resizeTo(new_width, new_height)
                window.moveTo(new_x, new_y)
            except Exception as e:
                print(f"Не удалось изменить окно: {e}")
        time.sleep(3)  # Интервал между искажениями

def keep_calculators_open():
    """Убедитесь, что всегда открыто ровно 7 калькулятора."""
    while True:
        calc_windows = gw.getWindowsWithTitle("Калькулятор")  # Находим окна с названием "Калькулятор"

        # Если меньше 7 окон, открываем недостающие
        while len(calc_windows) < 7:
            open_calculator()
            time.sleep(1)  # Даем время новому калькулятору открыться
            calc_windows = gw.getWindowsWithTitle("Калькулятор")

        # Если больше 7 окон, закрываем лишние
        if len(calc_windows) > 7:
            close_extra_calculators()

        # Располагаем окна в заданных позициях
        position_calculators()

        time.sleep(1)  # Повторяем проверку через секунду

from datetime import datetime

def log_expression(expression):
    """Логирует введенные выражения в файл."""
    with open("calculator_troll.log", "a") as log_file:
        log_file.write(f"[{datetime.now()}] Введено: {expression}\n")

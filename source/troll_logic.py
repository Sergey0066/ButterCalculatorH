import random
import winsound

def troll_result(expression):
    """Смешиваем результат выражения для веселья."""
    result = eval(expression)  # Вычисляем результат
    print(f"Решение для {expression} равно: {result}")
    print(f"Но... на самом деле это {result + random.randint(1, 10)}!")  # Подменяем результат

def play_random_sound():
    """Играем случайный звуковой файл для троллинга."""
    sound_files = ["sound1.wav", "sound2.wav", "sound3.wav"]  # Убедитесь, что такие файлы существуют
    sound = random.choice(sound_files)
    winsound.PlaySound(sound, winsound.SND_FILENAME)

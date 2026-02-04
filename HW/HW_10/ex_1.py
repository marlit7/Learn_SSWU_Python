'''розрахунок площі 2D фігур
журналу реєстрації подій – logging;
документація – docstring;
тестування за технологіями: Docstring Testing;
Unit Test - тестування засобави за власним вибором: Unittest та / або PyTest
'''

'''
1. Ініціалізація імпорту модуля logging
'''
import logging
'''
2. Встановлення параметрів для конфігурування logging

'''

logging.basicConfig(
    level=logging.DEBUG,                                # рівень logging
    filename='rect_events.log',                         # подія буде записуватися в файл rect_events.log
    filemode='a',                                       # додавання інформації до файлу
    format='%(asctime)s - %(levelname)s - %(message)s', # формат інформації logging
    encoding='utf-8'
)


def rectangle_area(width, height):
    """
    Розраховуємо площадь прямокутника.

    Docstring тест:приклади
    >>> rectangle_area(5, 10)
    50.0
    >>> rectangle_area(3.5, 2)
    7.0
    """
    if width < 0 or height < 0:
        logging.error(f"Помилка: Сторони прямокутника повинні бути більше 0 ({width}, {height})")
        raise ValueError("Сторони прямокутника не можуть бути відємні")

    area = float(width * height)
    logging.info(f"Площа прямокутника {width}x{height} = {area}")
    return area


if __name__ == "__main__":
    # Запуск Docstring тестів
    import doctest

    print("Перевірка Docstring тестів...")
    doctest.testmod()
    print("Завершено. Результат в логах.")






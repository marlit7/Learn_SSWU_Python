import pytest
from ex_1 import rectangle_area

# Розрахунок
def test_area_calculation():
    assert rectangle_area(10, 5) == 50.0
    assert rectangle_area(0, 5) == 0.0

# Тестуємо обробку помилок
def test_negative_values():
    with pytest.raises(ValueError):
        rectangle_area(-1, 10)
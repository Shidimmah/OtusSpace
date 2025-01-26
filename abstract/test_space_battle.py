import pytest
from space_battle_movement import SpaceShip, Movement

# Тест 1: Проверка движения корабля
@pytest.mark.parametrize("x, y, vx, vy, expected_x, expected_y", [
    (12, 5, -7, 3, 5, 8)  # Движение из (12,5) со скоростью (-7,3) -> (5,8)
])
def test_movement(x, y, vx, vy, expected_x, expected_y):
    ship = SpaceShip(x, y, vx, vy)
    movement = Movement()
    movement.move(ship)
    assert ship.get_position() == (expected_x, expected_y)

# Тест 2: Ошибка при невозможности прочитать положение
class BrokenPositionShip(SpaceShip):
    def get_position(self):
        raise AttributeError("Невозможно прочитать положение корабля")

def test_broken_position():
    ship = BrokenPositionShip(0, 0, 1, 1)
    movement = Movement()
    with pytest.raises(AttributeError, match="Невозможно прочитать положение корабля"):
        movement.move(ship)

# Тест 3: Ошибка при невозможности прочитать скорость
class BrokenVelocityShip(SpaceShip):
    def get_velocity(self):
        raise AttributeError("Невозможно прочитать скорость")

def test_broken_velocity():
    ship = BrokenVelocityShip(0, 0, 1, 1)
    movement = Movement()
    with pytest.raises(AttributeError, match="Невозможно прочитать скорость"):
        movement.move(ship)

# Тест 4: Ошибка при невозможности изменить положение
class FixedPositionShip(SpaceShip):
    def set_position(self, x, y):
        raise AttributeError("Невозможно изменить положение корабля")

def test_fixed_position():
    ship = FixedPositionShip(0, 0, 1, 1)
    movement = Movement()
    with pytest.raises(AttributeError, match="Невозможно изменить положение корабля"):
        movement.move(ship)

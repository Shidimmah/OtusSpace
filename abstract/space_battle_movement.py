from abc import ABC, abstractmethod
from typing import Tuple


class Movable(ABC):
    # Интерфейс для движущихся объектов.

    @abstractmethod
    def get_position(self) -> Tuple[int, int]:
        pass

    @abstractmethod
    def get_velocity(self) -> Tuple[int, int]:
        pass

    @abstractmethod
    def set_position(self, x: int, y: int):
        pass


class Coords:
    # Класс для хранения координат объекта.

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_position(self) -> Tuple[int, int]:
        return self.x, self.y

    def set_position(self, x: int, y: int):
        self.x = x
        self.y = y


class Movement:
    # Реализация движения объекта

    def move(self, obj: Movable):
        if not hasattr(obj, 'get_position') or not hasattr(obj, 'get_velocity'):
            raise AttributeError("Объект должен реализовывать методы получения позиции и скорости")

        x, y = obj.get_position()
        vx, vy = obj.get_velocity()
        obj.set_position(x + vx, y + vy)


class SpaceShip(Movable):
    # Космический корабль, который может двигаться

    def __init__(self, x: int, y: int, vx: int, vy: int):
        self.coords = Coords(x, y)
        self.vx = vx
        self.vy = vy

    def get_position(self) -> Tuple[int, int]:
        return self.coords.get_position()

    def get_velocity(self) -> Tuple[int, int]:
        return self.vx, self.vy

    def set_position(self, x: int, y: int):
        self.coords.set_position(x, y)

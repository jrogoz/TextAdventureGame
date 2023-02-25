from abc import ABC, abstractmethod


class Monster(ABC):
    _hp = 100
    _isAlive = True

    @abstractmethod
    def __init__(self, strength, armor):
        self._strength = strength
        self._armor = armor
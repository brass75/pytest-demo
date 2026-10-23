from dataclasses import dataclass
from typing import Any


@dataclass
class Point:
    x: int
    y: int

    def __add__(self, other: Any):
        """Add 2 Points together"""
        match other:
            case self.__class__():
                return self.__class__(self.x + other.x, self.y + other.y)
            case _:
                return NotImplemented

    def __sub__(self, other: Any):
        """Subtract one point from another"""
        match other:
            case self.__class__():
                return self.__class__(self.x - other.x, self.y - other.y)
            case _:
                return NotImplemented

    def __hash__(self):
        return hash((self.x, self.y))

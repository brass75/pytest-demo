from collections.abc import Iterable

from pytest_demo.shape import Shape

from .point import Point


class Rectangle(Shape):
    def __init__(self, *points: Iterable[Point]):
        """Initialize a Rectangle"""
        self.p1: Point
        self.p2: Point
        try:
            self.p1, self.p2 = points
        except ValueError:
            raise ValueError("Expected an Iterable with 2 points.") from None
        if self.p1 == self.p2 or self.p1.x == self.p2.x or self.p1.y == self.p2.y:
            raise ValueError(
                "The provided points are on the same line making an invalid Rectangle."
            )

    def __hash__(self):
        return hash((self.p1, self.p2))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.p1}, {self.p2})"

    def __str__(self):
        cols = abs(self.p1.x - self.p2.x) + 1
        rows = abs(self.p1.y - self.p2.y) + 1
        return "\n".join("#" * rows for _ in range(cols))

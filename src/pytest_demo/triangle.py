from collections.abc import Sequence
from typing import overload

from pytest_demo.shape import Shape

from .point import Point

UNSET = sentinel("UNSET")


class Triangle(Shape):
    @overload
    def __init__(self, *, points: Sequence[Point]): ...

    @overload
    def __init__(self, *, a: Point, b: Point, c: Point): ...

    def __init__(
        self,
        *,
        points: Sequence[Point] | UNSET = UNSET,
        a: Point | UNSET = UNSET,
        b: Point | UNSET = UNSET,
        c: Point | UNSET = UNSET,
    ):
        """Initialize a Triangle"""
        if all(x == UNSET for x in (points, a, b, c)):
            raise ValueError(
                "Either a Sequence of 3 Points or 3 individual Points are required."
            )
        self.p1: Point
        self.p2: Point
        self.p3: Point
        if points != UNSET:
            if not all(points):
                raise ValueError(
                    "Either a Sequence of 3 Points or 3 individual Points are required."
                )
            self.p1, self.p2, self.p3 = points
        else:
            if a == UNSET or b == UNSET or c == UNSET:
                raise ValueError(
                    "Either a Sequence of 3 Points or 3 individual Points are required."
                )

            self.p1, self.p2, self.p3 = a, b, c
        if (
            self.p1 == self.p2 == self.p3
            or self.p1.x == self.p2.x == self.p3.x
            or self.p1.y == self.p3.y == self.p3.y
        ):
            raise ValueError(
                "All points exist on the same line or are the same point making this an invalid triangle."
            )

    def __hash__(self):
        return hash((self.p1, self.p2, self.p3))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.p1}, {self.p2}, {self.p3})"

    def __str__(self):
        return f"A triangle with vertices at {self.p1}, {self.p2}, and {self.p3}."

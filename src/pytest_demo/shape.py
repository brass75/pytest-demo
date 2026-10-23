import json
from dataclasses import asdict
from pathlib import Path

from .point import Point


class Shape:
    def __init__(self):
        raise NotImplementedError("Shape should not be instantiated!")

    def asdict(self) -> dict[str, dict[str, int]]:
        """Return serializable dictionary of the shape"""
        return {k: asdict(v) for k, v in self.__dict__.items()}

    @classmethod
    def fromdict(cls, source: dict[str, dict[str, int]]) -> Shape:
        """Initialize the shape from a dictionary"""
        if cls == Shape:
            raise NotImplementedError("Shape should not be instantiated!")
        points: list[Point] = []
        for point in source.values():
            points.append(Point(**point))
        return cls(*points)

    def serialize(self, file: Path) -> None:
        """Write the Shape to a JSON file"""
        file.write_text(json.dumps(self.asdict(), indent=2))

    @classmethod
    def deserialize(cls, file: Path) -> Shape:
        """Desrialize the Shape from a JSON file"""
        return cls.fromdict(json.loads(file.read_text()))

    def __eq__(self, other: object):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return all(value == other.__dict__[key] for key, value in self.__dict__.items())

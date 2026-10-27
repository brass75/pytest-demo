from itertools import pairwise
import pytest
from pytest_demo import Point


def test_point_addition():
    assert Point(1, 1) + Point(2, 2) == Point(3, 3)


@pytest.mark.parametrize(
    "p1, p2, p3",
    [
        (Point(0, 0), Point(1, 1), Point(1, 1)),
        (Point(1, 1), Point(1, 1), Point(2, 2)),
        (Point(-1, -1), Point(1, 1), Point(0, 0)),
        (Point(2, 2), Point(3, 11), Point(5, 13)),
    ],
    ids=["p1", "p2", "p3", "p4"],
)
def test_addition_bunch(p1, p2, p3):
    assert p1 + p2 == p3


def get_points():
    for x, y in pairwise(range(30)):
        yield (Point(x, x), Point(y, y), Point(x - y, x - y))


@pytest.mark.parametrize("p1, p2, p3", get_points())
def test_subtraction(p1, p2, p3):
    assert p1 - p2 == p3


def test_failure():
    assert Point()


def test_pytest_addition_not_point():
    with pytest.raises(TypeError):
        Point(1, 1) + 1


def not_a_test():
    raise RuntimeError("This is not a test")

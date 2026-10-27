from pytest_demo import Rectangle, Point


def test_rect_serialization(temp_dir):
    rect = Rectangle(Point(0, 0), Point(42, 42))
    file = temp_dir / "rect.json"
    rect.serialize(file)
    rect2 = Rectangle.deserialize(file)
    assert rect == rect2

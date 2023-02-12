import lesson_py_test
from triangle.triangle import Triangle


def test_triangle_eq(self, right_triangle):
    first = right_triangle
    assert first.is_right_triangle()


class TestTrianglePtest:

    # def test_triangle_lt(self):
    #     first = Triangle(7, 8, 9)
    #     second = Triangle(9, 10, 11)
    #     assert first < second
    #
    # def test_triangle_right(self, right_triangle):
    #     assert right_triangle.is_right_triangle()

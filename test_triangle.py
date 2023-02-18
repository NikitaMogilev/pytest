from triangle.triangle import Triangle
import pytest


def test_perimetr(create_triangle):
    print("test Perimetr started")
    print(Triangle.perimetr(create_triangle))
    assert Triangle.perimetr(create_triangle) == 21
    print('test Perimetr end')


def test_square(create_triangle):
    print("test Square started")
    print(Triangle.square(create_triangle))
    assert Triangle.square(create_triangle) == pytest.approx(20.333, abs=1e-3)
    print('test Square end')


def test_triangle_eq(create_triangle):
    print('test EQUAL started ')
    second = Triangle(6, 8, 7)
    assert create_triangle == second
    print('test EQUAL finished')


def test_triangle_noteq(create_triangle):
    print('test NOTEQUAL started ')
    second = Triangle(4, 5, 6)
    assert create_triangle != second
    print('test NOTEQUAL finished')


def test_triangle_lt(create_triangle):
    print('test lt started ')
    second = Triangle(15, 15, 15)
    print(Triangle.perimetr(create_triangle))
    print(Triangle.perimetr(second))
    assert Triangle.perimetr(create_triangle) < Triangle.perimetr(second)
    print('test lt finished')


def test_triangle_gt(create_triangle):
    print('test gt started ')
    second = Triangle(3, 4, 5)
    print(Triangle.perimetr(create_triangle))
    print(Triangle.perimetr(second))
    assert Triangle.perimetr(create_triangle) > Triangle.perimetr(second)
    print('test gt finished')


def test_triangle_le(create_triangle):
    print('test LE started ')
    second = Triangle(8, 10, 15)
    print(Triangle.perimetr(create_triangle))
    print(Triangle.perimetr(second))
    assert Triangle.perimetr(create_triangle) < Triangle.perimetr(second)
    print('test LE finished')


def test_triangle_ge(create_triangle):
    print('test GE started ')
    second = Triangle(9, 6, 6)
    print(Triangle.perimetr(create_triangle))
    print(Triangle.perimetr(second))
    assert Triangle.perimetr(create_triangle) >= Triangle.perimetr(second)
    print('test GE finished')


def test_equals(create_triangle):
    print("test equals started")
    second = Triangle(12, 14, 16)
    assert Triangle.equal(create_triangle, second)
    print('test equals end')


@pytest.mark.xfail(reason="TEST will FAIL when hypotenuse input in 1 or 2 pos")
def test_is_right_angled():
    print('test 90C started ')
    second = Triangle(3, 5, 4)
    print(Triangle.is_right_angled(second))
    assert Triangle.is_right_angled(second)
    print('test 90C finished')


def test_is_right_triangle(right_triangle):
    print('test right triangle started ')
    print(Triangle.is_right_triangle(right_triangle))
    assert Triangle.is_right_triangle(right_triangle)
    print('test right triangle finished')


def test_two_sides_eq(rb_triangle):
    assert Triangle.two_sides_eq(rb_triangle)


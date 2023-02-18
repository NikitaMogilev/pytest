from pytest import fixture
from triangle.triangle import Triangle


@fixture()
def create_triangle():
    triangle1 = Triangle(6, 7, 8)
    yield triangle1
    del triangle1


@fixture(autouse=True)
def printer():
    print("\nIt is setup\n")
    yield
    print("\nTeardown\n")


@fixture()
def right_triangle():
    right_tr = Triangle(6, 6, 6)
    yield right_tr
    del right_tr


@fixture(params=[(3, 3, 4), (8, 8, 10), (5, 5, 8)])
def rb_triangle(request):
    rb_tr = Triangle(request.param[0], request.param[1], request.param[2])
    yield rb_tr
    del rb_tr

@fixture()
def right_angle_triangle():
    right_tr = Triangle(3, 4, 5)
    yield right_tr
    del right_tr
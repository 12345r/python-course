"""
File Name: course-exercise
Author: Roee Golan 25/06/2019
Purpose: Python course exercises
"""


def assignments():
    """Main function."""
    # 1
    # 1.1
    a, b, c, d, e = [1, 2, 3, 4, 5]

    # 1.2
    [a], [b], [c], [d], [e] = [[1], [2], [3], [4], [5]]

    # 1. 3
    a, [b, [c, [d, [e]]]] = [1, [2, [3, [4, [5]]]]]

    # 1. 4
    a, _, [b, [c], d, e, _, _] = [1, 0, [2, [3], 4, 5, 0, 0]]

    # 1. 5
    a, b, c, d, e = {1, 2, 3, 4, 5}

    # 2
    # 2.1
    numbers = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    for x, y, z in numbers:
        assert x == 1
        assert y == 2
        assert z == 3

    # 2.2
    numbers = [[1, [2, [3]]], [1, [2, [3]]], [1, [2, [3]]]]
    for x, [y, [z]] in numbers:
        assert x == 1
        assert y == 2
        assert z == 3

    # 2.3
    numbers = [[1], [1], [1], [1], [1]]
    for [x] in numbers:
        assert x == 1

    # 2.4
    numbers = [[1, 2], [1, 2, 3], [1, 2, 3, 4]]
    for x, y, *_ in numbers:
        assert x == 1
        assert y == 2

    # 2.5
    numbers = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
    for [x, y], i in zip(numbers.items(), [2] * len(numbers)):
        assert x**i == y

    # 3
    a = 1
    b = 2
    c = 3

    def f():
        locals() ['a'] = 4
        globals()['a'] = 5
        b = 6
        c = 7

        def g():
            global   b
            nonlocal c
            b = 8
            c = 9
            assert a == 5
            assert b == 8
            assert c == 9
        g()
        assert a == 5
        assert b == 6
        assert c == 9
    f()
    assert a == 5
    assert b == 8
    assert c == 3

    # 4
    a = 1
    if True:
        a = 2
    assert a == 2

    b = 3
    for b in range(10):
        print(b)
    assert b == 9

    c = 4

    class A:
        c = 5

        def f(self):
            return c

    a = A()
    assert c == 4
    assert a.c == 5
    assert a.f() == 4

    # 5
    As = []
    for i in range(5):
        class A:
            x = i

            def f(self):
                return i

            def g(self):
                return self.x

        As.append(A)
    a = As[2]()
    assert a.x == 2
    assert a.f() == 4
    assert a.g() == 2

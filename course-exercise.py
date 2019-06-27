"""
File Name: course-exercise
Author: Roee Golan 25/06/2019
Purpose: Python course exercises
"""


def assignments():
    """Practice assignments."""
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


def conditions():
    """Practice conditions."""
    # 1
    import datetime as dt

    specific_events = {
        'critical': [
            (dt.datetime(2000, 1, 1, 11, 0), 'server crashed'),
            (dt.datetime(2000, 1, 1, 12, 0), 'server crashed')
        ],
        'standard': [
            (dt.datetime(2000, 1, 1, 10, 0), 'server started'),
            (dt.datetime(2000, 1, 1, 11, 1), 'server started'),
            (dt.datetime(2000, 1, 1, 12, 1), 'server started')
        ]
    }

    def report_events(events, since=None, until=None):
        if not events:
            print('no events')
            return

        if 'critical' in events and events['critical']:
            print('critical events:')
            for date, message in events['critical']:
                print(f'  {date} {message}')
        else:
            print('no critical events')

        if since is not None and until is not None:
            print('standard events:')
            if 'standard' in events and events['standard']:
                for date, message in events['standard']:
                    if since <= date <= until:
                        print(f'  {date} {message}')

    report_events(specific_events, since=dt.datetime(2000, 1, 1, 10), until=dt.datetime(2000, 1, 1, 12))

    # 2
    def add_defaults(config=None):
        if config is not None:
            config = {}
        config['host'] = '0.0.0.0'
        config['port'] = 8000
        config['log_path'] = '/tmp/log'
        return config

    # 3
    import os

    def get_permissions(root_permissions, user_permissions):
        return user_permissions if os.getuid() else root_permissions

    # 4
    undefined = object()

    def count_args(x=undefined, y=undefined):
        return (x is not undefined and 1) + (y is not undefined and 1)

    assert count_args() == 0
    assert count_args(1) == 1
    assert count_args(1, 2) == 2

    # 5
    def greet1(name=None):
        return f'Hey, {name or "stranger"}!'

    def greet2(name=None):
        if name is None:
            name = 'stranger'
        return f'Hey, {name}!'

    # The difference is that greet1 chooses the name much more elegantly. However it catches all cases in which name
    # Returns false, such as an empty list, 'False' or '0', and it causes a slightly different behaviour, which in my
    # Opinion is better suited for the given case


def loops():
    """Practice loops."""
    # 1
    for index, char in enumerate(reversed(['a', 'b', 'c']), 1):
        print(char, index)

    # 2.1
    for char1, char2 in zip(['x', 'y', 'z'], reversed(['a', 'b', 'c', 'd', 'e'])):
        print(char1, char2)

    # 2.2
    from itertools import zip_longest
    for char1, [index, char2] in zip_longest(['x', 'y', 'z'], enumerate(['a', 'b', 'c', 'd', 'e'], 1), fillvalue='_'):
        print(char1, char2, index)

    # 3.1
    n = 10
    p = 1
    for i in range(2, n // 2 + 1):
        if n % i is 0:
            p = i
    else:
        p = 1

    # 3.2
    def get_smallest_factor(n):
        for i in range(2, n // 2 + 1):
            if n % i is 0:
                return i

        return 1

    # 4.1
    n = 25
    for i in range(1, 11):
        for j in range(1, 11):
            multiplication = i * j
            if multiplication == n:
                print("X")
                break
            print(f'{multiplication:3}', end=' ')
        else:
            print()
            continue
        break

    # 4.2
    def print_multiplication_table(n):
        for i in range(1, 11):
            for j in range(1, 11):
                multiplication = i * j
                if multiplication == n:
                    print("X")
                    return
                print(f'{multiplication:3}', end=' ')
            print()

    # 5.1
    import pathlib

    def file_sizes():
        return {file.name: file.stat().st_size for file in pathlib.Path.cwd().iterdir() if file.is_file()}

    # 5.2
    def sieve_of_eratosthenes(number):
        return {num for num in range(2, number) if True not in [num % i == 0 for i in range(2, num // 2 + 1)]}

    # 5.3
    def is_prime(number):
        return True not in [number % num == 0 for num in range(2, number // 2 + 1)]

    # 5.4
    def product(*iterables, repeat=1, result=None):
        for tup in map(tuple, iterables * repeat):
            result = [x + [y] for x in (result if result is not None else [[]]) for y in tup]
        return list(map(tuple, result))


def functions():
    """Manage all the function exercises."""
    # 1
    def add_defaults(config=None):
        if config is None:
            config = {}
        config['host'] = '0.0.0.0'
        config['port'] = 8000
        config['log_path'] = '/tmp/log'
        return config

    # 2
    def write_data(path, data, compress=False):
        if isinstance(data, str):
            data = data.encode()
        if compress:
            import zlib
            data = zlib.compress(data)
        with open(path, 'wb') as writer:
            writer.write(data)

    def write_json(path, obj, compress=False):
        import json
        write_data(path, json.dumps(obj), compress)

    def write_pickle(path, obj, compress=False):
        import pickle
        write_data(path, pickle.dumps(obj), compress)

    # 3.1
    def parameters_string(function):
        import inspect
        return f'{function.__name__}{str(inspect.signature(function))}'

    def f():
        pass

    def g(x, y=2, *args, z=3, **kwargs):
        pass

    assert parameters_string(f) == 'f()'
    assert parameters_string(g) == 'g(x, y=2, *args, z=3, **kwargs)'

    # 3.2
    def arguments_string(function, *args, **kwargs):
        import inspect
        sig = inspect.signature(function)
        sig.bind(*args, **kwargs)
        return f'{function.__name__}({", ".join([str(arg) for arg in args])}, ' \
            f'{", ".join([str(key) + "=" + str(value) for key, value in kwargs.items()])})'

    def g(*args, **kwargs):
        pass

    assert arguments_string(f) == 'f()'
    assert arguments_string(g, 1, 2, 3, 4, 5, z=0, a=1, b=2) == 'g(1, 2, 3, 4, 5, z=0, a=1, b=2)'

    # 4.1
    import functools

    def trace(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            print(f"enter {function.__name__}")
            function(*args, **kwargs)
            print(f"leave {function.__name__}")
        return wrapper

    # 4.2
    def trace(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            sig = f'{function.__name__}({", ".join([str(arg) for arg in args])}{", " if kwargs else ""}'
            f'{", ".join([str(key) + "=" + str(value) for key, value in kwargs.items()])}'
            print(f'enter {sig})')
            try:
                result = function(*args, **kwargs)
            except Exception as e:
                import traceback
                result = traceback.format_exc()
            print(f"leave {sig}): {result}")

        return wrapper

    # 4.3
    def trace(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            sig = f'{function.__name__}({", ".join([str(arg) for arg in args])}{", " if kwargs else ""}'
            f'{", ".join([str(key) + "=" + str(value) for key, value in kwargs.items()])}'
            print(f'{wrapper.space * "  "}enter {sig})')
            wrapper.space += 1
            try:
                result = function(*args, **kwargs)
            except Exception as e:
                import traceback
                result = traceback.format_exc()
            wrapper.space -= 1
            print(f"{wrapper.space * '  '}leave {sig}): {result}")
            return result

        wrapper.space = 0
        return wrapper
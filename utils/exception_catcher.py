def exception_catcher(func, *args):
    try:
        func(*args)
    except Exception as e:
        return type(e)


def test_func():
    1 / 0


if __name__ == "__main__":
    exception_catcher(test_func)

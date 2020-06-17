def exception_catcher(func):
    try:
        func()
    except TypeError:
        return True
    except ValueError:
        return True
    except ZeroDivisionError:
        return True
    else:
        return False


def test_func():
    1 / 0


if __name__ == "__main__":
    exception_catcher(test_func)

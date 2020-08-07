
class MagicInt:

    def __init__(self, value):
        self._value = int(value)
        self._hash = 0

    def __hash__(self):
        self._hash += 1
        return self._hash

    def __eq__(self, other):
        return self._value == other._value


assert MagicInt(1) == MagicInt('1')
assert MagicInt(1) != MagicInt(3)

magic_int = MagicInt(1)
assert len(set([magic_int, magic_int, magic_int])) == 3
assert len(set([MagicInt(1), MagicInt(1), MagicInt(1)])) == 1
assert len(set([magic_int, MagicInt(1), MagicInt(1)])) == 2

magic_int = MagicInt(1)
assert len(set([magic_int, MagicInt(1), MagicInt(1)])) == 1
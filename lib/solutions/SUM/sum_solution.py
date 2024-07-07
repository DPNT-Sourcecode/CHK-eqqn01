# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if isinstance(x, int) and isinstance(y, int):
        if 0 <= x <= 100 and 0 <= y <= 100:
            return x + y
        raise ValueError("expecting values between 1 and 100 for x and y")
    raise TypeError("expecting integer values for x and y")

# https://cses.fi/dsa24k/task/3055


def count(a: int, b: int, c: int) -> int:
    if not all(isinstance(x, int) and 1 <= x <= 100 for x in (a, b ,c)):
        raise ValueError('Args must be in range 1 ... 100')

    res = 0
    if a > b:
        res += c // b
    else:
        res += c // a
    return res


if __name__ == '__main__':
    print(count(3, 4, 11))
    print(count(5, 1, 100))
    print(count(2, 3, 1))
    print(count(2, 3, 9))

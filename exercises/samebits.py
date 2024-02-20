# https://cses.fi/dsa24k/task/3054


def count(s: str) -> int:
    if len(s) > 100 or not isinstance(s, str):
        raise ValueError("Input should be string and should not contain more than 100 characters.")

    zeros = len([el for el in s if el == "0"])
    ones = len([el for el in s if el == "1"])

    return min(zeros, ones)

if __name__ == "__main__":
    print(count("01101"))
    print(count("1111"))
    print(count("101111"))
    print(count("00001111"))
    print(count("00000000011111111111111"))

#!/usr/bin/python3


def smaller(x, y):
    result = x if x < y else y
    return result


def main():
    print(smaller(3, 9))


if __name__ == '__main__':
    main()

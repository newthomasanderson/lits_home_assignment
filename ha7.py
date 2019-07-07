#!/usr/bin/env python


import sys


def count_holes(num):

    num_with_holes = {'9': 1, '8': 2, '6': 1, '4': 1, '0': 1}
    return sum([num_with_holes[n] for n in list(num) if n in num_with_holes.keys()])


def main():

    try:
        data = sys.argv
        if len(data) == 2:
            num = data[1]

        else:
            raise ValueError
    except (OSError, ValueError) as e:
        print(e)

    print(count_holes(num))


if __name__ == '__main__':
    main()

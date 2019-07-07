#!/usr/bin/env python


import sys


def check_palindrom(text):

    lst = list(text.replace(' ', '').lower())
    if len(lst) % 2 > 0:
        first_half = lst[:(len(lst) / 2) + 1]
        second_half = lst[-len(lst) / 2:]
        second_half.reverse()
        if first_half == second_half:
            return 'YES'
    else:
        first_half = lst[:(len(lst) / 2)]
        second_half = lst[-len(lst) / 2:]
        second_half.reverse()
        if first_half == second_half:
            return 'YES'

    return 'NO'


def main():

    try:
        data = sys.argv
        if len(data) == 2:
            text = data[1]

        else:
            raise ValueError
    except (OSError, ValueError) as e:
        print(e)

    print(check_palindrom(text))


if __name__ == '__main__':
    main()

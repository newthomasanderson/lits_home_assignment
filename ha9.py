#!/usr/bin/env python


import sys
import random


def magic_numbers(start, end):
    magic_list = []
    lst = list(range(start, end))
    num = start
    for el in lst:
        if el is num:
            magic_list.append(el)
        num += 1
    if magic_list[-1] < 256:
        return '[{},{})'.format(magic_list[0], magic_list[-1] + 2)

    return '[{},{})'.format(magic_list[0], magic_list[-1] + 1)


def main():
    print_generated = False
    try:
        data = sys.argv
        if len(data) == 3:
            start = int(data[1])
            end = int(data[2])
        else:
            start = random.randint(-500, 0)
            end = random.randint(0, 500)
            print_generated = True

        if start > end:
            raise ValueError
        else:
            raise ValueError
    except (OSError, ValueError) as e:
        print(e)

    if not print_generated:
        print('Entered range is from {} to {} with step 1'.format(start, end))
        print('Range values in the set of magic numbers are:\n {}'.format(magic_numbers(start, end)))
    else:
        print('Generated random range is from {} to {} with step 1'.format(start, end))
        print('Range values in the set of magic numbers are:\n {}'.format(magic_numbers(start, end)))


if __name__ == '__main__':
    main()

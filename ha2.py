#!/usr/bin/env python


import math
import sys


def calculate_eq(chi, mu, omega):
    try:
        return (math.exp(-1 * math.pow((chi - mu), 2) / (2 * math.pow(omega, 2)))) \
               / (omega * math.sqrt(2 * math.pi))

    except ArithmeticError as e:
        print(e)


def main():
    try:
        data = sys.argv
        if len(data) == 4:
            chi = float(data[1])
            mu = float(data[2])
            omega = float(data[3])
        else:
            raise ValueError
    except (OSError, ValueError) as e:
        print(e)

    print(calculate_eq(chi, mu, omega))


if __name__ == '__main__':
    main()

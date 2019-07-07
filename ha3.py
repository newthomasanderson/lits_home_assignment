#!/usr/bin/env python


import sys
import string


POSITIONAL_NOTATION_DIGITS = string.digits + string.uppercase


def converter(value, n, m):
    try:
        # Get number presentation
        number = 0
        for digit in value:
            number = len(POSITIONAL_NOTATION_DIGITS[:n]) * number + POSITIONAL_NOTATION_DIGITS[:n].index(digit)
        # Convert number to its digit representation with specified base 'm'
        digits = ''
        if m > 1:
            while number > 0:
                digits = POSITIONAL_NOTATION_DIGITS[:m][number % len(POSITIONAL_NOTATION_DIGITS[:m])] + digits
                number = number // len(POSITIONAL_NOTATION_DIGITS[:m])
        else:
            digits = '0' * number

        return digits

    except Exception as e:
        print(e)


def convert_n_to_m(x, n, m):

    if x and 1 <= n and 1 <= m <= 36:
        if isinstance(x, str) and len(x) > 1 and x[0] != '-':
            if n > 10:
                x = x.upper()
            if bool([e for e in x if e not in POSITIONAL_NOTATION_DIGITS[:n]] == []):
                output = converter(x, n, m)
            else:
                return bool([e for e in x if e not in POSITIONAL_NOTATION_DIGITS[:n]] == [])

        elif isinstance(x, str):
            if n > 10:
                x = x.upper()
            if bool(x in POSITIONAL_NOTATION_DIGITS[:n]):
                output = converter([x], n, m)
            else:
                return bool(x in POSITIONAL_NOTATION_DIGITS[:n])

        elif isinstance(x, int) and x > 0:
            x = str(x)
            if len(x) > 1:
                if n > 10:
                    x = x.upper()
                if bool([e for e in x if e not in POSITIONAL_NOTATION_DIGITS[:n]] == []):
                    output = converter(x, n, m)
                else:
                    return bool([e for e in x if e not in POSITIONAL_NOTATION_DIGITS[:n]] == [])
            else:
                if n > 10:
                    x = x.upper()
                if bool(x in POSITIONAL_NOTATION_DIGITS[:n]):
                    output = converter(x, n, m)
                else:
                    return bool(x in POSITIONAL_NOTATION_DIGITS[:n])

        else:
            return False

    else:
        raise ValueError

    return output


def main():

    try:
        data = sys.argv
        if len(data) == 4:
            x = data[1]
            n = int(data[2])
            m = int(data[3])
        else:
            raise ValueError
    except (OSError, ValueError) as e:
        print(e)

    print(convert_n_to_m(x, n, m))


if __name__ == '__main__':
    main()

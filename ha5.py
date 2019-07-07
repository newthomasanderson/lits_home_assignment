#!/usr/bin/env python


import sys


def reverse_polish_notation(text):
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    string_with_brackets = [el for el in text if el in '{}[]()']
    stack = []

    for string in string_with_brackets:
        if string in opening_brackets:
            stack.insert(0, string)
        elif string in closing_brackets:
            if len(stack) == 0:
                return False
            if stack[0] == opening_brackets[closing_brackets.index(string)]:
                stack.pop(0)
            else:
                return False

    return bool(len(stack) == 0)


def main():

    try:
        data = sys.argv
        if len(data) == 2:
            text = data[1]

        else:
            raise ValueError
    except (OSError, ValueError) as e:
        print(e)

    print(reverse_polish_notation(text))


if __name__ == '__main__':
    main()

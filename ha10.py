#!/usr/bin/env python3


class CacheClass(dict):

    def __init__(self, func_to_decorate):
        self.func_to_decorate = func_to_decorate

    def __call__(self, *args):
        return self[args]

    def __missing__(self, key):
        result = self[key] = self.func_to_decorate(*key)
        return result


@CacheClass
def bar(a, b):
    print('calculating...')
    return a + b


def main():
    d = [[2, 2], [3, 2], [2, 2], [4, 1], [4, 1], [1, 4]]

    for el in d:
        print(bar(el[0], el[1]))
        print(bar)


if __name__ == '__main__':
    main()

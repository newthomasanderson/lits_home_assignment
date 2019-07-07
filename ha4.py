#!/usr/bin/env python


import sys
import re


def find_most_frequent(text):

    if isinstance(text, str):
        replaced_text = (re.sub("[,.:;!?-]", " ", text)).lower().split()
        counted_words = {el: replaced_text.count(el) for el in set(replaced_text)}
        freq_values = counted_words.values()
        freq_values.sort()
        new_list = [word for word, freq in counted_words.items() if freq == freq_values[-1]]
        new_list.sort()

        return new_list

    else:
        raise ValueError


def main():

    try:
        data = sys.argv
        if len(data) == 2:
            text = data[1]

        else:
            raise ValueError
    except (OSError, ValueError) as e:
        print(e)

    print(find_most_frequent(text))


if __name__ == '__main__':
    main()

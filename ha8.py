#!/usr/bin/env python


import sys
import random

CURRENCY_TEXT = {'0': 'hryven', '1': 'hryvna', '2': 'hryvni', '3': 'hryvni', '4': 'hryvni',
                 '5': 'hryven', '6': 'hryven', '7': 'hryven', '8': 'hryven', '9': 'hryven'}
BEFORE_100 = {'0': 'nul', '1': 'odna', '2': 'dvi', '3': 'try', '4': 'chotyry', '5': 'pyat', '6': 'shist',
              '7': 'sim', '8': 'visim', '9': 'devyat', '10': 'desyat', '11': 'odynadtsyat', '12': 'dvanadtsyat',
              '13': 'trynadtsyat', '14': 'chotyrnadtsyat', '15': 'pyatnadtsyat', '16': 'shistnadtsyat',
              '17': 'simnadtsyat', '18': 'visimnadtsyat',
              '19': 'devyatnadtsyat', '20': 'dvadtsyat', '30': 'trydtsyat', '40': 'sorok', '50': 'pyatdesyat',
              '60': 'shistdesyat', '70': 'simdesyat', '80': 'visimdesyat', '90': 'devyanosto'}
SOT = {'100': 'sto', '200': 'dvisti', '300': 'trysta', '400': 'chotyrysta', '500': 'pyatsot',
       '600': 'shistsot', '700': 'simsot', '800': 'visimsot', '900': 'devyatsot'}
TYS = {'1000': 'tysyacha', '2000': 'tysyachi', '3000': 'tysyachi', '4000': 'tysyachi', '5000': 'tysyach',
       '6000': 'tysyach', '7000': 'tysyach', '8000': 'tysyach', '9000': 'tysyach'}


def dict_substitution(num):

    if int(num) < 20:
        return '{}'.format(BEFORE_100[num])
    if int(num) < 100:
        if int(num) % 10 == 0:
            return '{}'.format(BEFORE_100[num])
        else:
            return '{} {}'.format(BEFORE_100[str(int(num) // 10 * 10)], BEFORE_100[str(int(num) % 10)])
    if int(num) < 10**3:
        if int(num) % 100 == 0:
            return '{}'.format(SOT[num])
        else:
            return '{} {}'.format(SOT[str(int(num) // 100) + '00'], dict_substitution(str(int(num) % 100)))
    if int(num) < 10**4:
        return '{} {} {}'.format(dict_substitution(str(int(num) // 10 ** 3)),
                                 TYS[str(int(num) // 10 ** 3) + '000'],
                                 dict_substitution(int(num) % 10 ** 3))
    if int(num) < 10**5:
        return '{} {} {}'.format(dict_substitution(str(int(num) // 10 ** 3)), TYS['9000'],
                                 dict_substitution(int(num) % 10**3))


def main():

    try:
        data = sys.argv
        if len(data) == 2:
            num = data[1]
        else:
            num = str(random.randint(0, 100000))
            print_num = True

        if int(num) > 10 ** 5:
            return "Out of range"
        else:
            raise ValueError
    except (OSError, ValueError) as e:
        print(e)

    if int(num[-2:]) < 10:
        curr_text = CURRENCY_TEXT[str(int(num[-2:]))]
    else:
        curr_text = CURRENCY_TEXT[str(int(num[-1:]))]

    if not print_num:
        print('Translated value is: {} {}'.format(dict_substitution(num), curr_text))
    else:
        print('Generated random value is: {}'.format(num))
        print('Translated value is: {} {}'.format(dict_substitution(num), curr_text))


if __name__ == '__main__':
    main()

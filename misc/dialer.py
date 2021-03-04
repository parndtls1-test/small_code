def phone_number(keys):
    if isinstance(keys, int):
        keys = str(keys)

    keypad = {'1': '', '11': '', '111': '',
            '2': 'a', '22': 'b', '222': 'c',
            '3': 'd', '33': 'e', '333': 'f',
            '4': 'g', '44': 'h', '444': 'i',
            '5': 'j', '55': 'k', '555': 'l',
            '6': 'm', '66': 'n', '666': 'o',
            '7': 'p', '77': 'q', '777': 'r', '7777': 's',
            '8': 't', '88': 'u', '888': 'v',
            '9': 'w', '99': 'x', '999': 'y', '9999': 'z',
            '0': ' ',
            '': ''
            }

    s, result = '', ''

    for letter in keys:
        print(letter)
        print(s)
        if len(s) > 0 and (s[-1] != letter or (s+letter) not in keypad):
            result += keypad[s]
            s = ''

        s += letter

    result += keypad[s]
    return result

print(phone_number(234))

import sys
ANSWER = 0
TOTAL = 69
NUMBER = 3


def get_exponent():
    for x in range(1, TOTAL):
        exponent_check = NUMBER ** x

        if exponent_check >= TOTAL:
            exponent = x - 1
            left_over = TOTAL - (NUMBER ** exponent)
            return exponent, left_over


def total_check(num):
    if num == 0:
        print(num)
        sys.exit()

    return num

while TOTAL > NUMBER:
    exponent, left_over = get_exponent()
    print(exponent, left_over)
    ANSWER += exponent
    TOTAL = total_check(left_over)
    print(TOTAL)
    print(ANSWER)
    print()

print(ANSWER+1)


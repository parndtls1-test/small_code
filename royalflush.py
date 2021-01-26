import random
import time

royal_flush_odds = 649739
magic_number = 13
counter = 0
x = 0

while magic_number != x:
    time.sleep(.5)
    x = random.randrange(royal_flush_odds)
    print(x)
    counter += 1

print('done')
print(counter)
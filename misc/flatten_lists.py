from collections import Iterable

def deep_flatten(l):
    for el in l:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from deep_flatten(el)
        else:
            yield el


x = deep_flatten([[(1, 2), (3, 4)], [(5, 6), (7, 8)]])
print(list(x))

#[1, 2, 3, 4, 5, 6, 7, 8]
x = deep_flatten([[1, [2, 3]], 4, 5])
print(list(x))
#[1, 2, 3, 4, 5]




def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = [f'{k}={v}' for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)
        print(f'{fn.__name__}({args_str}) took {elapsed:.6f}s to run')

        return result

    return inner

# fibonacci numbers, recursion, loop, reduce
# 1, 1, 2, 3, 5, 8, 13 .....
def fib_recursion(n): # not efficient
    if n <= 2:
        return 1
    return fib_recursion(n-1) + fib_recursion(n-2)

#print(fib_recursion(3))
@timed
def fib_recursive(n): # only 1 closure
    return fib_recursion(n)

# loop
@timed
def fib_loop(n): # bit more efficient
    fib_1, fib_2 = 1, 1

    for _ in range(3, n+1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2

# reduce
from functools import reduce
@timed
def fib_reduce(n):
    initial = (1, 0)
    dummy = range(n)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]),
	               dummy, initial)
    return fib_n[0]

print(fib_recursive(25))
print(fib_loop(25))
print(fib_reduce(25))

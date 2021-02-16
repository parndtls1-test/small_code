def fib(n):
    print(f'fib {n}')
    return 1 if n < 3 else fib(n-1) + fib(n-2)

#print(fib(10))

class Fib:
    def __init__(self):
        self.cache = {1: 1, 2: 1}

    def fib(self, n):
        if n not in self.cache:
            print(f'fib {n}')
            self.cache[n] = self.fib(n-1) + self.fib(n-2)    
        return self.cache[n]

f1 = Fib()
#print(f1.fib(10))

def fib_closure():
    cache = {1: 1, 2: 1}

    def calc_fib(n):
        if n not in cache:
            print(f'fib {n}')
            cache[n] = calc_fib(n-1) + calc_fib(n-2)    
        return cache[n]

    return calc_fib

f2 = fib_closure()
#print(f2(10))    
# new instance, has to recalculate
f3 = fib_closure()
#print(f3(10))   

def memoize(fn):
    cache = dict()

    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]

    return inner

@memoize
def fib(n):
    print(f'fib {n}')
    return 1 if n < 3 else fib(n-1) + fib(n-2)    

print(fib(10)) 
print(fib(10)) # 2nd time no calculations
print(fib(11)) # only needs to do 11

@memoize
def fact(n):
    print(f'fact {n}')
    return 1 if n < 2 else n * fact(n-1)

print(fact(10))    
print(fact(11))

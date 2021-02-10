def counter(fn):
    count = 0
	
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'func {fn} was called {count} times')
        return fn(*args, **kwargs)
		
    return inner
	
def add(a:int, b:int=0):
    '''add two integers'''
    return a + b
	
id(add)	# def add function
add = counter(add)
id(add) # new inner function
print(add(10, 20))
print(add(10))
print(add(20,40))

def mult(a: int, b: int=1):
    '''multiply two integers'''
    return a * b
	
mult = counter(mult)
print(mult(1, 2))
print(mult(1))
print(mult(3, 8))

# --or-- user decorator
@counter
def add2(a:int, b:int=0):
    '''add two integers'''
    return a + b

print(add2(10, 20))
print(add2(10))
print(add2(20,40))

@counter
def mult2(a: int, b: int=1):
    '''multiply two integers'''
    return a * b
	
print(mult2(1, 2))
print(mult2(1))
print(mult2(3, 8))

	




	
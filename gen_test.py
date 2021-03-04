def afunc():
    for i in range(1,4):
        yield i

x = afunc()
print(x)
print(next(x))
next(x)
print(next(x))

y = {x:x**x for x in range(1,6)}
print(y)


astring = 'A clear and open and spacious day. Only you can prevent forest fires.'
vowels = 'aeiou'

count = 0
for letter in astring:
    if letter.lower() in vowels:
        count += 1

print(count)

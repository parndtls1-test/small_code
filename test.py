x = [1,2,3,4,6]
y = [t - s for s, t in zip(x, x[1:])]
y.append(0)
print(y)
spot = 0
first = None
last = None

for i, j in enumerate(x):
    print(i,j)
    if y[i] == 1:
        last = j
        if not first:
            first = j


print(first, last)
x = [10, 2, 3, 1]

res = 0
idx = 0

while idx <= len(x)-1:
    for item in x[idx+1:]:

        if x[idx] > item:
            res += 1
    idx += 1

print(res)

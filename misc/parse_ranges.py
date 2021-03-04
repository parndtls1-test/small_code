def parse_ranges(astr):
    final = list()
    for items in astr.split(','):  
        nums = [int(x) for x in items.split('-')]
        final.extend((y for y in range(min(nums),max(nums)+1)))
    return final  

print(parse_ranges('1-2,4-4,8-10'))  
print(parse_ranges('0-0, 4-8, 20-20, 43-45'))
